from django.shortcuts import render,get_object_or_404
from .models import Teacher
from Course.models import Courses
from django.contrib.auth.decorators import login_required

@login_required
def teacher_view(request, branch):
    # ✅ Get distinct course names only (not whole objects)
    courses = Courses.objects.values_list('course_name', flat=True).distinct()

    # ✅ Handle filtering safely
    if branch.lower() == "all":
        teachers = Teacher.objects.all()
    else:
        teachers = Teacher.objects.filter(branch__course_name__iexact=branch)

    # ✅ Convert queryset to a sorted list (removes duplicates manually if needed)
    unique_courses = sorted(set(courses))

    return render(request, 'all.html', {
        'teachers': teachers,
        'courses': unique_courses,   # Use the unique cleaned list
        'selected_branch': branch
    })



@login_required
def teacher_detail_view(request,pk):
    teacher=get_object_or_404(Teacher,pk=pk)
    return render(request,'teacher_detail.html',{'teacher':teacher})



