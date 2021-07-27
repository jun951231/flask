import matplotlib.pyplot as plt
import random
import csv
from modu.template import ChangedTemperatureOnMyBirthday


def random_dice(count):
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(count)]
    return ls



def highest_temperature(month: str) -> []:
    birth = ChangedTemperatureOnMyBirthday()
    birth.read_data()
    arr = []
    # [print(i) for i in birth.data]
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' if i[0].split('-')[1] == month]
    return arr


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='r', label=f'{month} Month')
    plt.legend()
    plt.show()
    '''
    month_arr = []
    for i in birth.data:
        if i[-1] != '':
            if i[0].split('-')[1] == '08':
                aug.append(float(i[-1]))
            if i[0].split('-')[1] == '01':
                jan.append(float(i[-1]))    
                '''


if __name__ == '__main__':
    show_hist_about(highest_temperature('01'), month='01')