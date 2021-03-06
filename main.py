from bs4 import BeautifulSoup
import os
import urllib2
import time
import re
import sys

def notify(message, url):

    exString = 'terminal-notifier -message "%s" -open "%s" -sound "default" -appIcon $(pwd)/oatmeal.png' % (message, url)
    os.system(exString)

if __name__ == '__main__':

    with open("cName") as f:
        currentName = f.readline()

    while True:

        try:
            oatmeal = urllib2.urlopen("http://theoatmeal.com/comics").read()
            soup = BeautifulSoup(oatmeal, 'html.parser')

            link = soup.find_all("a", href=re.compile("^/comics/"), recursive=True)[0]

            if link['href'][8:] != currentName:
                u = "http://theoatmeal.com/comics/" + link["href"][8:]
                notify("NEW COMIC", u)
                currentName = link["href"][8:]

                with open("cName", "w+") as f:
                    f.write(currentName)
        except urllib2.URLError as err: pass

        time.sleep(1200)
