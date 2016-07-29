import os
import numpy
import tarfile
dir1="/media/lijian/G/train_tar/"
dir2="/media/lijian/G/train/"

def extract(tar_path, target_path):
    try:
        tar = tarfile.open(tar_path, "r:tar")
        file_names = tar.getnames()
        for file_name in file_names:
            tar.extract(file_name, target_path)
        tar.close()
    except Exception, e:
        raise Exception, e

for dir in os.listdir(dir1):
  tardir=dir1+dir
  temp=dir.split('.')
  targetdir=dir2+temp[0]
  print tardir,targetdir
  extract(tardir,targetdir)
