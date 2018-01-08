from django.contrib import admin
from courses.models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'course_id', 'subject']
    list_display = ['course_id', 'name', 'subject', 'length']

admin.site.register(Course, CourseAdmin)