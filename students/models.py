from __future__ import unicode_literals

from django.db import models
from courses.models import Course
from courses.serializers import CourseSerializer
import json

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=255, primary_key=True)
	enrolled_courses = models.ManyToManyField(Course)

	@property
	def courses(self):
		return [CourseSerializer(course).data for course in self.enrolled_courses.all()]