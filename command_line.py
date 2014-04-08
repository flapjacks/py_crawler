'''
Created on Jan 11, 2013

@author: mwbarry
'''

import urllib.request
from urllib.error import URLError
from html.parser import HTMLParser

links = ''

def get_page(url):
            

    #make the request
    req = urllib.request.Request(url)
    the_page = urllib.request.urlopen(req)
    
    #get the results of the request
    try:
        #read the page
        page = the_page.read()
        print(page)
        #parse the page
        parser = MyHTMLParser(strict=False)
        parser.feed(page.decode('UTF-8'))
        
    #except error
    except URLError as e:
        #if error has a reason (thus is url error) print the reason
        if hasattr(e, 'reason'):
            print(e.reason)
        #if error has a code (thus is html error) print the code and the error
        if hasattr(e, 'code'):
            print(e.code)
            print(e.read())
    
    return links

#this will be used to parse html and print out what we want
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global links
        if tag == 'a':
            # get all attrs of anchor tag
            #print('Start tag:', tag)
            #for item in range(len(attrs)):
            #    print(tag + ' has attribute: ' + attrs[item][0] + '=\'' + attrs[item][1] + '\'')
            #    links += tag + ' has attribute: ' + attrs[item][0] + '=\'' + attrs[item][1] + '\'\n'
            
            # get only hrefs
            for item in range(len(attrs)):
                for href in range(len(attrs[item])):
                    if attrs[item][href] == 'href':
                        print(attrs[item][0] + '=\'' + attrs[item][1] + '\'')
                        links += attrs[item][0] + '=\'' + attrs[item][1] + '\'\n'

if __name__ == '__main__':
    get_page('http://www.xkcd.com')
    
    