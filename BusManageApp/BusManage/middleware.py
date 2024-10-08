class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Thêm Cache-Control header cho các file tĩnh
        if 'static' in request.path:
            response['Cache-Control'] = 'max-age=3600, public'

        return response