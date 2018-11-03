#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:33:56
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-11-02 22:39:28


import os
import shutil
file_path = os.path.dirname(__file__)
from msvcrt import getch

def install_package(python_path,package_name):
    with open(python_path + r'\Lib\site-packages\%s.pth'%(package_name,),'w') as f:
        f.write('#.pth file for the %s extensions\n'%(package_name,))
        f.write(package_name)
    
    shutil.copytree(r'.\%s'%(package_name),r'%s\Lib\site-packages\%s'%(python_path,package_name))
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>\npackage install succeed'
    print 'any key exit'
    getch()


if __name__ == '__main__':
    install_package('c:\\Python27','guiengine_trzp')
