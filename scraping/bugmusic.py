from bs4 import BeautifulSoup
from urllib.request import urlopen
"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.

"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""



class Bugmusic(object):

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='p', attrs={'class':'artist'})
        print(f'List size is {len(ls)}')
        for i in ls:
            n_artists += 1
            print(str(n_artists) + "Rank")
            print("Artist : " + i.find('a').text)
        print("*"*100)



def main():
    # 20210720
    # 16
    Bugmusic('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210720&charthour=16').scrap()



if __name__ == '__main__':
    main()


