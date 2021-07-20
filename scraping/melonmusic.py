from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melonmusic(object):

    def __init__(self, url):
        self.url = url


    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='span', attrs={'class':'checkEllipsis'})
        print(f'List size is {len(ls)}')
        for i in ls:
            n_artists += 1
            print(str(n_artists) + "Rank")
            print("checkEllipsis : " + i.find('a').text)



def main():
    Melonmusic(f'https://www.melon.com/chart/index.htm').scrap()



if __name__ == '__main__':
    main()
