from ClassCar import *


def search(lst, name):
    def lam(i):
        for x in i.mydict:

            if i.mydict[x].find(name)!=-1:
                return True
        return False
    nlst = list(filter(lam, lst))
    return nlst



def show_list(lst):
    return lst

def sort_name(lst):
    return sorted(lst, key=lambda i: (i.name.upper(), i.name[0].islower()))

def sort_age(lst):
    return sorted(lst, key=lambda i: i.age)

def sort_price(lst):
    return sorted(lst, key=lambda i: i.group)


def dell(list, name):
    for i in list:
        if name == i.get_name():
            list.remove(i)

def insertt(list, obj):
    list.append(obj)

def replacee(lst,index, obj):
    lst[index]=obj


def decorator(func):
    def wrapper(var, line,i):
        if func(var, line,i):
            return True
    return wrapper

@decorator
def valid_string(var, line,i):
    k=0
    if not var.isalpha():
        while True:
            print("In line "+str(i+1)+" brand " + line + " entered incorrectly!")
            print(line + " can't be " + str(var))
            print("1.continue the program without this line input")
            print("2.finish the program input")
            d = int(input())
            if d == 1:
                break
            if d == 2:
                exit(0)
    else:
        k+=1
    return k

@decorator
def valid_digits(var, line, i):
    k=0
    if not var.isdigit():
        while True:
            print("In line "+str(i+1)+" brand " + line + " entered incorrectly!")
            print(line + " can't be " + str(var))
            print("1.continue the program without this line input")
            print("2.finish the program input")
            d = int(input())
            if d == 1:
                break
            if d == 2:
                exit(0)
    else:
        k+=1
    return k

def decorator2(func):
    def wrapper(var):
        func(var)
    return wrapper

@decorator2
def check_string(var):
    if var.isalpha():
        var = var
        return True

@decorator2
def check_digits(var):
    if var.isdigit():
        var = var
        return True

def filling():
    while True:
        obj_name = input("Input name: ")
        if obj_name.isalpha():
            obj_name = obj_name
            break
    while True:
        obj_age = (input("Input age: "))
        if obj_age.isdigit() and 1879 < int(obj_age) < 2020:
            obj_age = int(obj_age)
            break
    while True:
        obj_group = (input("Input car price: "))
        if obj_group.isdigit() and float(obj_group) > 0:
            obj_price = float(obj_group)
            break
    while True:
        obj_subject = input("Input subject: ")
        if obj_subject.isalpha():
            obj_color = obj_subject
            break
    while True:
        obj_mark = input("Input mark: ")
        if obj_mark.isdigit() and 20 < int(obj_mark) < 2000:
            obj_hp = int(obj_mark)
            break
    obj = Car(obj_name, obj_age, obj_group, obj_subject, obj_mark)
    return obj




