from django.http import HttpResponse
from django.shortcuts import redirect, render

from crudoperations.forms import StudentForm
from crudoperations.models import Student

# Create your views here.
def create_student(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        city = request.POST.get('city')

        if name == '':
            context['name_error'] = "Name is required"

        if roll == '':
            context['roll_error'] = "Roll is required"

        if city == '':
            context['city_error'] = "City is required"

        if name and roll and city:
            student = Student(name=name, roll=roll, city=city)
            student.save()
            return redirect('retrieve')
        else:
            context['msg'] = "Please provide all the details"

    return render(request, 'crudoperations/create_student.html', context)

def retrieve_students(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'crudoperations/retrieve_students.html', context)

def student_details(request, id):
    student = Student.objects.get(id=id)

    context = {
        'student': student
    }

    return render(request, 'crudoperations/student_details.html', context)

def update_student(request, id):
    student = Student.objects.get(id=id)
    studentform = StudentForm(instance=student)

    context = {}

    if request.method == 'POST':
        studentform = StudentForm(request.POST, instance=student)
        if studentform.is_valid():
            studentform.save()
            return redirect('retrieve')

    context['form'] = studentform

    return render(request, 'crudoperations/update_student.html', context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    if student:
        student.delete()
        return redirect('retrieve')
    else:
        return HttpResponse("Student not found")

    return redirect('retrieve')