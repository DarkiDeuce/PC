from django.contrib.sessions.backends.db import SessionStore

class SessionPerRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = SessionStore(request.session.session_key)
        request.session = session

        response = self.get_response(request)

        session.save()

        return response


    # class SessionPerRequestMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         session = request.session
#         response = self.get_response(request)
#
#         request.session.modified = True
#
#         return response