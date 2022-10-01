from django.shortcuts import render
from .tasks import generate_file
# Create your views here.

def index(request):
    file_name ='akshay'
    rows = 10
    task = generate_file.delay(file_name,rows)
    print("Task ID:",task)
    return render(request,'example/index.html')