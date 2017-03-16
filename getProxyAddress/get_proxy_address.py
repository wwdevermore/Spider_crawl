import urllib2
'''
get_proxy_address from localhost:5000/get class
api created by flask
wwd

'''
class get_proxy_address:

    def get(self):
        proxy_url = urllib2.urlopen('http://127.0.0.1:5000/get')
        address = proxy_url.read()
        proxy = {'http': address}

        return proxy





