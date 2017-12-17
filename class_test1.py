#!/usr/bin/env python

class Robot(object):
    population = 0

    def __init__(self,name,age,):
        self.name = name
        self.age = age
        print("{}初始化".format(self.name))
        Robot.population += 1

    def say_hello(self):
        print("hello,my name is {}".format(self.name))
        print("my age is {}".format(self.age))

    def die(self):
        print("{} is die".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} is the last one".format(self.name))
        elif Robot.population < 0:
            print("")


    @classmethod
    def how_many(cls):
        print("The Robot has {}".format(cls.population))


code1 = Robot("robot1",2)
code1.say_hello()
Robot.how_many()

code2 = Robot("robot2",2)
code2.say_hello()
Robot.how_many()

code1.die()
Robot.how_many()

code2.die()
Robot.how_many()

code2.die()
Robot.how_many()




