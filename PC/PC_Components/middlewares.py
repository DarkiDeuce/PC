from django.contrib.sessions.backends.db import SessionStore

class SessionPerRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = SessionStore(request.session.session_key)
        session.save()

        request.session = session

        # Передача управления следующему middleware  или обработчику запроса.
        response = self.get_response(request)

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