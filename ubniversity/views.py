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
        return render(request, 'courses.html', context={'actcourses': courses})
    except:
        logger.exception('')


def shoot(request, name):
    r = None

    try:
        raise Exception('Log my raised ex')
    except Exception as e:
        r = str(e)
        logger.exception('')

    r = "name = {0} -  ex: {1}".format(name, r)
    return HttpResponse(r)
