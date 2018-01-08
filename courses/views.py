from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer
from random import randint

class CourseAPIView(APIView):
    queryset = Course.objects.all()
    lookup_field = 'course_id'
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    def get(self, request, course_id=None):
    	if course_id:
    		print course_id
    		course = self.queryset.get(course_id=course_id)
    		serializer = CourseSerializer(course)
    	else:
    		course = self.queryset.all()
    		serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def put(self, request, course_id=None):
    	if not course_id:
    		return Response('no course_id supplied', status=400)
        course = self.queryset.get(course_id=course_id)
    	serializer = CourseSerializer(data=request.data.copy(), instance=course)
        serializer.is_valid(raise_exception=True)
        course = serializer.save()
    	return Response(serializer.data)

    def post(self, request):
        course_data = request.data.copy()
        print course_data
        if not course_data.get('course_id'):
            course_data['course_id'] = randint(10000, 99999)
        serializer = CourseSerializer(data=course_data)
        serializer.is_valid(raise_exception=True)
        course = serializer.save()
        return Response(serializer.data)

def index(request):
	return render(request, 'courses/index.html')
