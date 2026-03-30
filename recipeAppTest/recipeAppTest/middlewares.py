import time
from django.utils.deprecation import MiddlewareMixin

def measure_time_execution(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request, *args, **kwargs)  # executes middleware or view
        end_time = time.time()
        print(f"Total time for execution with function is {end_time - start_time}")
        return response

    return middleware


# class MeasureTimeExecution:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request, *args, **kwargs):
#         start_time = time.time()
#         response = self.get_response(request, *args, **kwargs)  # executes middleware or view
#         end_time = time.time()
#         print(f"Total time for execution with Class is {end_time - start_time}")
#         return response

class MeasureTimeExecution(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_view(self, request, view, *args, **kwargs):
        print("it is executing right before the view")

    def process_template_response(self, request, response):
        print("it is executing after the view and before template rendering")
        return response

    def process_exception(self, request, exception):
        print(f"The exeptiond that happend was {exception}")

    def process_response(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f"Total time for execution with MiddlewareMixin is {total_time}")
        return response