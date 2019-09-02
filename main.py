import requests
from bs4 import BeautifulSoup as bs
import js2py
import base64


header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url="https://footdistrict.com"
class sucuriFirewall():

	def __init__(self):

		self.ua=header
		self.page=url

	def mainf(self):
		try:
			print("Requesting Home Page without cookies")
			req=requests.get(self.page, headers=self.ua)
			print("Parsing Sucuri Script...")
			soup=bs(req.text, 'html.parser')
			script=(soup.find('script'))
			scr=script.text
			a=(scr.split("(r)")[0][:-1]+"r=r.replace('document.cookie','var cookie');")
			print("Extracted internal script")
			b=(js2py.eval_js(a))
			print("Getting cookies")
			sucuri_cloudproxy_cookie=js2py.eval_js(b.replace("location.","").replace("reload();",""))
			cookies={sucuri_cloudproxy_cookie.split("=")[0]:sucuri_cloudproxy_cookie.split("=")[1].replace(";path","")}
			print(cookies)

			req=requests.get("https://footdistrict.com", headers=self.ua, cookies=cookies)
			if req.status_code==200:
				print("Successfully got site...")
			elif req.status_code==502:
				print("This site is actually down 90% of time")
			elif req.status_code==403:
				print("BANBANBANBAN")
			else:
				print("Life is hard")
		except Exception as e:
			raise e
s=sucuriFirewall()

if __name__ == '__main__':
	s.mainf()