from common.menu import print_menu
from modu.template.basic_plot import plot_show, plot_two_list_show, scatter
from modu.template.changed_temperature_on_my_birthday import ChangedTemperatureOnMyBirthday


if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'plot_show', 'plot_two_list_show', 'Scatter', 'Blank',
                           'ChangedTemperatureOnMyBirthday'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            scatter()
        elif menu == 4:
            pass
        elif menu == 5:
            ChangedTemperatureOnMyBirthday().processing()