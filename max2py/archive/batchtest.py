# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:59:00 2018

@author: User
"""

from subprocess import Popen
p = Popen("batch.bat", cwd=r"C:\Users\User\Desktop\Marking\py2max")
stdout, stderr = p.communicate()