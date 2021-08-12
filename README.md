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
 
You may install the packages (except tkinter on Linux) via `pip install packageXY` or `pip3 install packageXY` (if you have Python2 installed and set as default). 

The tkinter package has some system dependencies. You may install this package via `sudo apt-get install python3-tk` (on Ubuntu systems).

In addition, the SRAtoolkit is required. If you have not installed it you may use our simple install and configuration script see [below](#sratoolkit-install-script)

## Download scripts
To download simply clone this repository.

```
git clone https://github.com/mdsufz/downloadtool
cd hmgdb_script # change to the direction of the scripts
```

The download tool use the SRAtoolkit to download metagenome data. The SRAtoolkit offers very stable and fast download. If you have not installed the SRAtoolkit you can use our install and configuration script. 

### Graphical user interface (GUI)
We developed an east-to-use GUI to perform all relevant steps. Execute the `python download_gui.py` script to start the GUI. 

![gui interface](gui.png "GUI interface")

To install the SRAtoolkit click button at the bottom. To download metagenome sample. Select the CSV file, an output folder and the location of the SRAtoolkit folder and start download with the ***Start Download*** button. There are input field for optional parameters of [maximal file size](#maximal-file-size) and [CPU cores](cpu-cores) to use. The parameters are explained below.


### Python scripts

All script are written for Python3, thus use `python3` instead of `python` to call the script if you have Python2 install too and set as default. You can call the help to see required parameters via:

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

The Windows executables are compiled in Win10 64bit and can be used without installing Python and its dependencies on Windows.

The GUI can be started with double click on the exe. 

Due to the need of parameter input (e.g. output folder) the other executable must be started from the command-line. Open the Windows `CMD` navigate to the executable and use the parameters similar to the Python scripts:

The command-line executables can be used similar to the Python scripts:

```
# install SRAtoolkit
install_sra.exe -p install_path

# download metagenome samples
get_sra_sample.exe -c ...

```

### Optional parameters

#### Maximal file size
The parameter controls the maximal file size that the SRAtoolkit will download. The file size is given in GB.

#### CPU cores
The SRAtoolkit can use multiple cores/threads to create the FASTQ files are download. More CPUs will speed up this process.

