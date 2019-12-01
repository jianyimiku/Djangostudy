# 自定义中间件例子
from django.utils.depreaction import MiddlewareMixin
class Mymiddle(MiddlewareMixin):
	#中间件必须继承MiddlewareMixin
	def process_request(self, request):
		print("get参数为": request.GET.get("a"))