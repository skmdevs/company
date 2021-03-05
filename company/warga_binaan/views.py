from django.shortcuts import render
import pandas as pd
import json
from .models import Prison

# Create your views here.
def tabel_warga_binaan(request):
    
    context = {'d':Prison.objects.all()}

    return render(request, 'warga_binaan/index.html', context)