import hashlib
import csv
import binascii
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    mydict = OrderedDict()
    mydict1 = OrderedDict()
    rows = []
    with open(input_file_name, mode='r') as input_file_name1:
            reader = csv.reader(input_file_name1)
            mydict1 = {rows[0]: rows[1] for rows in reader}
    with open(output_file_name, 'w', newline='') as output_file_name1:
        writer = csv.writer(output_file_name1, dialect='excel', delimiter=' ')
        for i in range(0, 10000):  # 0-10000 shavad
            #print(hashlib.sha256(str(i).encode()).hexdigest())
            row = (hashlib.sha256(str(i).encode()).hexdigest())
            writer.writerow([row])
            for x in row:
                mydict[row] = i
    with open(output_file_name, 'w', newline='') as output_file_name1:
            writer = csv.writer(output_file_name1, dialect='excel')
            for i in range(len(mydict1)):
                #print(len(mydict1))
                if ((list(mydict1.values())[i])) in (list(mydict.keys())):
                    #print(mydict.get(str((list(mydict1.values())[i]))))
                    #print(list(mydict1.keys())[i],',',mydict.get(str((list(mydict1.values())[i]))))
                    row = (list(mydict1.keys())[i], mydict.get(
                        str((list(mydict1.values())[i]))))
                    writer.writerow(row)

