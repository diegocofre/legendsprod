import logging
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from .models import Organization, Teacher, Course, CourseDay, CourseClass

logger = logging.getLogger(__name__)


def index(request):
    try:
        courses = Course.objects.filter(active=True)
        teachers = Teacher.objects.filter(active=True)
        context = {'context': {'courses': courses}, 'teachers': teachers}
        return render(request, 'index.html', context)
    except:
        logger.exception(request)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def courses(request):
    try:
        courses = Course.objects.filter(active=True)
        context = {'context': {'courses': courses}}
        return render(request, 'courses.html', context)
    except:
        logger.exception(request)


def course_details(request, idcourse):
    try:
        cdetail = Course.objects.filter(
            id=idcourse
        ).filter(
            active=True
        )
        return render(request, 'course-details.html', context={'coursedetail': cdetail})
    except:
        logger.exception(request)


def teachers(request):
    try:
        teachers = Teacher.objects.filter(active=True)
        context = {'context': {'teachers': teachers}}
        return render(request, 'teachers.html', context)
    except:
        logger.exception(request)


def shoot(request, name):
    r = None

    try:
        raise Exception('Log my raised ex')
    except Exception as e:
        r = str(e)
        logger.exception('')

    r = "name = {0} -  ex: {1}".format(name, r)
    return HttpResponse(r)
