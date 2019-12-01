import os
from django.conf import settings
def saveFile(request):
	if request.method == "POST":
		f = request.FILES['file']
		# 文件在服务器端的路径
		filepath = os.path.join(settings.MEDIA_ROOT, f.name)
		# 打开这个文件
		with open(filepath, 'wb') as fp:
			# 从文件里面读写到fp中去
			for info in f.chunks():
				fp.write(info)
		return HttpResponse("SUCCESS")
	else：
		return HttpResponse("FAIL")