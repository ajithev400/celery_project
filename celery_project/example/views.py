from django.shortcuts import render,redirect
from example.models import Celery_log
from .tasks import generate_file
from celery.result import AsyncResult

# Create your views here.

def index(request):
    
    if request.method == 'POST':       
        file_name = request.POST.get('file_name')
        rows = request.POST.get('count')

        
        task = generate_file.delay(file_name,rows)

        celery_result = AsyncResult(task.task_id)
        print("celery status:",celery_result.state)
        print("celery Result:",celery_result)
        
        celery_model = Celery_log.objects.create(
            file_name= file_name,
            count=rows,
            task_id = task.task_id,
            status = task.status
        )

        return redirect('success')
    return render(request,'example/main.html')



def success(request):
    return render(request,'example/success.html')