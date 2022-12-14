from django.urls import path, include
from .views import *

app_name = "api"

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('mashina-api/', MashinaMakeAPI),
    path('mashina-api/<int:pk>/', bittaAPI),
    path('mahsulot-api/', MahsulotMakeAPI),
    path('mahsulot-api/<int:pk>/', birAPI),
    path('create/', malumotjoylash),
    path('update/<int:pk>/', malumotyangilash),
    path('delete/<int:pk>/', malumotdelete),
    path('search/', maxsulotserach),
    path('filter', filterMahsulot),
]
