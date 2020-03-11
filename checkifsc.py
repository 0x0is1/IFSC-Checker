# coding: utf-8
import requests
from bs4 import BeautifulSoup
import os

def banner():
    a = '''
        \033[1;35;40m
    
    ╻┏━╸┏━┓┏━╸   ┏━╸╻ ╻┏━╸┏━╸╻┏ ┏━╸┏━┓
    ┃┣╸ ┗━┓┃     ┃  ┣━┫┣╸ ┃  ┣┻┓┣╸ ┣┳┛
    ╹╹  ┗━┛┗━╸   ┗━╸╹ ╹┗━╸┗━╸╹ ╹┗━╸╹┗╸
  <Copyright: 0x0is1 (github.com/0x0is1)>
    \033[32m
    '''
    print(a)

def check():
    if requests.get('https://example.com').ok:
        print('You are Online')
    else:
        print("You're Offline")
        exit()

def mainfun():
    ifsc = input('Enter IFSC Code:')
    url = 'https://ifsc.bankifsccode.com/' + ifsc
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    result = soup.find_all("div", {"class": "text"})[2]
    address = result.find('b', text='Address:')
    print('')
    print('Address: ' + address.next_sibling)
    link = result.find_all('a')
    print('Bank: ' + link[0].get('href').split('/')[3].strip())
    print('State: ' + link[1].get('href').split('/')[4].strip())
    print('District: ' + link[2].get('href').split('/')[5].strip())
    print('Branch: ' + link[4].get('href').split('/')[6].strip())
    contact = result.find('b',text='Contact:')
    print('Contact: ' + contact.next_sibling)
    print('IFSC Code: ' + ifsc)
    print('Branch Code: ' + ifsc[-6:])
    micr = result.find('b',text='MICR Code:')
    try:
        print('MICR Code: ' + link[6].get('href').split('/')[3].strip())
    except:
        print('MICR Code: ' + micr.next_sibling)

os.system('clear')
banner()
check()
print('')
try:
    mainfun()
except:
    print('Bank may not be internationaly known!')

