from django.db import models
from django.urls import reverse

class VideoCards(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название видеокарты',
                            verbose_name='Название видеокарты')
    video_memory = models.CharField(max_length=10,
                                       help_text='Введите объём видеопамяти',
                                       verbose_name='Объём памяти')
    memoty_type = models.CharField(max_length=10,
                                   help_text='Введите тип видеопамяти',
                                   verbose_name='Тим видеопамяти')
    memory_frequency = models.CharField(max_length=10,
                                           help_text='Введите частоту памяти',
                                           verbose_name='Частота памяти')
    connection_type = models.CharField(max_length=50,
                                       help_text='Введите тип подключения',
                                       verbose_name='Тип подключения')
    recommended_psu_wattage = models.CharField(max_length=10,
                                                  help_text='Введите рекомендуемую мощность БП',
                                                  verbose_name='Рекомендуемая мощность БП')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('videocard-detail', args=[str(self.id)])

class type_RAM(models.Model):
    type = models.CharField(max_length=10,
                            help_text='Введите тип оперативной памяти',
                            verbose_name='Тип оперативной памяти')

    def __str__(self):
        return self.type

class RAM(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название оперативное памяти',
                            verbose_name='Название оперативной памяти')
    memory = models.CharField(max_length=10,
                            help_text='Введите объём модуля ОП',
                            verbose_name='Объём модуля ОП')
    type = models.ForeignKey('type_RAM',
                            on_delete=models.CASCADE,
                            verbose_name='Тип оперативной памяти')
    clock_frequency = models.CharField(max_length=10,
                            help_text='Введите тактовую частоту',
                            verbose_name='Тактовая частота')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ram-detail', args=[str(self.id)])

class CPUSocket(models.Model):
    socket_name = models.CharField(max_length=15,
                                   help_text='Введите название сокета',
                                   verbose_name='Сокет')
    def __str__(self):
        return self.socket_name

class CPU(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название процессора',
                            verbose_name='Название процессора')
    socket_cpu = models.ForeignKey('CPUSocket',
                            on_delete=models.CASCADE,
                            verbose_name='Сокет')
    nuclei = models.CharField(max_length=15,
                            help_text='Введите количество ядер',
                            verbose_name='Количество ядер')
    clock_frequency = models.CharField(max_length=10,
                            help_text='Введите тактовую частоту',
                            verbose_name='Тактовая частота')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cpu-detail', args=[str(self.id)])

class SSD(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название накопителя',
                            verbose_name='Название накопителя')
    capacity = models.CharField(max_length=10,
                            help_text='Введите ёмкость накопителя',
                            verbose_name='Ёмкость накопителя')
    speed = models.CharField(max_length=25,
                            help_text='Введите скорость чтения/записи',
                            verbose_name='Скорость чтения/записи')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ssd-detail', args=[str(self.id)])

class Motherboard(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название материнской платы',
                            verbose_name='Название материнской платы')
    socket_motherboard = models.ForeignKey('CPUSocket',
                            on_delete=models.CASCADE,
                            verbose_name='Сокет')
    memory_type = models.ForeignKey('type_RAM',
                            on_delete=models.CASCADE,
                            verbose_name='Тип оперативной памяти')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('motherboard-detail', args=[str(self.id)])

class PowerUnit(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Введите название блока питания',
                            verbose_name='Название блока питания')
    power = models.CharField(max_length=20,
                            help_text='Введите мощность БП',
                            verbose_name='Мощность БП')
    efficiency_standard = models.CharField(max_length=50,
                            help_text='Введите стандарт эффективности',
                            verbose_name='Стандарт эффективности')
    motherboard_connector_type = models.CharField(max_length=50,
                            help_text='Введите тип разъёма для мат. платы',
                            verbose_name='Тип разъёма для мат. платы')
    quantityCPU = models.CharField(max_length=50,
                            help_text='Введите количество разъёмов 4+4pin CPU',
                            verbose_name='Количество разъёмов 4+4pin CPU')
    quantityPCI_E = models.CharField(max_length=50,
                            help_text='Введите количество разъёмов PCI-E',
                            verbose_name='Количество разъёмов PCI-E')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('powerunit-detail', args=[str(self.id)])