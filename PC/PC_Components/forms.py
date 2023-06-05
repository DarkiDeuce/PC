from django import forms
from .models import VideoCards, RAM, CPU, SSD, Motherboard, PowerUnit

class VideoCardsForm(forms.Form):
    videocard = forms.ModelChoiceField(queryset=VideoCards.objects.all(), label='Материнская плата')

class RAMForm(forms.Form):
    ram = forms.ModelChoiceField(queryset=RAM.objects.all())

class CPUForm(forms.Form):
    cpu = forms.ModelChoiceField(queryset=CPU.objects.all())

class SSDForm(forms.Form):
    ssd = forms.ModelChoiceField(queryset=SSD.objects.all())

class MotherboardForm(forms.Form):
    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all())

class PowerUnitForm(forms.Form):
    powerunit = forms.ModelChoiceField(queryset=PowerUnit.objects.all())
