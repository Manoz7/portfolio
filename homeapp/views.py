import email
from django.shortcuts import render
from django.views.generic import TemplateView

from homeapp.models import Contact, Portfolio

# Create your views here.

class HomeView(TemplateView):
    template_name = 'homeapp/index.html'
    

def homePage(request):
    portfolio = Portfolio.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        mycon = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        mycon.save()
        
        return render(request, 'homeapp/index.html')
    
    context = {'portfolio': portfolio}
    return render(request, 'homeapp/index.html', context)


def portfolioList(request):
    portfolio = Portfolio.objects.all()
    
    return render(request, 'homeapp/portfolio.html', {'portfolio': portfolio})

def portDetails(request, slug):
    port = Portfolio.objects.get(slug=slug)
    portfolio = Portfolio.objects.all().exclude(slug=slug)
    
    context= {'port': port, 'portfolio': portfolio}
    
    return render(request, 'homeapp/port_details.html', context)

def portfolioDetails(request):
    return render(request, 'homeapp/portfolio_details.html')