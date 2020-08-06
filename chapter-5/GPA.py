from statistics import mean
from collections import OrderedDict
import collections
import numpy as np
import csv
#input_file_name=('C://source.csv')
#output_file_name=('D://1.csv')

def calculate_averages(input_file_name, output_file_name):
    mydict = OrderedDict()
    rows=[]
    with open(input_file_name, mode='r') as input_file_name1:
        reader = csv.reader(input_file_name1)
        mydict = {rows[0]: rows[1:] for rows in reader}
    
    #print(mydict.values())
    mydict = dict((k, [int(s) for s in v]) for k,v in mydict.items())
    #print(mydict)
    with open(output_file_name, 'w', newline='') as output_file_name1:
        writer = csv.writer(output_file_name1,dialect='excel',delimiter =' ')
        for st,vals in mydict.items():
            row=("{},{}".format(st,mean(vals)))
            #writer.writerows([row])
            print(row)
            writer.writerows([i.strip().split(' ') for i in [row]])
            

#calculate_averages('C://source.csv','D://1.csv')    


def calculate_sorted_averages(input_file_name, output_file_name):
    mydict = OrderedDict()
    rows=[]
    with open(input_file_name, mode='r') as input_file_name11:
        reader = csv.reader(input_file_name11)
        mydict = {rows[0]: rows[1:] for rows in reader}
    #print(mydict.values())
    mydict = dict((k, [int(s) for s in v]) for k,v in mydict.items())
    #print(mydict) 
    with open(output_file_name, 'w', newline='') as output_file_name11:
        writer = csv.writer(output_file_name11,dialect='excel',delimiter =' ')    
        od = collections.OrderedDict(sorted(mydict.items()))
        student_averages = ((sum(scores) / len(scores), s) for s, scores in od.items())
        for average, student in sorted(student_averages, reverse=False):
            row=("{},{}".format(student,average))
            writer.writerows([i.strip().split(' ') for i in [row]])

    
#calculate_sorted_averages('C://source.csv','D://1.csv')    

def calculate_three_best(input_file_name, output_file_name):
    mydict = OrderedDict()
    rows=[]
    with open(input_file_name, mode='r') as input_file_name111:
        reader = csv.reader(input_file_name111)
        mydict = {rows[0]: rows[1:] for rows in reader}
    #print(mydict.values())
    mydict = dict((k, [int(s) for s in v]) for k,v in mydict.items())
    #print(mydict)
    with open(output_file_name, 'w', newline='') as output_file_name111:
        writer = csv.writer(output_file_name111,dialect='excel',delimiter =' ')
        od2 = collections.OrderedDict(sorted(mydict.items()))
        student_averages = ((sum(scores) / len(scores), s) for s, scores in od2.items())
        student_averages=sorted(student_averages, reverse=True)
        student_averages=student_averages[:3]
        for average, student in student_averages:
            row=("{},{}".format(student,average))
            writer.writerows([i.strip().split(' ') for i in [row]])
   
#calculate_three_best('C://source.csv','D://1.csv')

def calculate_three_worst(input_file_name, output_file_name):
    mydict = OrderedDict()
    rows=[]
    with open(input_file_name, mode='r') as input_file_name1111:
        reader = csv.reader(input_file_name1111)
        mydict = {rows[0]: rows[1:] for rows in reader}
    #print(mydict.values())
    mydict = dict((k, [int(s) for s in v]) for k,v in mydict.items())
    #print(mydict)
    with open(output_file_name, 'w', newline='') as output_file_name1111:
        writer = csv.writer(output_file_name1111,dialect='excel',delimiter =' ')
        student_averages = ((sum(scores) / len(scores), s) for s, scores in mydict.items())
        student_averages=sorted(student_averages, reverse=False)
        student_averages=student_averages[:3]
        for average, student in student_averages:
            row=("{}".format(average))    
            writer.writerows([i.strip().split(' ') for i in [row]])

#calculate_three_worst('C://source.csv','D://1.csv')

def calculate_average_of_averages(input_file_name, output_file_name):
    mydict = OrderedDict()
    rows=[]
    with open(input_file_name, mode='r') as input_file_name11111:
        reader = csv.reader(input_file_name11111)
        mydict = {rows[0]: rows[1:] for rows in reader}
    #print(mydict.values())
    mydict = dict((k, [int(s) for s in v]) for k,v in mydict.items())
    #print(mydict)
    with open(output_file_name, 'w', newline='') as output_file_name11111:
        writer = csv.writer(output_file_name11111,dialect='excel',delimiter =' ')
        student_averages = ((sum(scores) / len(scores), s) for s, scores in mydict.items())
        student_averages=sorted(student_averages, reverse=False)
        mydict2=OrderedDict()
        for i,j in student_averages:
            mydict2={j:i for i,j in student_averages}
        test=list(mydict2.values())
        row=(sum(test) / len(test) )
        writer.writerow([row])

#calculate_average_of_averages('C://source.csv','D://1.csv')