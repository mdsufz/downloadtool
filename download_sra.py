### Function that are used to install SRAtoolkit and download SRA metagenomes
###  including helper functions

### imports
from platform import system as plat_system
from platform import uname
from distro import linux_distribution
from urllib.request import urlretrieve
from os.path import join, isdir, isfile
from os import system, remove
from zipfile import ZipFile
import tarfile

### SRAtoolkit download
# get OS
def get_OS():
    plat = plat_system()
    print('Detected system: '+plat)
    if plat == "Linux":
        # linux
        return plat
    elif plat == "Darwin":
        # MAC OS X
        return plat
    elif plat == "Windows":
        # Win
        return plat
    else:
        return 'none'

# download SRAtoolkit
def download_sratoolkit(downloadPath):
    # get OS
    my_os = get_OS()

    # check if path exists
    if not isdir(downloadPath):
        print('Download directory does not exist: '+downloadPath+'. Create the directory or select another one.')
    elif (my_os == 'Windows') or (my_os == "Linux") or (my_os == "Darwin"):
        # print status
        print('Downloading SRAtoolkit for: ',my_os)
        # Win
        if my_os == "Windows":
            # download
            urlretrieve('https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.11.0/sratoolkit.2.11.0-win64.zip', join(downloadPath, 'sratoolkit.2.11.0-win64.zip'))
            # unzip 
            with ZipFile(join(downloadPath, 'sratoolkit.2.11.0-win64.zip'),"r") as zip_ref:
                zip_ref.extractall(join(downloadPath))
            remove(join(downloadPath, 'sratoolkit.2.11.0-win64.zip'))
            # print status
            print('Download DONE')
        elif my_os == "Linux":
            plat_uname = uname()
            if 'Ubuntu' in plat_uname[3]:
                urlretrieve('http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz', join(downloadPath, 'sratoolkit.current-ubuntu64.tar.gz'))
                tar = tarfile.open(join(downloadPath, 'sratoolkit.current-ubuntu64.tar.gz'), "r:gz")
                tar.extractall(downloadPath) #'./my_folder'
                tar.close()
                remove(join(downloadPath, 'sratoolkit.current-ubuntu64.tar.gz'))
                # print status
                print('Download DONE')
            elif 'CentOS' in linux_distribution()[0]:
                urlretrieve('http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-centos_linux64.tar.gz', join(downloadPath, 'sratoolkit.current-centos_linux64.tar.gz'))
                tar = tarfile.open(join(downloadPath, 'sratoolkit.current-centos_linux64.tar.gz'), "r:gz")
                tar.extractall(downloadPath)
                tar.close()
                remove(join(downloadPath, 'sratoolkit.current-centos_linux64.tar.gz'))
                # print status
                print('Download DONE')
            else:
                print('No pre build found for your linux. Check https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit')
        elif my_os == "Darwin":
            urlretrieve('https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.11.0/sratoolkit.2.11.0-mac64.tar.gz', join(downloadPath, 'sratoolkit.2.11.0-mac64.tar.gz'))
            tar = tarfile.open(join(downloadPath, 'sratoolkit.2.11.0-mac64.tar.gz'), "r:gz")
            tar.extractall()
            tar.close()
            remove(join(downloadPath, 'sratoolkit.2.11.0-mac64.tar.gz'))
            # print status
            print('Download DONE')
    else:
        # print status
        print('No SRAtoolkit for your system found.')

# configure sratoolkit
def config_sratoolkit(toolPath):
    # get OS
    my_os = get_OS()

    # configure SRAtoolkit
    if (my_os == 'Windows') or (my_os == "Linux") or (my_os == "Darwin"):
        if my_os == "Windows":
            # check tool is present
            if not isfile(join(str(toolPath).replace('/','\\'),'bin','vdb-config.exe')):
                print('No vdb-config found in '+join(str(toolPath).replace('/','\\'),'bin')) 
            else:
                system('echo & echo.|'+join(str(toolPath).replace('/','\\'),'bin','vdb-config')+' -i --interactive-mode textual')
                system("FOR /F %i IN ('powershell -Command \"[guid]::NewGuid().ToString()\"') DO echo /LIBS/GUID = \"%i\" >> \"%systemdrive%%homepath%\\.ncbi\\user-settings.mkfg\"")
        else:
            # check if tool is present
            print(join(str(toolPath),'bin','vdb-config'))
            vdb_config_path = join(str(toolPath),'bin','vdb-config')
            if not isfile(join(str(toolPath),'bin','vdb-config')):
                print('No vdb-config found in '+join(str(toolPath),'bin'))
            else:
                system("echo | "+vdb_config_path+" -i --interactive-mode textual")
                system("printf '/LIBS/GUID = \"%s\"\n' `uuidgen` >> ~/.ncbi/user-settings.mkfg")
    else:
        # print status
        print('SRAtoolkit not detected for your system.')
		
### Metagenome file download
# open csv and extract SRA and MGRast sample
def get_ids(csvPath):
	l="a"
	f=open(csvPath,"r")
	mgrast_list=[]
	sra_list=[]
	header=f.readline()
	while True:
		l=f.readline()
		if not l: break
		else:
			# get id
			id=l.split(",")[0]
			# remove quote
			id = id.replace('"', '')
            # assign to MGrast or SRA list
			if "mg" in id:
				mgrast_list.append(id)
			else:
				sra_list.append(id)
	f.close()
	return sra_list, mgrast_list

# download sample
def download_samples(csvPath, outPath, toolPath, numThreads=2, maxSize='20G'):
    # get OS
    my_os = get_OS()

    # read csv
    sra_list, mgrast_list = get_ids(csvPath)
    # status that only sra samples will be downloaded
    if mgrast_list == []:
        print('Only SRA sample will be downloaded. MGRast not available for download.\n')
    
    # for each entry
    for i in sra_list:
        # status print
        print (i+" started...")
        
        # prefetch the reads
        system(join(toolPath,'bin','prefetch')+" "+i+" -p --max-size "+str(maxSize)+" -O "+join(outPath))
        
        # check if SRA file was prefetched
        if isfile(join(outPath,i,i+'.sra')):
            # validate the download
            if my_os == 'Windows':
                # win
                system(join(toolPath,'bin','vdb-validate')+" "+join(outPath,i)+" 1> "+join(outPath,i,i+".intlog")+" 2>&1")
            else:
                # linux
                system(join(toolPath,'bin','vdb-validate')+" "+join(outPath,i)+" 2> "+join(outPath,i,i+".intlog"))
            
            # extract the reads from the prefetched files
            system(join(toolPath,'bin','fasterq-dump')+" -p -e "+str(numThreads)+" -O "+join(outPath,i)+" "+i)

        # status print
        print(i+" FINISHED!\n")
