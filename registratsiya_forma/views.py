from django.shortcuts import render
from .models import Student

def register(request):
    if request.POST:
        model = Student()
        model.first_name = request.POST.get('first_name','')
        model.last_name = request.POST.get('last_name','')
        model.company = request.POST.get('company','')
        model.email = request.POST.get('email','')
        model.area_code = request.POST.get('area_code','')
        model.phone_number = request.POST.get('phone','')
        model.subject = request.POST.get('subject','')
        model.exist = request.POST.get('exist','')
        model.save()
    return render(request, 'index.html')