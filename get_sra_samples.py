### script to download SRA metagenomes
# imports 
import download_sra as sra
import argparse
from os.path import join
from os import listdir 
from re import match

# parse arguements
parser = argparse.ArgumentParser(description='Description SRAtoolkit')
parser.add_argument('-c','--csv-path', help='Path to CSV file', required=True)
parser.add_argument('-o','--out-path', help='Output path', required=True)
parser.add_argument('-l','--tool-path', help='Path to SRAtoolkit', required=True)
parser.add_argument('-t','--threads', help='Number of threads to use', required=False, default='2')
parser.add_argument('-m','--max-size', help='Max size of download files', required=False, default='20G')
args = vars(parser.parse_args())

# identify sratoolkit sub-dircetory
files = [f for f in listdir(args['tool_path']) if match(r'sratoolkit', f)]
files = [f for f in files if not match(r'.*tar.gz', f)]
files = [f for f in files if not match(r'.*zip', f)]
if len(files)>0:
    tool_path = join(args['tool_path'],files[0])
else:
    tool_path = args['tool_path']

# download
sra.download_samples(args['csv_path'],args['out_path'],tool_path,args['threads'],args['max_size'])
