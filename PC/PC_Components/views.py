from django.shortcuts import render
from django.http import *
from .models import Motherboard, VideoCards, RAM, CPU, PowerUnit
from django.views import generic

class MotherboardListView(generic.ListView):
    template_name = 'catalog/motherboard_list.html'
    model = Motherboard

class MotherboardDetailView(generic.DetailView):
    model = Motherboard
    template_name = 'catalog/motherboard_detail.html'

class VideocardsListView(generic.ListView):
    template_name = 'catalog/videocards_list.html'
    model = VideoCards

class VideocardsDetailView(generic.DetailView):
    model = VideoCards
    template_name = 'catalog/videocards_detail.html'

def index(request):
    num_matherboard = Motherboard.objects.all().count()
    num_videcard = VideoCards.objects.all().count()
    num_ram = RAM.objects.all().count()
    num_cpu = CPU.objects.all().count()
    num_powerunit = PowerUnit.objects.all().count()


    return render(request, 'index.html', context={'num_matherboard': num_matherboard,
                                                  'num_videcard': num_videcard,
                                                  'num_ram': num_ram,
                                                  'num_cpu': num_cpu,
                                                  'num_powerunit': num_powerunit,}
                  )

def accessories(request):
    return render(request, 'catalog/accessories.html')