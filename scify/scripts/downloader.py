#!/usr/bin/python
import zipfile, requests, sys
from tqdm import tqdm
from dataset_urls import DATASET_URLS
import os
import shutil
import urllib.request as request
from urllib.request import urlretrieve
from contextlib import closing
#from urllib.request import urlretrieve
import gzip

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))


def download_ftp(url, target, ext="xml"):
    filename = target + "/" + url.split("/")[-1]
    urlretrieve(url, filename, reporthook)
    
    print("File Downloaded from " + url + " into " + target)
    #EVEN with unzipping the xml. Concierge Service
    if filename.endswith("gz"):
        with gzip.open(filename, 'rb') as f_in:
            with open(filename.split(".")[0] + "." + ext, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                print("Unzipped File: " + filename)
       
       
        """ with closing(request.urlopen(url)) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r, f)
   """

#url = "https://download.winzip.com/gl/nkln/winzip24-downwz.exe"
# download the body of response by chunk, not all at once
def download(url, target="data/", buffer_size=1024):
    try: 
        if not os.path.exists(target):
            os.makedirs(target)
            print("Directory '%s' created" %target) 

    except OSError as error: 
        print(error) 
    
    if ("ftp" in url):
        download_ftp(url, target)
        return


    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0)) #Content-Length header parameter is the total size of the file in bytes.
    
 

    filename = target + "/" + url.split("/")[-1]

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, 
    unit="B", unit_scale=True, unit_divisor=1024)

    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

    # get the file name

def unzip(data):
    with zipfile.ZipFile(data) as zf:
        for member in tqdm(zf.infolist(), desc='Extracting '):
            try:
                zf.extract(member, target_path)
            except zipfile.error as e:
                pass

def run(a,b,c):
    print(a or no, b or no, c or no)


if __name__ == "__main__":
    [download(url, target="data/pubmed") for url in DATASET_URLS["pubmed"]]
    #for filename in os.listdir(directory):
    #[download(url, target="data/gnbr") for url in DATASET_URLS["gnbr"][:2]] #chemical-gene files for now
    
    #TODO also make work for FTP
    
    # if you call it from command line then this:
    # download(*sys.argv[1:])
