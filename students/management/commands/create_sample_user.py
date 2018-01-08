from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from courses.models import Course
from courses.serializers import CourseSerializer
from students.models import Student

COURSE_DATA_DIR = settings.BASE_DIR + "/LearningApp/course_data/"

class Command(BaseCommand):
    help = 'create John Doe and assign him to all classes'

    def handle(self, *args, **options):
        s, _ = Student.objects.get_or_create(name="John Doe")
        [s.enrolled_courses.add(course_id) for course_id in Course.objects.all().values_list('course_id', flat=True)]
