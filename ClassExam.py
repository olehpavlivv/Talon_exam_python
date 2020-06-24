
class Exam():
    def __init__(self, name=" ", age=None, group=None, subject=" ", mark=None):
        self.name = name
        self.age = age
        self.group = group
        self.subject = subject
        self.mark = mark
        self.mydict = dict()

    def __str__(self):
        return self.name + ", " + str(self.age) + ", " + str(self.group) + ", " + self.subject + ", " + str(self.mark)

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_group(self):
        return self.group
    def get_subject(self):
        return self.subject
    def get_mark(self):
        return self.mark


    def input(self,file):
        line = file.readline()
        line = line.split(' ')
        self.name = line[0]
        self.age = (line[1])
        self.group = (line[2])
        self.subject = line[3]
        self.mark = (line[4])
        self.mydict = {"name": self.name, "age": self.age, "group": self.group, "subject": self.subject, "mark": self.mark}



