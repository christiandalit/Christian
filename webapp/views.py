from django.shortcuts import render, redirect
from .models import   *
from .forms import StudentForm
def index(request):

    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def AddStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Update')


    context = {'form':form}
    return render(request, 'pages/AddStudents.html',context)



def ManageStudent(request):
    students = Student.objects.all()
    return render(request, 'pages/ManageStudents.html' , {'students':students})


def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('Update')

    context = {'student': student}
    return render(request, 'pages/delete.html', context)


def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Update')

    context = {'form': form}
    return render(request, 'pages/AddStudents.html', context)
