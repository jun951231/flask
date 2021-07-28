import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib import font_manager, rc
rc('font', family = font_manager.FontProperties(fname='C:\Windows\Fonts\Arial.ttf').get_name())

class Population(object):

    data: [] = list()
    home: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        self.read_data()
        # print([i for i in self.data])
        arr = []
        [arr.append(j) for i in self.data if dong in i[0] for j in i[3:]]
        print('*' * 100)
        print([i for i in arr])
        return arr
    '''
    def pop_comparison(self, dong: str) -> []:
        self.read_data()
        np = []
        dong = input('신도림동 :')
        [np.array(i[3:], dtype=int)/int(i[2]) for i in self.data if dong in i[0] for i in self.data]
        print([i for i in dong])
        return np
        '''
    def show_plot(self, arr: [], dong: str):
        self.read_data()
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()



if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.show_plot(pop.pop_per_dong('신도림동'))