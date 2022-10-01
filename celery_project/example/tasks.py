from celery import shared_task
from time import sleep
import csv
import os

path = 'files/csv/'

@shared_task(bind=True)
def generate_file(self,file_name,rows):
    print("Rows:",rows)
    file_dict = {}
    file_name = file_name+'.csv'
    csv_file_name = os.path.join(path+file_name)
    with open(csv_file_name,'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(rows):
            file_dict[i]= 'here is the Random data'

        writer.writerow(file_dict)

    return file_name+'Has been generated'


    # file_name = file_name+'.csv'
    # csvFileName = os.path.join(path+file_name)
    # print("CsvFileName: ",csvFileName)

    # with open(csvFileName,'a') as csv_file:
    #     csvWriter = csv.writer(csv_file, delimiter = ',')
    #     csvWriter.writerow('here is some random data')