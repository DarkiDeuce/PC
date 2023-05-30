from django.contrib import admin
from django.urls import path, re_path
from PC_Components import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    re_path(r'^accessories/motherboards/$', views.MotherboardListView.as_view(), name='motherboard'),
    re_path(r'^accessories/motherboard/(?P<pk>\d+)/$', views.MotherboardDetailView.as_view(), name='motherboard-detail'),
    re_path(r'^accessories/videocards/$', views.VideocardsListView.as_view(), name='videocard'),
    re_path(r'^accessories/videocard/(?P<pk>\d+)/$', views.VideocardsDetailView.as_view(), name='videocard-detail'),
]
