from django.shortcuts import render, resolve_url, redirect
from .models import Student
# Create your views here.


def index(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'workshop19/index.html', context)


def detail(request, id):
    context = {
        'student': Student.objects.get(id=id)
    }
    return render(request, 'workshop19/detail.html', context)


def new(request):
    if request.method == 'GET':
        return render(request, 'workshop19/new.html')
    else:
        data = request.POST
        student = Student()
        student.name = data.get('name')
        student.email = data.get('email')
        student.birthday = data.get('birthday')
        student.age = data.get('age')
        student.save()
        return redirect(resolve_url('workshop19:student_detail', id=student.id))


def update(request):
    if request.method == 'GET':
        student = Student.objects.get(id=request.GET.get('id'))
        print(str(student.birthday))
        student.birthday = student.birthday.strftime('%Y-%m-%d')
        context = {
            'student': student
        }
        return render(request, 'workshop19/update.html', context)
    else:
        data = request.POST
        student = Student.objects.get(id=data.get('id'))
        student.name = data.get('name')
        student.email = data.get('email')
        student.birthday = data.get('birthday')
        student.age = data.get('age')
        student.save()
        return redirect(resolve_url('workshop19:student_detail', id=student.id))


def delete(request):
    if request.method == 'GET':
        return redirect(resolve_url('workshop19:student_index'))
    else:
        student = Student.objects.get(id=request.POST.get('id'))
        student.delete()
        return redirect(resolve_url('workshop19:student_index'))
