# to scan robot.text file
import urllib.request
import io


def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request.urlopen(path + "robot.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

# below is the sample ways to run this code
# print(get_robots_txt('http://www.reddit.com/'))

