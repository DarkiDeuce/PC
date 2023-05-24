from django.contrib import admin
from django.urls import path
from PC_Components import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home')
]
