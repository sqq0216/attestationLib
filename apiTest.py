import requests
import unittest
from unittest import TestCase

class IasApiTest(TestCase):
    def setUp(self):
        self.baseUrl = "https://api.trustedservices.intel.com/sgx/dev"
        print("开始认证，baseUrl=",self.baseUrl)

    def tearDown(self):
        print("认证结束")

    def test_get(self):
        apiUrl = "/attestation/v3/sigrl/00000000"
        url = self.baseUrl + apiUrl
        # url1 = "https://api.trustedservices.intel.com/sgx/attestation/v3/sigrl/00000010"
        print("当前访问url为",url)
        headers = {'Ocp-Apim-Subscription-Key': '801e6f2c64a74f5ca3b0e25749add6ed'}
        r = requests.get(url, headers=headers)
        # r_json = r.json()
        print("status_code is :", r.status_code)
        print("response is ", r.text)
        # print(r.json())

    def test_post(self):
        apiUrl = "/attestation/v3/report"
        url = self.baseUrl + apiUrl
        headers = {'Ocp-Apim-Subscription-Key':'801e6f2c64a74f5ca3b0e25749add6ed'}
        body = {"isvEnclaveQuote":"AAEAAAEAAA+yth5<...encoded_quote...>GuOKBJ+5cs0PQcnZp"}
        res = requests.post(url,headers=headers, json=body)
        print("status_code is :", res.status_code)
        print("response is ", res.headers)
        print("response body is :", res.text)
        if res.status_code == 200:
            print("认证成功")
        else:
            print("认证失败")

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suit = unittest.TestSuite()
    suit.addTest(IasApiTest("test_post"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    