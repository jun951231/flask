'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.
'''

class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'\n[Person Info] \nName: {self.name} \nAge: {self.age} \nAddress: {self.address}\n')


def main():
    persons = []
    while 1:
        print('0- Exit 1-Add 2-Print')
        menu = input('Choose One Number')
        if menu == '1':
            persons.append(Person(input('name: '), input('age: '), input('address: ')))
        elif menu == '2':
            for i in persons:
                i.to_string()
        elif menu == '0':
            return



if __name__ == '__main__':
    main()

'''def addPerson(self, name, age, live):
        Person(name, age, live)
        
        person = Person(input())
        for i in ['Name', 'Age', 'Live']:
            person.addPerson(input(f'{i}: '))
'''
