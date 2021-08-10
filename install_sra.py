### script to install and configure SRAtoolkit

# imports 
import download_sra as sra
import argparse
from os.path import join
from os import listdir 
from re import match

# parse arguements
parser = argparse.ArgumentParser(description='Description SRAtoolkit')
parser.add_argument('-p','--path', help='Download path', required=True)
args = vars(parser.parse_args())

# download 
sra.download_sratoolkit(args['path'])

# identify sratoolkit dirctory
files = [f for f in listdir(args['path']) if match(r'sratoolkit', f)]
files = [f for f in files if not match(r'.*tar.gz', f)]
files = [f for f in files if not match(r'.*zip', f)]
path = join(args['path'],files[0])

# configure
sra.config_sratoolkit(path)
