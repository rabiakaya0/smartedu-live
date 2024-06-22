from django.shortcuts import render
from . models import Student

# Create your views here.
def students_list(request):
    students = Student.objects.all().order_by('-date')
    context = {
        'students': students
    }
    return render(request, 'students.html', context)
