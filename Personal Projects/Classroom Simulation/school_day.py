#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 02:51:01 2020

@author: jhenderson
"""

import random
from unicodedata import name
from students import Student

#  teacher simulator start

# base student learn rate
# key = student name ; value = [base rate, block rate, distraction rate, epipheny rate]

# base_stats = {'jaylen':[5, 0.8, 0.4, 0.8],
#             'jayson':[9, 0.9, 0.4, 0.6],
#             'marcus':[1, 0.45, 0.9, 0.2],
#             'peyton':[7, 0.2, 0.1, 0.2],
#             'al':[4, 0.1, 0.6, 0.7]}


class SchoolDay:
    def __init__(self, class_roster, total_time, rounds):
        self.class_roster = class_roster 
        self.total_time = total_time
        self.rounds = rounds
        self.round_length = total_time / rounds
        self.time_remaining = total_time
        self.is_over = False

    def set_time_remaining(self):
        self.time_remaining -= float(self.round_length)
        self.rounds -= 1
        if self.rounds == 0: self.set_is_over()

    def display_all_students(self):
        for student in self.class_roster:
            print('Name: '+student.get_name()+'  Status: '+student.get_status()+'  Progress: '+str(student.get_progress()))
        return self
    
    def get_time_remaining(self):
        print('Time remaining: '+str(self.time_remaining)+ '   Rounds: '+str(self.rounds))
    
    def set_is_over(self):
        self.is_over = True
    
    def end_day(self):
        self.set_is_over() # set is_over to true and display final student progress
        for student in self.class_roster: 
            print(student.name()+': '+student.get_progress())
        print('Thanks for playing!')
        return self
