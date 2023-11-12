from django.urls import path, include
from . import views


app_name = 'luoghi'
#infovisit.it
urlpatterns = [
    path('home/', views.home),
    path('<str:nome_luogo>/', views.place_view),
    path('<str:nome_luogo>/<str:nome>/', views.detail),
    path('', views.serch_place, name="search"),
     #o funziona anche con place view perchè manda direttamente a roma/
]