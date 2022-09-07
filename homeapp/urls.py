from django.urls import path
from homeapp.views import HomeView
from homeapp import views

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', views.homePage, name= 'home'),
    path('about', views.aboutPage, name= 'about'),
    path('portfolio', views.portfolioList, name= 'portfolio'),
    path('portfolio/<slug:slug>', views.portDetails, name = 'port_details'),
    path('work', views.portfolioDetails, name='portfolio_details')
]
