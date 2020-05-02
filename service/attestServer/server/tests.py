from django.test import TestCase
import requests
import unittest
from unittest import TestCase
import random
import string

# Create your tests here.
class IasApiTest(TestCase):
    def setUp(self):
        self.baseUrl = "https://api.trustedservices.intel.com/sgx/dev"
        print("开始认证")

    def tearDown(self):
        print("认证结束")

    def test_post(self):
            # apiUrl = "/attestation/v3/report"
            # url = self.baseUrl + apiUrl
            url_test = "http://127.0.0.1:8000/quote_attest/"
            print("当前访问地址为：",url_test)
            # headers = {'Ocp-Apim-Subscription-Key':'801e6f2c64a74f5ca3b0e25749add6ed'}
            body = {"isvEnclaveQuote":"AgABAI8LAAAKAAkAAAAAAOowCfk2OW73srd6ihwINLcAAAAAAAAAAAAAAAAAAAAADg4CBP8CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAfAAAAAAAAAEOHyd1bZIb5qHElFzWh5e2rCqbK1bOqdFnViGp62wfuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACD1xnnferKFHD2uvYqTXdDA8iZ22kCD5xw7h38CMfOngAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAIAAJEd+bif0yFBLdVurRkr0jl+QyosRpDSuxxhNIk7mEGGJzYljR3naNzIusPcD63vEGejqVX8LTz/k45u8BsLwHXEUz3ikBQSAcKEIgXFAiWgjvuVjlrkoMyBeH0zr3nri1e2uc7PeC076YohL344ArDMwQpRWtPZ4mZhTKA8KT+X6PBYAtCAZQGy5yRDHCe18tgQgVn1anT/TK2Z4RdSiBMhNtMbvUwy9RmZ/bqbb0JagwFw4SMmI9axCVO4MaKgP1CtA/EXGIeGWOkmHKC6zbh+iL6vZPN6nrwZItPA+vD+T1EylkkGp23wbhBI04vs6rIAT9HZJNovOIVQYj/WkrmRwfXvzY55Eik8I69y0PA00QpYU5lCr53tiJRKEMUKLuri4Hi2qzB6SwF75GgBAABz2etJpdBMHUwCE9E/cUHq4duX5txx2YMNS5taWrGx99dL9xFiF7j93JFJLbtvt6/XlM/AgrZ47I5qWQYOYMxBkVnw5zuR/BkREwGqmjtSsf8l7fvEdXd3xnR0w7+Eqm6ror8KW+Sj8E8JtMWkGCAXCgsLHerumfi7DUsBQx62CfrndojHT/h4+BEb/sZwancBzn1NBSx5ZeSVwh8mT+RFUPgZxQecF+CQkYDuSeaRxVxjLKF0lieYYG8Jagh3VCNFJkAlgy73Qwy2Tr3sD7TwPSLM/7axdRolMRCGkAqeFxz/PrWvmEnDUtAywrFBiidDoKzc1BwNV3JtGLlJHCuMI9Oi1n7j19ie1XiUSepNgdCsQ3zqNz5ZhTeBjNog3WiLP4cDySUHtQg2Kk4hCDhm6IBVAr7vPZDo/0ItreNO9HVciomS1Lh1cXW4HnXjXGy/HgjNaCv2SVLDopg7Oae7pnRCebad3jOGuWuVfWdC/b2U7cHuXhF2"}
            res = requests.post(url_test,body)
            print("+++++++响应内容：++++++ \n",res.text)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suit = unittest.TestSuite()
    suit.addTest(IasApiTest("test_post"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    