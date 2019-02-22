import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class TimeItMiddleware(MiddlewareMixin):
    # """新版"""
    # def __call__(self, request):
    #     response = None
    #     self.start_time = time.time()
    #     if hasattr(self, 'process_request'):
    #         response = self.process_request(request)
    #     response = response or self.get_response(request)
    #     if hasattr(self, 'process_response'):
    #         response = self.process_response(request, response)
    #     costed = time.time() - self.start_time
    #     print('request to response cose:{:.2f}s'.format(costed))
    #     return response


    """旧版"""
    def process_request(self,request):
        self.start_time = time.time()
        return

    def process_view(self,request,func,*args,**kwargs):
        if request.path !=reverse('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view:{:.2f}s'.format(costed))
        return response

    def procss_exception(self,request,exception):
        pass

    def process_template_response(self,request,response):
        return response

    def process_response(self,request,response):
        costed = time.time() - self.start_time
        print('request to response cose:{:.2f}s'.format(costed))
        return response
