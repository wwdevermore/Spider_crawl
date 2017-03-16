import urllib2
from getProxyAddress import get_proxy_address
from getUserAgent import get_user_agent


def get_html(url):
    address= get_proxy_address.get_proxy_address()
    agents=get_user_agent.get_user_agent()
    proxy=address.get()
    agent=agents.get()

    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    req=urllib2.Request(url)
    req.add_header('User-Agent',agent)
    urllib2.install_opener(opener)
    html=urllib2.urlopen(req)

    return html

url='http://httpbin.org/user-agent'
url2='http://httpbin.org/ip'
doc=get_html(url).read()
doc2=get_html(url2).read()
print doc2,doc




