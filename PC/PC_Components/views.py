from django.shortcuts import render
from django.http import *
from .models import Motherboard, VideoCards, RAM, CPU, PowerUnit
from django.views import generic

class MotherboardListView(generic.ListView):
    template_name = 'catalog/motherboard_list.html'
    model = Motherboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = 'img/motherboard/'
        return context

class MotherboardDetailView(generic.DetailView):
    model = Motherboard

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