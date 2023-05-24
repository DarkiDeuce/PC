from django.shortcuts import render
from django.http import *

def main(request):
    return render(request, 'base.html')