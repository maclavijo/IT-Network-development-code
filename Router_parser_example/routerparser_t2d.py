from tabulate import tabulate
from textfsm import TextFSM
import json

class routerparser():

    config = open('router.txt', 'r').read()

    def parser(self):
        with open('router_template.tmpl','r') as template:
            regex_table = TextFSM(template)
            parser_header = regex_table.header
            parser_data = regex_table.ParseText(self.config)

        return parser_data,parser_header

#print tabulated data
print('--------------')
print('Tabulated data')
print('--------------')
data, header = routerparser().parser()
print(tabulate(data,headers=header ))

#print json format
print()
print('------------')
print('JSON Format')
print('------------')
for element in data:
    print(json.dumps(dict(zip(header,element)),indent=4))
