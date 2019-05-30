from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('paciente/', views.paciente_list),
    path('paciente/<int:paciente_id>/', views.paciente_show),
    
]


#ath('home/', views.home),
 #   path('home/<str:time>/', views.time),
  #  path('home/<str:time>/<str:jogador>/', views.jogador),
   # path('home/<str:time>/<str:jogador>/<str:melhor>/', views.melhor),