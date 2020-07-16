from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    image_url = models.CharField(max_length=256, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    image_url = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    bio = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=256, null=True)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    image_url = models.CharField(max_length=256, null=True)
    age_from = models.SmallIntegerField()
    age_to = models.SmallIntegerField()
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, to_field="id", null=True)
    time_zone = models.SmallIntegerField()
    max_attendants = models.SmallIntegerField()
    curr_attendants = models.SmallIntegerField(null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="courses", to_field="id")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=settings.CURRENCY_CHOICES)
    duration_minutes = models.IntegerField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class CourseDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="days", to_field="id")
    week_day = models.SmallIntegerField(choices=settings.WEEK_DAYS)
    from_time = models.TimeField()
    to_time = models.TimeField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return ("{} {}/{}").format(settings.WEEK_DAYS[self.week_day], self.from_time, self.to_time)


class CourseClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="classes", to_field="id")
    attendant = models.ForeignKey(User, on_delete=models.CASCADE,
                                  null=True, blank=True, to_field="id", related_name="classes")
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.course.name, self.datetime.tostring)
