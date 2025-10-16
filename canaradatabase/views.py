from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
# Create your views here.
from .forms import AddStudent
def home(request):
    students=Student.objects.all()
    return render(request, 'index.html',{'students':students})



def student_view(request,pk):
    st=get_object_or_404(Student,pk=pk)

    return render(request,'student.html',{'st':st})





def add_student_view(request):
    if request.method=='POST':
        form=AddStudent(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'addstudent.html',{'form':form})
    
    else:
        form=AddStudent()
    
    return render(request,'addstudent.html',{'form':form})