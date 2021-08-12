# Repository of the Download Tool for the MarMDB 

The [Python scripts](#python-scripts) can be used on all operating systems. For Windows (Win10) we recommend to use the [Windows executable](#windows-executables) that are provided for easy use without the installation of Python or any dependencies.

## Compatibility to other metadata databases
The Download tool is compatible with exported CSV tables from the TerrestrialMetagenomeDB [Website](https://webapp.ufz.de/tmdb/) [Publication](https://academic.oup.com/nar/article/48/D1/D626/5625925) [PubMed](https://pubmed.ncbi.nlm.nih.gov/31728526/) and the HumanMetagenomeDB [Website](https://webapp.ufz.de/hmgdb/), [Publication](https://academic.oup.com/nar/article/49/D1/D743/5998395), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33221926/). 

## Dependencies and Requirements

The scripts are written in Python3. The following Python Packages are necessary:

* tkinter
* os
* re
* platform
* urllib.request
* zipfile
* tarfile
* distro
 
The tkinter package has some system dependencies. You may install this package via `sudo apt-get install python3-tk` (on Ubuntu systems).

You may install the packages (except tkinter on Linux) via `pip install packageXY` or `pip3 install packageXY` (if you have Python2 installed and set as default). To install all at once:

```
pip install os re platform urllib.request zipfile tarfile distro
```

The tkinter package has some system dependencies. You may install this package via `sudo apt-get install python3-tk` (on Ubuntu systems).

In addition, the [SRAtoolkit](https://github.com/ncbi/sra-tools) is required. If you have not installed it you may use our simple install and configuration script see [below](#sratoolkit-install-script)

## Download scripts
To download all scripts clone this repository:

```
git clone https://github.com/mdsufz/downloadtool.git
```

The download tool uses the [SRAtoolkit](https://github.com/ncbi/sra-tools) to download metagenome data. The [SRAtoolkit](https://github.com/ncbi/sra-tools) offers very stable and fast download. If you have not installed the SRAtoolkit you can use our install and configuration script. 

### Graphical user interface (GUI)
We developed an east-to-use GUI to perform all relevant steps. Execute the `python download_gui.py` script to start the GUI. 

![The GUI interface](gui.png "GUI interface")

To install the SRAtoolkit click ***Download and configure SRAtoolkit*** button at the bottom. The download size is around 70MB and is completed if you get the notification.

To download metagenome sample. Select the CSV export file from MarMDB, an output folder and the location of the SRAtoolkit folder and start download with the ***Start Download*** button. There are input field for optional parameters of [maximal file size](#maximal-file-size) and [CPU cores](cpu-cores) to use. The parameters are explained below.


### Python scripts

All script are written for Python3, thus use `python3` instead of `python` to call the script if you have Python2 install too and set as default. You may call the help to see required parameters (details explained below) via:

```
# call help
python install_sra.py -h
python get_sra_sample.py -h
```

#### SRAtoolkit install script

If you have not install SRAtoolkit you can use our install script. It performs the download and configuration. To run the install script run 

```
# install SRAtoolkit
python install_sra.py -p install_path` 
```

#### Download script

The download script requires 3 mendatory and 2 optional parameters: 

* CSV path (`-c` or `--csv-path`): the path to the CSV export file from MarMDB.
* output path (`-o` or `--out-path`): the path of the folder where all download and dumped metagenome data will be written.
* tool path (`-l` or `--tool-path`): the path to the folder where the SRAtoolkit was installed.
* [optional] [threads](#cpu-cores): `-t` or `--threads`
* [optional] [max file size](#maximal-file-size) `-m` or `--max-size`

The download script can be call via:

```
# download SRA files and create FASTQ files
python get_sra_sample.py -c csv_path -o output_path -l too_path -t 2 -m 20
```

### Windows executables

The Windows executables are compiled on Win10 64bit and can be used without installing Python and its dependencies on Windows.

The GUI can be started with double click on the `download_gui.exe`. We apologize the safty check question when starting this executable due to missing Windows signature.

Instead of the GUI you may want to use the command-line version of the single executables. Open the Windows terminal (`CMD`) navigate to the executable (`cd path_to_exe`) and use the parameters similar to the Python scripts:

The command-line executables can be used similar to the [Python scripts](#python-scripts), the parameters are identical:

```
# install SRAtoolkit
install_sra.exe -p install_path

# download metagenome samples
get_sra_sample.exe -c csv_path -o output_path -l too_path -t 2 -m 20

```

### Optional parameters

#### Maximal file size
The parameter controls the maximal file size that the SRAtoolkit will download. The file size is given in GB.

#### CPU cores
The SRAtoolkit can use multiple cores/threads to create the FASTQ files are download. More CPUs will speed up this process.

