#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:33:56
# Contact: mrtang@nudt.edu.cn 
# Github: trzp
# Last Modified by:   mr tang
# Last Modified time: 2018-11-02 22:39:28

import os
import platform
import shutil


def install_package(package_name,python_path):
    if platform.system().lower() == 'windows':
        package_path = r'%s/Lib/site-packages'%(python_path,)
    elif platform.system().lower() == 'linux':
        package_path = r'%s/dist-packages'%(python_path)
    else:
        raise ImportError,'unsupported system platform %s'%(platform.system(),)

    if os.path.exists(r'%s\%s.pth'%(package_path,package_name)):
        os.remove(r'%s\%s.pth'%(package_path,package_name))

    if os.path.exists(r'%s/%s'%(package_path,package_name)):
        shutil.rmtree(r'%s/%s'%(package_path,package_name))

    shutil.copy(r'./%s/%s.pth'%(package_name,package_name),r'%s'%(package_path,))
    shutil.copytree(r'./%s'%(package_name),r'%s/%s'%(package_path,package_name))
    
def import_test():
    import guiengine
    print guiengine.__doc__

    print '>>>>>>>>>>>>>>>>>>>>>>>>>>\npackage installed'
    print 'any key exit'
    os.system('pause')

if __name__ == '__main__':
    #example for linux
    #使用import sys
    # sys.path查看python的路径
    #install_package('guiengine_trzp','/usr/lib/python2.7')
    #example for windows
    install_package('guiengine_trzp','c:/Python27')
    import_test()
