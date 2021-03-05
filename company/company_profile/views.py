from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'company_profile/index.html', context)

def profil(request):
    context = {}
    return render(request, 'company_profile/profil_lapas.html', context)