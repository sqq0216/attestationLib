from django.shortcuts import render
import requests
import unittest
from unittest import TestCase
import random
import string
from django.http import JsonResponse
import logging

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

# encalve 认证接口2(quote)
def quote_attest(request):
    quote_data = request.POST.get('isvEnclaveQuote')
    
    if quote_data is None:
        return JsonResponse({'status':10021,'message':'parameter error'})

    url = "https://api.trustedservices.intel.com/sgx/dev/attestation/v4/report"
    headers = {'Ocp-Apim-Subscription-Key':'801e6f2c64a74f5ca3b0e25749add6ed'}
    # body = {"isvEnclaveQuote": "AgABAI8LAAAKAAkAAAAAAOowCfk2OW73srd6ihwINLcAAAAAAAAAAAAAAAAAAAAADg4CBP8CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAfAAAAAAAAAEOHyd1bZIb5qHElFzWh5e2rCqbK1bOqdFnViGp62wfuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACD1xnnferKFHD2uvYqTXdDA8iZ22kCD5xw7h38CMfOngAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAIAAJEd+bif0yFBLdVurRkr0jl+QyosRpDSuxxhNIk7mEGGJzYljR3naNzIusPcD63vEGejqVX8LTz/k45u8BsLwHXEUz3ikBQSAcKEIgXFAiWgjvuVjlrkoMyBeH0zr3nri1e2uc7PeC076YohL344ArDMwQpRWtPZ4mZhTKA8KT+X6PBYAtCAZQGy5yRDHCe18tgQgVn1anT/TK2Z4RdSiBMhNtMbvUwy9RmZ/bqbb0JagwFw4SMmI9axCVO4MaKgP1CtA/EXGIeGWOkmHKC6zbh+iL6vZPN6nrwZItPA+vD+T1EylkkGp23wbhBI04vs6rIAT9HZJNovOIVQYj/WkrmRwfXvzY55Eik8I69y0PA00QpYU5lCr53tiJRKEMUKLuri4Hi2qzB6SwF75GgBAABz2etJpdBMHUwCE9E/cUHq4duX5txx2YMNS5taWrGx99dL9xFiF7j93JFJLbtvt6/XlM/AgrZ47I5qWQYOYMxBkVnw5zuR/BkREwGqmjtSsf8l7fvEdXd3xnR0w7+Eqm6ror8KW+Sj8E8JtMWkGCAXCgsLHerumfi7DUsBQx62CfrndojHT/h4+BEb/sZwancBzn1NBSx5ZeSVwh8mT+RFUPgZxQecF+CQkYDuSeaRxVxjLKF0lieYYG8Jagh3VCNFJkAlgy73Qwy2Tr3sD7TwPSLM/7axdRolMRCGkAqeFxz/PrWvmEnDUtAywrFBiidDoKzc1BwNV3JtGLlJHCuMI9Oi1n7j19ie1XiUSepNgdCsQ3zqNz5ZhTeBjNog3WiLP4cDySUHtQg2Kk4hCDhm6IBVAr7vPZDo/0ItreNO9HVciomS1Lh1cXW4HnXjXGy/HgjNaCv2SVLDopg7Oae7pnRCebad3jOGuWuVfWdC/b2U7cHuXhF2"}
    body = {"isvEnclaveQuote":quote_data}
    response_data = requests.post(url,headers=headers, json=body)
    res_status = response_data.status_code
    res_body = response_data.text

    # 添加日志 ,返回数据作处理TODO  
    if res_status == 200:
        print("认证成功")
        return JsonResponse({'status':200,'message':'attest success','data':res_body})       
    else:
        return JsonResponse({'status':10023,'message':'event status is not available'})
        print("认证失败")
    
        
    



    