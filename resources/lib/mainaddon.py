import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
def get_soup2(URL2):
    page = requests.get(URL2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
def get_soup3(URL3):
    page = requests.get(URL3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
def get_soup4(URL4):
    page = requests.get(URL4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
def get_soup5(URL5):
    page = requests.get(URL5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
def get_soup6(URL6):
    page = requests.get(URL6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
def get_soup7(URL7):
    page = requests.get(URL7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
def get_soup8(URL8):
    page = requests.get(URL8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup8))
    return soup8
def get_soup9(URL9):
    page = requests.get(URL9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup9))
    return soup9
def get_soup10(URL10):
    page = requests.get(URL10)
    soup10 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup10))
    return soup10
def get_soup11(URL11):
    page = requests.get(URL11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup11))
    return soup11
def get_soup12(URL12):
    page = requests.get(URL12)
    soup12 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup12))
    return soup12
def get_soup13(URL13):
    page = requests.get(URL13)
    soup13 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup13))
    return soup13

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast10(soup10):
    subjects = []
    for content in soup10.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast10(playable_podcast10):
    items = []
    for podcast in playable_podcast10:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast12(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast13(soup13):
    subjects = []
    for content in soup13.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast13(playable_podcast13):
    items = []
    for podcast in playable_podcast13:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
