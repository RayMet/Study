import os

class Person(list):
    def __init__(self,first_name,second_name,age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.append(first_name)
        self.append(second_name)
        self.append(age)
    @classmethod
    def get_user_input(self):
            while 1:
                try:
                    first_name = input('Enter first name: ')
                    second_name = input('Enter last name: ')
                    age = input('Enter age: ')
                    return self(first_name,second_name,age)
                except:
                    print('Invalid input!')
                    continue


    def getMenu():
            def clear(): os.system('cls') #on Windows System
            MenuChoice=''
            while MenuChoice!='0':
                print('0:Exit')
                print('1:Show all Persons')
                print('2:Add new Person')
                print('3:Find person by')
                MenuChoice = input()
                clear()
                if  MenuChoice == '1':
                    for obj in p1:
                        print( obj.first_name, obj.second_name, obj.age, sep =' ')
                if MenuChoice == '2':
                    p1.append(Person.get_user_input())
                if MenuChoice == '3':
                    print('1:Find by First name: ')
                    print('2:Find by Second name')
                    print('3:Find by Age')
                    MenuChoice = input()
                    if MenuChoice == '1':
                        data = input('Enter first name: ')
                        print([x for x in p1 if x[0]==data])
                    if MenuChoice == '2':
                        data = input('Enter first name: ')
                        print([x for x in p1 if x[1]==data])
                    if MenuChoice == '3':
                        data = input('Enter first name: ')
                        print([x for x in p1 if x[2]==int(data)])

p1=[]
p1.append(Person("Artem","Korniichuk",27))
p1.append(Person("Sergiy","Yaschuk",27))
Person.getMenu()

  