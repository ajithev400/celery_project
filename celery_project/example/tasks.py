from celery import shared_task
from time import sleep
import csv
import os

path = 'files/csv/'

@shared_task(bind=True)
def generate_file(self,file_name,rows):
    print("Rows:",rows)
    sleep(1)
    file_dict = ['here is the Random data']
    file_name = file_name+'.csv'
    csv_file_name = os.path.join(path+file_name)

    for i in range(int(rows)):
        with open(csv_file_name,'a',newline='') as csv_file:
            print(file_dict)
            writer = csv.writer(csv_file)            
            writer.writerow(file_dict)
        

    return file_name+' Has been generated'
