from bs4 import BeautifulSoup
import pandas as pd
import requests

from common.menu import print_menu
from oop import contacts


class MusicRanking(object):
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text

    def get_html(self):
        print(f'Crawling HTML is {self.html}')

    def get_raking(self):
        soup = BeautifulSoup(self.html, 'html parser')
        music_info = []
        for name in self.class_name:
            music_info.append(soup.find_all(name=f'{self.tag}', attrs={'class': f'{name}'}))
            _ = 0
        for title,artist in zip(music_info):
            _ +=1
            print(f'{"*" * 50}\n{_} Rank\nTitle: {title.find("a").text}\nArtist: {artist.find("a").text}')
        self.class_name = []

    def insert_dict(self):
        # 방법 1
        soup = BeautifulSoup(self.html, 'html parser')
        music_info = []
        for name in self.class_name:
            music_info.append(soup.find_all(name=f'{self.tag}', attrs={'class': f'{name}'}))
        for title, artist in zip(music_info):
            self.titles.append(title.find("a").text)
            self.artists.append(artist.find("a").text)

        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j

        print(self.dict)

        ''''
        # 방법 2
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        # 방법 3
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]
        '''

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')


def main():
    # 20210720
    # 16
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output', 'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        # 0-exit, 1-Bugs (input URL), 2-Melon (input URL), 3-output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210720&charthour=16'
            mr.set_html()

        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = 'dayTime=2021072016'
            mr.set_html()

        elif menu == 3:
            mr.tag_name = 'p'
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_raking()

        elif menu == 4:
            site = int(input(f'1.벅스 2.멜론'))
            if site == 1:
                mr.tag = 'P'
                mr.class_name.append('title')
                mr.class_name.append('artist')
                mr.get_raking()
            elif site == 2:
                mr.tag = 'div'
                mr.class_name.append('ellipsis rank01')
                mr.class_name.append('ellipsis rank02')
                mr.get_raking()
        elif menu == 5:
            pass


if __name__ == '__main__':
    main()

