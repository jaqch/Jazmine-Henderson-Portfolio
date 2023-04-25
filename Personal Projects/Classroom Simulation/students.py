#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 02:51:01 2020

@author: jhenderson
"""

import random
from unicodedata import name

#  teacher simulator start

# base student learn rate; sample dict
# key = student name ; value = [base rate, block rate, distraction rate, epipheny rate]

# statuses = 'Working', 'Question', 'Distracting', 'Distracted', 'Helping', 'Focused' 

class Student:
    def __init__(self,name,base_rate,block_rate,distraction_rate,ephiphany_rate):
        self.name = name
        self.base_rate = base_rate
        self.block_rate = block_rate
        self.base_distraction_rate = distraction_rate
        self.ephipany_rate = ephiphany_rate
        self.working_rate = base_rate
        self.status = 'Working'
        self.progress = 0
        self.rounds_with_question = 0
        self.rounds_distracted = 0
        self.status_locked = False
        self.is_distracted = False
        self.has_question = False
        self.neighbors_distracted = False
        self.num_neighbors_distracted = 0
        self.finished_working = False
    
    def question(self):
        q = random.random()
        if q <= self.block_rate:
            self.set_status('Question')
        
    
    # def distracting(self):
    #     distraction_chance = self.base_distraction_rate + (self.rounds_with_question*0.075)
    #     dis = random.random()
    #     if dis <= distraction_chance:
    #         self.set_status('Distracting')
        

    # def distracted(self):
    #     distraction_chance = self.base_distraction_rate + (self.rounds_with_question*0.075) + (self.num_neighbors_distracted*0.15)
    #     dis = random.random()
    #     if dis <= distraction_chance:
    #         self.set_status('Distracted')
    #     return self

    def epiphany(self):
        ep = random.random()
        if ep <= self.ephipany_rate:
            self.set_status('Working')
        

    def get_progress(self):
        return self.progress

    def update_progress(self,status):
        if status.lower() == 'working':
            self.working_rate == self.base_rate
        elif status.lower() == 'helped':
            self.working_rate == round(self.base_rate / 2)
        elif status.lower() == 'focused':
            self.working_rate == round(self.base_rate*1.5)
        self.progress += self.working_rate
        
    def set_status(self,new_status):
        self.status = new_status
        
    def get_status(self):
        return self.status
    
    def get_name(self):
        return self.name
    
    def get_base_rate(self):
        return self.base_rate
        
