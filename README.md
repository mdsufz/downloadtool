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
 
You may install the packages (except tkinter on Linux) via 'pip install packageXY' or 'pip3 install packageXY' (if you have Python2 installed and set as default). 

The tkinter package has some system dependencies. You may install this package via 'sudo apt-get install python3-tk' (on Ubuntu systems).

## Download scripts
git clone https://github.com/mdsufz/downloadtool
cd hmgdb_script # change to the direction of the scripts

## Download tool usage
The download tool use the SRAtoolkit to download metagenome data. The SRAtoolkit offers very stable and fast download. If you have not installed the SRAtoolkit you can use our install and configuration script. 

### Graphical user interface (GUI)
We developed a east-to-use GUI to perform all relevant steps. Execute the 'download_gui.py' script to start the GUI. 

[img]

### Python scripts

#### SRAtoolkit install script

If you have not install SRAtoolkit you can use our install script. It performs the download and configuration. To run the install script 'python install 

### Windows executables



## Parameters


