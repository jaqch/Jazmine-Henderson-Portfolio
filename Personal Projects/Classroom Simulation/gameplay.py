import random
from unicodedata import name
from students import Student
from school_day import SchoolDay 

print("Welcome to MyClassroom Simulator!")
teacher_name = input("What should your students call you? ")
print('Nice to meet you '+teacher_name+'!')
print('Time to get to know your students!')

#presets; this can be changed when additional customization options are supported (random, custom)
game_mode = 'classic' 
roster =  {'jaylen':[14, 0.1, 0.4, 0.8],
             'jayson':[9, 0.35, 0.4, 0.6],
             'marcus':[7, 0.45, 0.9, 0.2],
             'derrick':[6, 0.2, 0.1, 0.2],
             'al':[12, 0.5, 0.6, 0.7]}

def create_classroom_roster(game_mode='classic'):
    classroom_roster = []
    if game_mode != 'classic':
        pass #to be supported in future versions; rewrite roster dict with user settings or random stats
    else:
        for stud in roster.keys():
            classroom_roster.append(Student(stud,roster[stud][0],roster[stud][1],roster[stud][2],roster[stud][3]))
    return classroom_roster

def initialize_school_day(roster,length=80,rounds=10):
    first_school_day = SchoolDay(roster,length,rounds)
    return first_school_day

def help_student(student):
    student.set_status('helped')
    return student

def take_action(action,school_day):
    
        if action.lower() == 'help student':
            selected_student = input('Type the name of the student you would like to help   ')
            while selected_student.lower() not in roster.keys():
                selected_student = input('Please select a student.   ')
            for i in range(len(school_day.class_roster)):
                if school_day.class_roster[i].name == selected_student:
                    student_object = school_day.class_roster[i] 
                    school_day.class_roster[i] = help_student(student_object)
            return school_day
        
        elif action.lower() == 'teach class':
            updated_roster = []
            for student in school_day.class_roster:
                updated_student = help_student(student)
                updated_roster.append(updated_student)
            school_day.class_roster = updated_roster
        
        elif action.lower() == 'do nothing':
            return school_day
        
        elif action.lower() == 'exit':
            school_day.set_is_over()
        
        else:
            print('Sorry that is not a valid input.')
            next_action = input('Please select another action: help student, teach class, do nothing   ')
            return take_action(next_action, school_day)
        return school_day

def teaching_round(school_day):
    if school_day.is_over:
        for student in school_day.class_roster: 
            print(student.name+': '+str(student.get_progress()))
        print('Thanks for playing, '+teacher_name+'!')
    else:
        for student in school_day.class_roster:
            if student.get_status().lower() == 'focused':
                student.set_status('Working')
            elif student.get_status().lower() == 'helped':
                student.set_status('Focused')
            elif student.get_status().lower() == 'question':
                student.epiphany()
            else: student.question()
        school_day.get_time_remaining()
        school_day.display_all_students()
        action = input('Please select one of the following options: help student, teach class, do nothing, exit   ')
        updated_school_day = take_action(action,school_day)
        for student in updated_school_day.class_roster:
            current_status = student.get_status()
            student.update_progress(current_status)
        updated_school_day.set_time_remaining()
        return teaching_round(updated_school_day)

# Begin game
classroom = create_classroom_roster()
for student in classroom:
    print('Name: '+student.get_name())
    print('Base Progress Rate: '+str(student.get_base_rate()))

start_school = initialize_school_day(classroom)

teaching_round(start_school)
            
    
