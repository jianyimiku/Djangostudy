def studentsinfo(request):
	stus = Students.objects.all()
	list = []
	for stu in stus:
		list.append([stu.name])
	return JsonResponse({"data":list})