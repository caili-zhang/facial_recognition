# -*- coding: utf-8 -*-
from multiprocessing import Pool
import bs4 as bs
import  random
import  requests
import string

# 複数のサイトを同時にスクラルする
def random_starting_url():
    starting =''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url=''.join(['http://',starting,'.com'])

    return url

# build spider
def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link

def get_links(url):
    try:
        resp=requests.get(url)
        soup=bs.BeautifulSoup(resp.text,'lxml')
        body=soup.body
        links=[link.get('href') for link in body.find_all('a')]

        links=[handle_local_links(url,link) for link in links]
        links =[str(link.encode("ascii")) for link in links]
        return links
    except TypeError as e:
        print(e)
        print('Got TypeError')
        return []
    except IndexError as e:
        print(e)
        print('Got IndexError')
        return []
    except AttributeError as e:
        print(e)
        print('Got AttributeError')
        return []
    except Exception as e:
        print(str(e))
        print('Other exception ')
        return []

def main():
    howmany =100
    p=Pool(processes=howmany)
    parse_us = [random_starting_url() for _ in range(howmany)]

    # data is a list of list
    data=p.map(get_links,[link for link in parse_us])
    print(data)
    data=[url for url_list in data for url in url_list]# data => url_list => url

    p.close()

    with open('url.txt', 'w') as f:
        f.write(str(data))


if __name__=='__main__':
    main()