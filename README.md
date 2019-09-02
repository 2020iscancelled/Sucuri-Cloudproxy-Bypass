# Sucuri-Cloudproxy-Scraper
Simple python class to bypass Sucuri Firewall...
As first of all, install the needed packages with pip install requests , pip install bs4 , pip install js2py , pip install base64

Once done, clone in the repo and copy the sucuriscr.py file in the dir of your project... You can then call the sucuri-scraper function to obtain the cookies like in example.py or with the following function-call:


cookies=sucuriFirewall.mainf(self,"https://mypagewithsucuriprotection.com",self.ua) 
print(cookies) #will give you a cookie dict


self.ua is the given useragent or headers dictionary. Sucuri usually disallows various UAs the site access, so make sure to use a UA that is actually allowed to access the page.

The script will then return a sucuri cloudproxy cookie dict; you can use it in your following requests with
requests.get(url=mysite, headers=self.headers, cookies=returned_cookie_dict)

Also make sure to be always on the latest version, check your version by calling
sucuriFirewall.show_ver()
