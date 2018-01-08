from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from students.models import Student

# Create your views here.
def student(request):
	name = request.GET.get('name', request.POST.get('name', None))
	if not name:
		return HttpResponse({'error': 'name required'}, status=400)
	student = Student.objects.filter(name=name)
	if request.method == "GET":
		if not student.exists():
			return HttpResponse(status=404)
		resp_data = {'courses': Student.objects.get(name=name).courses}
		status = 200
	elif request.method == "POST":
		student = Student.objects.get_or_create(name=name)
		course_id = request.POST.get('course_id')
		student.enrolled_courses.add(course_id)
		resp_data = {'courses': student.courses}
		status = 201
	else:
		resp_data = {'error': 'Unsupported operation: {0}'.format(request.method)}
		status = 400
	return JsonResponse(resp_data, status=status)