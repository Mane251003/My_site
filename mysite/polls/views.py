from django.shortcuts import render,get_object_or_404, redirect
from .models import Course

from django.http import HttpResponse

def course_list(request):
    courses=Course.objects.all()
    return render(request, "polls/course_list.html", {"courses": courses})

def course_detail(request, course_id):
    course=get_object_or_404(Course, pk=course_id)
    return render(request,"polls/course_detail.html", {"course": course})

def rate_course(request, course_id):
    course=get_object_or_404(Course, pk=course_id)

    if request.method=="Post":
        new_rating=float(request.Post.get('rating'))
        course.update_rating(new_rating)
        course.count+=1
        course.save()
        return redirect('course_detail', course_id=course_id)
    
    return render(request, 'polls/rate_course.html', {'course':course})




