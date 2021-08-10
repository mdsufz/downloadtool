# Repository of the Download Tool for the MarMDB 

The Python script can be used on all Operating Systems. Windows executable are provided for easy use on Windows without the need to install Python or any dependencies.

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
 
You may install the packages (except tkinter on Linux) via `pip install packageXY` or `pip3 install packageXY` (if you have Python2 installed and set as default). 

The tkinter package has some system dependencies. You may install this package via `sudo apt-get install python3-tk` (on Ubuntu systems).

In addition, the SRAtoolkit is required. If you have not installed it you may use our simple install and configuration script see [below](#sratoolkit-install-script)

## Download scripts
git clone https://github.com/mdsufz/downloadtool
cd hmgdb_script # change to the direction of the scripts

The download tool use the SRAtoolkit to download metagenome data. The SRAtoolkit offers very stable and fast download. If you have not installed the SRAtoolkit you can use our install and configuration script. 

### Graphical user interface (GUI)
We developed a east-to-use GUI to perform all relevant steps. Execute the `python download_gui.py` script to start the GUI. 

![gui interface](gui.png "GUI interface")

To install the SRAtoolkit click button at the bottom. To download metagenome sample. Select the CSV file, an output folder and the location of the SRAtoolkit folder and start download with the ***Start Download*** button. There are input field for optional parameters of [maximal file size](#maximal-file-size) and [CPU cores](cpu-cores) to use. The parameters are explained below.


### Python scripts

#### SRAtoolkit install script

If you have not install SRAtoolkit you can use our install script. It performs the download and configuration. To run the install script `python install_sra.py -p install_path`. 

#### Download script

The download script will download ...

### Windows executables

The Windows executables are compiled in Win7 64bit and can be used without installing Python and its dependencies on Windows.

The GUI can be started with double click on the exe. 

Due to the need of parameter input (e.g. output folder) the other executable must be started from the command-line. Open the Windows `CMD` navigate to the executable and use the parameters similar to the Python scripts:

## Parameters

### Maximal file size
The parameter controls the maximal file size that the SRAtoolkit will download. It is given in GB.

### CPU cores
The SRAtoolkit can use multiple cores to create the FASTQ files are download. More CPUs will speed up this process.

