from functions import *

name_text = input("Input file name: ")
name_text = name_text +".txt"

try:
    file = open(name_text,"r")
except FileNotFoundError:
    print("File not found")
    exit(0)
exams = []
x = int(file.readline())
for i in range(x):
    exam = Exam()
    exam.input(file)
    a=0
    if valid_string(exam.get_name(), "name", i):
        a+=1
    if valid_digits(exam.get_age(), "age", i):
        a+=1
    if valid_digits(exam.get_group(), "group", i):
        a+=1
    if valid_string(exam.get_subject(), "subject", i):
        a+=1
    if valid_digits(exam.get_mark(), "mark", i):
        a+=1

    if a==5:
        exams.append(exam)



while True:
    print("Choose option: ")
    print("1.show list input")
    print("2.sort by name input")
    print("3.sort by age input")
    print("4.sort by price input ")
    print("5.find by name input")
    print("6.delete element input")
    print("7.insert element input")
    print("8.replace element input")
    a = (input())
    if a.isdigit():
        a=int(a)
    if a == 1:
        for i in show_list(exams):
            print(i)
    elif a == 2:
        for i in sort_name(exams):
            print(i)
    elif a == 3:
        for i in sort_age(exams):
            print(i)
    elif a == 4:
        for i in sort_price(exams):
            print(i)
    elif a == 5:
        word = " "
        while not search(exams, word):
            word = input("Input name: ")
            if not search(exams, word):
                print("Name not found, try again!!!")
            else:
                for i in search(exams, word):
                    print(i)
    elif a == 6:
        word = input("Input name: ")
        if not search(exams, word):
            print("Name not found, try again!!!")
        else:
            dell(exams, word)
            print("Element deleted")
    elif a == 7:
        obj = filling()
        insertt(exams, obj)
    elif a == 8:
        indexx=int(input("Input index: "))
        obj = filling()
        replacee(exams,indexx,obj)
        print("you input wrong number, please try again!!!")

