# this are the main file which retrieve information form other file

from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robo import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F',ip_address)
    robo = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robo, whois)


def create_report(name, full_url, domain_name, nmap, robo, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url,txt', full_url)
    write_file(project_dir + '/domain_name,txt', domain_name)
    write_file(project_dir + '/nmap,txt', nmap)
    write_file(project_dir + '/robo,txt', robo)
    write_file(project_dir + '/whois,txt', whois)

# enter the "foldername" and the "website name" into the both parameters per below
# gather_info('thenewboston', 'https://www.thenewboston.com/')


# https://www.youtube.com/watch?v=LqIkt78qBSk#t=713.45893








