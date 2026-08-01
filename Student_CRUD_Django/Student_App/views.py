from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from .models import Student
from .froms import StudentForm

# Create your views here.

## Get all students and render them in the index.html template
## http://127.0.0.1:8000/
@login_required
def get_student(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})



## Create a new student using the first method (manual form handling)
## http://127.0.0.1:8000/create_type1/
@login_required
def create_student_type1(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        testscore = request.POST.get('testscore')

        student = Student(firstname=firstname, lastname=lastname, age=age, testscore=testscore)
        if firstname and lastname and age and testscore:
            student.save()
        return redirect('/')

    return render(request, 'students/create_type1.html')

## Create a new student using the second method (Django forms)
## http://127.0.0.1:8000/create_type2/
@login_required 
def create_student_type2(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'students/create_type2.html', {'form': form})




## Delete a student by ID and redirect to the index page
## http://127.0.0.1:8000/delete/<student_id>/
@login_required
@permission_required('Student_App.delete_student')
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/')



## Update a student using the first method (manual form handling)
## http://127.0.0.1:8000/update_type1/<student_id>/
@login_required
def update_student_type1(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        testscore = request.POST.get('testscore')

        student.firstname = firstname
        student.lastname = lastname
        student.age = age
        student.testscore = testscore
        if firstname and lastname and age and testscore:
            student.save()
        return redirect('/')
    return render(request, 'students/update_type1.html', {'student': student})

## Update a student using the second method (Django forms)
## http://127.0.0.1:8000/update_type2/<student_id>/
@login_required
def update_student_type2(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'students/update_type2.html', {'form': form})



## Logout the user and redirect to the login page
## http://127.0.0.1:8000/logout/
def logout_user(request):
    auth_logout(request)
    return redirect('login')
