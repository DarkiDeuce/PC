from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import Motherboard, VideoCards, RAM, CPU, PowerUnit, SSD
from django.views import generic
from .forms import VideoCardsForm, RAMForm, CPUForm, SSDForm, MotherboardForm, PowerUnitForm

class MotherboardListView(generic.ListView):
    model = Motherboard
    template_name = 'catalog/motherboard_list.html'

class MotherboardDetailView(generic.DetailView):
    model = Motherboard
    template_name = 'catalog/motherboard_detail.html'

class VideocardsListView(generic.ListView):
    model = VideoCards
    template_name = 'catalog/videocards_list.html'

class VideocardsDetailView(generic.DetailView):
    model = VideoCards
    template_name = 'catalog/videocards_detail.html'

class RAMListView(generic.ListView):
    model = RAM
    template_name = 'catalog/ram_list.html'

class RAMDetailView(generic.DetailView):
    model = RAM
    template_name = 'catalog/ram_detail.html'

class CPUListView(generic.ListView):
    model = CPU
    template_name = 'catalog/cpu_list.html'

class CPUDetailView(generic.DetailView):
    model = CPU
    template_name = 'catalog/cpu_detail.html'

class PowerUnitListView(generic.ListView):
    model = PowerUnit
    template_name = 'catalog/powerunit_list.html'

class PowerUnitDetailView(generic.DetailView):
    model = PowerUnit
    template_name = 'catalog/powerunit_detail.html'

class SSDListView(generic.ListView):
    model = SSD
    template_name = 'catalog/ssd_list.html'

class SSDDetailView(generic.DetailView):
    model = SSD
    template_name = 'catalog/ssd_detail.html'

class MotherboardSelection(generic.ListView):
    model = Motherboard
    template_name = 'constructor/motherboard_list.html'

def index(request):
    #Заменить запросы к базе на 404
    #Забить из БД только те значения, которы используются в шаблоне
    num_matherboard = Motherboard.objects.all().count()
    num_videcard = VideoCards.objects.all().count()
    num_ram = RAM.objects.all().count()
    num_cpu = CPU.objects.all().count()
    num_powerunit = PowerUnit.objects.all().count()
    num_ssd = SSD.objects.all().count


    return render(request, 'index.html', context={'num_matherboard': num_matherboard,
                                                  'num_videcard': num_videcard,
                                                  'num_ram': num_ram,
                                                  'num_cpu': num_cpu,
                                                  'num_powerunit': num_powerunit,
                                                  'num_ssd': num_ssd,}
                  )

def accessories(request):
    return render(request, 'catalog/accessories.html')

def constructor(request):
    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        motherboard = get_object_or_404(Motherboard, id=motherboard_id)

        return render(request, 'constructor/constructor.html', context={'motherboard': motherboard})

    return render(request, 'constructor/constructor.html')