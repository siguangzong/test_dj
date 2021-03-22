from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class MiddleWare1(MiddlewareMixin):
    def process_request(self, request):
        # if request.META.get("REMOTE_ADDR") == "127.0.0.1":
        #     return HttpResponse("")
        print("middle_ware1.process_request")
        return HttpResponse("")

    def process_view(selfs, request, view_func, view_func_args, view_func_kwargs):
        print("middle_ware1.process_view")
        # return HttpResponse("middle_ware1.process_view")

    def process_exception(self, request, exception):
        print("middleware1.process_exception")

    def process_response(self, request, response):
        print("middle_ware1.process_response")
        return response


class MiddleWare2(MiddlewareMixin):

    def process_request(self, request):
        print("middle_ware2.process_request")

    def process_view(selfs, request, view_func, view_func_args, view_func_kwargs):
        print("middle_ware2.process_view")
        # return HttpResponse("middle_ware2.process_view")

    def process_exception(self, request, exception):
        print("middleware2.process_exception")

    def process_response(self, request, response):
        print("middle_ware2.process_response")
        return response
