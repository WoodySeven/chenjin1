#!/usr/bin/env python

import os

#def crawl_dirname():
def crawl_dirname(FilePath):

    fileList = os.listdir(FilePath)
    fp = open('myfile.txt', 'w')
    for filename in fileList:
        list_name = os.path.join(FilePath, filename)
        print(list_name)
        fp.writelines(b"{}\n".format(list_name).encode('utf-8'))
    fp.close()


if __name__ == "__main__":
    filepath = r"D:\GitHub\autotest7"
    print(crawl_dirname(filepath))