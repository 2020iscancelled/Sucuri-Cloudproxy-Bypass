#Simply call the sucuri scraper class and give it the page URL you want to scrape
# It will return you a cookie dict you can then add to your session

#EXAMPLE SCRIPT FOR AN INTEGRATION

from sucuriscr import sucuriFirewall
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

class Test():
	def __init__(self):
		self.ua=header
	def testing(self):
		print(sucuriFirewall.mainf(self,"https://footdistrict.com",self.ua,logging=False))
		sucuriFirewall.show_ver()

c=Test()
if __name__ == '__main__':
	c.testing()