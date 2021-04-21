from test_auth.models import Person
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def sign_in(request):
    if request.method == "POST":
        person_ = Person()
        person_.full_name = request.POST.get("full_name")
        person_.corp = request.POST.get("corp")
        person_.phone = request.POST.get("phone")
        person_.mail = request.POST.get("mail")
        person_.save()
        return render(request, 'succes.html', context={ 'person_': person_})
    else:
        return render(request, "login.html")
