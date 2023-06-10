from django.contrib.sessions.backends.db import SessionStore

class SessionPerRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Создаем экземпляр класса сессии и сохраняем его в атрибуте request.session
        session = SessionStore(request.session.session_key)
        request.session = session

        response = self.get_response(request)

        # Сохраняем изменения в сессии
        session.save()

        return response