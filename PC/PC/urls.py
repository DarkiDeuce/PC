from django.contrib import admin
from django.urls import path, re_path
from PC_Components import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    path('constructor/', views.constructor, name='constructor'),
    re_path(r'^accessories/motherboards/$', views.MotherboardListView.as_view(), name='motherboard'),
    re_path(r'^accessories/motherboard/(?P<pk>\d+)/$', views.MotherboardDetailView.as_view(), name='motherboard-detail'),
    re_path(r'^accessories/videocards/$', views.VideocardsListView.as_view(), name='videocard'),
    re_path(r'^accessories/videocard/(?P<pk>\d+)/$', views.VideocardsDetailView.as_view(), name='videocard-detail'),
    re_path(r'^accessories/ram/$', views.RAMListView.as_view(), name='ram'),
    re_path(r'^accessories/ram/(?P<pk>\d+)/$', views.RAMDetailView.as_view(), name='ram-detail'),
    re_path(r'^accessories/cpu/$', views.CPUListView.as_view(), name='cpu'),
    re_path(r'^accessories/cpu/(?P<pk>\d+)/$', views.CPUDetailView.as_view(), name='cpu-detail'),
    re_path(r'^accessories/powerunit/$', views.PowerUnitListView.as_view(), name='powerunit'),
    re_path(r'^accessories/powerunit/(?P<pk>\d+)/$', views.PowerUnitDetailView.as_view(), name='powerunit-detail'),
    re_path(r'^accessories/ssd/$', views.SSDListView.as_view(), name='ssd'),
    re_path(r'^accessories/ssd/(?P<pk>\d+)/$', views.SSDDetailView.as_view(), name='ssd-detail'),
    re_path(r'^constructor/motherboard_selection/$', views.MotherboardSelection.as_view(), name='motherboard_selection'),
    re_path(r'^constructor/videocard_selection/$', views.VideocardSelection.as_view(), name='videocard_selection'),
    re_path(r'^constructor/ram_selection/$', views.RAMSelection.as_view(), name='ram_selection'),
    re_path(r'^constructor/cpu_selection/$', views.CPUSelection.as_view(), name='cpu_selection'),
    re_path(r'^constructor/power_unit_selection/$', views.PowerUnitSelection.as_view(), name='power_unit_selection'),
    re_path(r'^constructor/ssd_selection/$', views.SSDSelection.as_view(), name='ssd_selection'),
]
