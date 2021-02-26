import re
import json

class routerParser():

    #Read router output
    config = open('router.txt', 'r').read()

    #Get customer names
    def custNames(self):
        '''
        Returns: list with name of customers
        '''
        nameRegex = r'ip vrf forwarding (.*)\n'
        names = re.findall(nameRegex, self.config)
        return names

    #Get interface, vlan and ip address
    def custInfo(self,customer):
        ''' Args:
                customer: Name of customer
            Returns: interface, vlan and ip address
        '''
        infoRegex = (
            r'interface (.*)\n'
            r'\s+encapsulation dot1Q (.*)\n'
            r'\s+ip vrf forwarding %s\n'
            r'\s+ip address (.*) (.*)\n' % customer
       )
        parsedInfo = re.search(infoRegex, self.config)
        return [parsedInfo.group(1),parsedInfo.group(2),parsedInfo.group(3), parsedInfo.group(4)]

    #First find customers, then find other info
    def parsedInfo(self):
        '''Returns: Json with all router info'''
        finalInfo = {}
        customers = routerParser().custNames()
        for customer in customers:
            finalInfo[customer] = routerParser().custInfo(customer)
        return json.dumps(finalInfo,indent=2)

print(routerParser().parsedInfo())