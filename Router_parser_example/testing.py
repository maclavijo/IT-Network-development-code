import unittest
from routerparser import routerParser

class test_routerparser(unittest.TestCase):

    def setUp(self):
        self.info = routerParser()

    def test_name(self):
        parsedNames = self.info.custNames()
        #print(parsedNames)
        routerNames = ['CUST_A','CUST_B']
        self.assertEqual(list, type(parsedNames))
        self.assertEqual(routerNames, parsedNames)

    def test_custInfo(self):
        customer_info = self.info.custInfo('CUST_B')
        print(customer_info)
        vlans = ['GigabitEthernet0/0.200', '200', '172.16.200.1']
        self.assertEqual(vlans, customer_info)

if __name__ == '__main__':
    unittest.main()