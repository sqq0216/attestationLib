import requests
import unittest
from unittest import TestCase
import random
import string

class IasApiTest(TestCase):
    def setUp(self):
        self.baseUrl = "https://api.trustedservices.intel.com/sgx/dev"
        print("开始认证")

    def tearDown(self):
        print("认证结束")

    def test_get(self):
        # apiUrl = "/attestation/sgx/v3/sigrl/83291A3"
        # url = self.baseUrl + apiUrl
        url1 = "https://api.trustedservices.intel.com/sgx/dev/attestation/v4/sigrl/23291A3"
        # print("当前访问url为",url)
        headers = {'Ocp-Apim-Subscription-Key':'801e6f2c64a74f5ca3b0e25749add6ed'}
        r = requests.get(url1, headers=headers)
        # r_json = r.json()
        print("status_code is :", r.status_code)
        print("response is ", r.text)
        # print(r.json())

    
        
    def test_test(self):
        data = ' ' 
        s = 'EIDKFJ'
        data.join(s)
        print(data)
        # url = "https://www.baidu.com/"
        # res = requests.get(url)
        # print("status code is :", res.status_code)
        # if res.status_code == 200:
        #     print("认证成功")
        #     salt = ''.join(random.sample(string.ascii_letters + string.digits, 6))
        #     print(salt.encode(encoding='utf-8'))
        # else:
        #     print("认证失败")

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suit = unittest.TestSuite()
    suit.addTest(IasApiTest("test_post"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    