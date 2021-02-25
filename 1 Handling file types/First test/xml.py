# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:13:35 2021

@author: PcHouston
"""

import xml.etree.ElementTree as ET

with open('test1.xml','r') as file:
    mytree = ET.parse(file)
    myroot = mytree.getroot()
    
user = myroot.find('user')
print(user.find('name').text)

for role in user.findall('roles'):
    print(role.text)
    

user.find('location').find('city').text = 'San Antonio'

with open('new_file.xml','w') as file:
    mytree.write(file, encoding='unicode')
    
    