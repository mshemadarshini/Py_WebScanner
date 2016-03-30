# this would advice who register the domain name
# would reveal private information of the website
# this can be prevent when the domain purchaser buy the domain name privacy
# when buying the website, else all the information would appear here.

import os


def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results

# below is the sample way to run this code
# print(get_whois('thenewboston.com'))

