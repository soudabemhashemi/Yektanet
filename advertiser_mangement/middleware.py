class sampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
  

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # def process_template_response(self, _, response):
    #     ip = response.request["META"]
    #     return ip
