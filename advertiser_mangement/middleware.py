class getIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
  
    def getIP(request):
        x_firwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_firwarded_for:
            ip = x_firwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    # def __call__(self, request):
    #     response = request.META.get["IP"]
    #     return response

    # def process_template_response(self, _, response):
    #     ip = response.request["META"]
    #     return ip
