from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse,render
from django.http import JsonResponse

class RequestHeaderMixin(MiddlewareMixin):
    USER_AGENT = "HTTP_USER_AGENT"
    #私人爬虫
    black_word = ["python","scrapy","java"]
    #g各家搜索公司爬虫
    spider_list = ["Baiduspider","Googlebot","360Spider","sogou spider","Sosospider"]
    spider = "spider"
    def process_request(self,request):
        request_header = request.META
        req_method = request_header.get("REQUEST_METHOD", "")
        context = {}
        if req_method:
            if req_method.lower() == "put":
                context["error_message"] = "访问拒绝！"
                context["error_code"] = "0002"
                return JsonResponse(context)


        if self.USER_AGENT not in request_header:
            context["error_code"] = "0001"
            context["error_message"] = "访问拒绝！"
            return JsonResponse(context)
        else:
            user_agent = request_header.get("HTTP_USER_AGENT")
            is_spider = [black for black in self.black_word if black in user_agent]
            if len(is_spider) > 0:
                context["error_code"] = "0003"
                context["error_message"] = "访问被拒绝,请稍后尝试,！"
                return JsonResponse(context)