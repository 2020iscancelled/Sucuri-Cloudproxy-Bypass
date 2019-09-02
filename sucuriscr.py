import requests
from bs4 import BeautifulSoup as bs
import js2py
import base64, sys

VERSION="0.0.2"

BUG_REPORT="""
SOMETHING WENT WRONG
HAS THE SITE ACTUALLY A SUCURI WEB FIREWALL?
HAS SUCURI CHANGED SOMETHING? 
OPEN AN ISSUE ON GITHUB AND I WILL FIX IT
"""

class sucuriFirewall():

	def __init__(self):
		self.ua=header

	def show_ver():
		print(VERSION)

	def mainf(self, page, header,logging):
		try:
			self.page=page
			if logging==True:
				print("Requesting Home Page without cookies")
			req=requests.get(self.page, headers=header)
			if logging==True:
				print("Parsing Sucuri Script...")
			soup=bs(req.text, 'html.parser')
			script=(soup.find('script'))
			scr=script.text
			a=(scr.split("(r)")[0][:-1]+"r=r.replace('document.cookie','var cookie');")
			if logging==True:
				print("Extracted internal script")
			b=(js2py.eval_js(a))
			if logging==True:
				print("Getting cookies")
			sucuri_cloudproxy_cookie=js2py.eval_js(b.replace("location.","").replace("reload();",""))
			cookies={sucuri_cloudproxy_cookie.split("=")[0]:sucuri_cloudproxy_cookie.split("=")[1].replace(";path","")}
			return cookies
		except Exception as e:
			print(BUG_REPORT)
			sys.exit(1)
