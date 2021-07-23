import matplotlib.pyplot as plt
from common.menu import print_menu

"""
list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
"""
def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40], color='skyblue', linestyle='--', label='Mr.bluesky')
    plt.plot([40, 30, 20, 10], 'pink', ls=':', label='pinkGay')
    plt.legend()
    plt.show()
"""
첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
"""
def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


def plot_marker():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'plot_show', 'plot_two_list_show', 'plot_marker',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        # 0-exit, 1-Bugs (input URL), 2-Melon (input URL), 3-output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_marker()