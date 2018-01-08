from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from courses.models import Course
from courses.serializers import CourseSerializer

COURSE_DATA_DIR = settings.BASE_DIR + "/LearningApp/course_data/"

def parse_course_data(course_data):
    try:
        split_course_data = course_data.strip('\r\n').split(' ')
        d = {
            "course_id": int(split_course_data[0]),
            "name": " ".join(split_course_data[1:-2]),
            "length": int(split_course_data[-2]),
            "subject": split_course_data[-1]
        }
        return d
    except IndexError as e:
        print "Error Parsing course data: {0}".format(course_data)
    except Exception as e:
        print "Error with course data: {0}\n{1}".format(course_data, str(e))

class Command(BaseCommand):
    help = 'Ingest raw course data from file. defaults to courses.txt. specify a different file: --file_name <FILENAME>'

    def add_arguments(self, parser):
        parser.add_argument('--file_name', nargs='+', type=str)

    def handle(self, *args, **options):
        succ = 0
        fail = 0
        file_name = options.get('file_name')
        if not options.get('file_name'):
            print "No Filename Specified (--file_name <FILE_NAME>)"
            return

        with open(COURSE_DATA_DIR + file_name[0], 'r') as f:
            course_data = [parse_course_data(data) for data in f.readlines()]
            print "Ingesting {0} courses".format(len(course_data))
            for record_data in course_data:
                serializer = CourseSerializer(data=record_data)
                if serializer.is_valid():
                    # print serializer.validated_data
                    course = serializer.save()
                    succ += 1
                    print "course created: {0}".format(course.name)
                else:
                    fail += 1
                    print "Course data invalid: {0}".format(serializer.errors)
        print "Ingestion complete"
        print "{0} courses processed".format(str(succ))
        if fail:
            print "Failed to ingest {0} courses".format(str(fail))