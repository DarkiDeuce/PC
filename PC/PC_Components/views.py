from django.shortcuts import render
from .models import Motherboard, VideoCards, RAM, CPU, PowerUnit, SSD
from django.views import generic
from django.contrib.sessions.backends.db import SessionStore

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

class VideocardSelection(generic.ListView):
    model = VideoCards
    template_name = 'constructor/videocard_list.html'

class RAMSelection(generic.ListView):
    model = RAM
    template_name = 'constructor/ram_list.html'

class CPUSelection(generic.ListView):
    model = CPU
    template_name = 'constructor/cpu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        session = self.request.session
        cpu_socket = session.get('motherboard_socket')
        cpu_list = CPU.objects.filter(socket_cpu__socket_name=cpu_socket)

        context['cpu_list'] = cpu_list

        return context

class PowerUnitSelection(generic.ListView):
    model = PowerUnit
    template_name = 'constructor/powerunit_list.html'

class SSDSelection(generic.ListView):
    model = SSD
    template_name = 'constructor/ssd_list.html'

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
                                                  'num_ssd': num_ssd,
                                                  }
                  )

def accessories(request):
    return render(request, 'catalog/accessories.html')

def constructor(request):
    session = request.session

    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        videocards_id = request.POST.get('videocards_id')
        ram_id = request.POST.get('ram_id')
        cpu_id = request.POST.get('cpu_id')
        powerunit_id = request.POST.get('powerunit_id')
        ssd_id = request.POST.get('ssd_id')

        if motherboard_id is not None:
            session['motherboard_id'] = motherboard_id
            session['motherboard_socket'] = request.POST.get('motherboard_socket')

        if videocards_id is not None:
            session['videocards_id'] = videocards_id

        if ram_id is not None:
            session['ram_id'] = ram_id

        if cpu_id is not None:
            session['cpu_id'] = cpu_id

        if powerunit_id is not None:
            session['powerunit_id'] = powerunit_id

        if ssd_id is not None:
            session['ssd_id'] = ssd_id

    motherboard_id = session.get('motherboard_id')
    videocards_id = session.get('videocards_id')
    ram_id = session.get('ram_id')
    cpu_id = session.get('cpu_id')
    powerunit_id = session.get('powerunit_id')
    ssd_id = session.get('ssd_id')

    motherboard = Motherboard.objects.filter(id=motherboard_id)
    videocard = VideoCards.objects.filter(id=videocards_id)
    ram = RAM.objects.filter(id=ram_id)
    cpu = CPU.objects.filter(id=cpu_id)
    powerunit = PowerUnit.objects.filter(id=powerunit_id)
    ssd = SSD.objects.filter(id=ssd_id)

    return render(request, 'constructor/constructor.html', context={'motherboard': motherboard,
                                                                    'videocard': videocard,
                                                                    'ram': ram,
                                                                    'cpu': cpu,
                                                                    'powerunit': powerunit,
                                                                    'ssd': ssd,
                                                                    }
                  )