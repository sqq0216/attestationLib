from django.shortcuts import render
import requests
import unittest
from unittest import TestCase
import random
import string
from django.http import JsonResponse

base_url = "https://www.baidu.com/"

# enclave 认证接口1（sigrl）
def sig_attest(request):
    # api_url = base_url + "attestation/sgx/v3/sigrl/" + gid
    # headers = {'Ocp-Apim-Subscription-Key': '801e6f2c64a74f5ca3b0e25749add6ed'}
    sig_resp = requests.get(base_url)
    if sig_resp.status_code == 200:
        return JsonResponse({'status':200, 'message':'认证成功'})
        print("attestation successful")
    else:
        return JsonResponse({'status':404, 'message':'认证失败'})
        print("attestation failed")



class IasApiTest(TestCase):
    def setUp(self):
        self.baseUrl = "https://test-as.sgx.trustedservices.intel.com/"
        print("开始认证，baseUrl=",self.baseUrl)

    def tearDown(self):
        print("认证结束")

    def test_get(self):
        apiUrl = "/attestation/sgx/v3/sigrl/A3291A3"
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

#if __name__ == "__main__":
#     # unittest.main(verbosity=2)
#     suit = unittest.TestSuite()
#     suit.addTest(IasApiTest("test_test"))
#     runner = unittest.TextTestRunner()
#     runner.run(suit)


    