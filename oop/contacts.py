'''
name, phone, email, address
'''


class Contacts(object):
    def __init__(self, name, phone, email, address):#생성자
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):#메소드
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact() -> object:#함수
    return Contacts(input('name'), input('phone'), input('email'), input('address'))


def get_contact(ls):
    for i in ls:
        i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):
        if name == j.name:
            del ls[i]


def print_menu(ls) -> int:
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))



def main():
    ls = []
    while 1:
        menu = print_menu(['Exit', 'Add', 'Print', 'Delete'])
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contact()
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break


if __name__ == '__main__':
    main()
    # ls = ['0-Exit', '1-Add', '2-Print', '3-Delete']
    # ls2 = ['Exit', 'Add', 'Print', 'Delete']
    # print(print_menu(ls2))

'''
    while 1:
        if menu == '0':
            return
        if menu == '1':
            contacts.append(Contacts(input('set: ')))
        elif menu == '2':
            contacts.append(Contacts(input('get: ')))
        elif menu == '3':
            contacts.append(Contacts(input('del: ')))
'''