# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:01:33 2021

@author: PcHouston
"""

import yaml
import json

with open ('yaml_test.yml','r') as file:
    data = yaml.safe_load(file)
    
user = data['user']
print(user['name'])

for role in user['roles']:
    print(role)
    

user['location']['city'] = 'Houston'
with open('new_test.json','w') as file:
    json.dump(data, file, indent=4)