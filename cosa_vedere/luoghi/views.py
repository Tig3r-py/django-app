from django.shortcuts import render
from .models import City, PlaceToVisit

# Create your views here.
def home(request):
    #info = Places.objects.filter(nome = 'Roma')
    # funzione che una volta premuto il bottone porti alla giusta città
    #lista = ['roma', 'venezia', 'firenze', 'milano']
    #luoghi_obj = None
    #luoghi_obj = Place.objects.filter(nome_luogo=x).values()
    luoghi_obj = City.objects.all()
    return render(request, 'luoghi/home.html', {'data': luoghi_obj})

def place_view(request, nome_luogo=None, *args, **kwargs):
    luoghi_obj = None
    posti_obj = None
    if nome_luogo is not None:
        luoghi_obj = City.objects.get(nome_luogo=nome_luogo)
    posti_obj = PlaceToVisit.objects.filter(dove=City.objects.get(nome_luogo=nome_luogo))
    context = {
        "object" : luoghi_obj,
        "place" : posti_obj
    }
    #print(type(nome_luogo)) str
    return render(request, 'luoghi/info_city.html', context=context)
#prendere poi anche tutto da l tabase plase to visit

def detail(request, nome=None, *args, **kwargs):
    detail_obj=None
    if nome is not None:
        detail_obj = PlaceToVisit.objects.get(nome=nome)
    data={
        "data":detail_obj,
    }
    return render(request, 'luoghi/detail_place.html', context=data)
"""
citta=Place.object.filter(citta='True').value
print(citta) ?forse è una lista

if luoghi_obj.citta:

lista = ['roma', 'venezia', 'firenze', 'milano']
    for x in lista:
        luoghi_obj2 = Place.objects.filter(nome_luogo=x).values()
        context2 = {
            'data': luoghi_obj2,
        }
    print(context2)#dizionario ma solo con ultimo elemento

#usare metodo get per i buttoni
"""


def serch_place(request, *args, **kwargs):
    query_dict = request.GET #è un dizionario
    query = query_dict.get("query") # <input class="form-control me-2" type="search" placeholder="luoghi..." aria-label="Search" name="query">
    luoghi_obj = None
    if query is not None:
        luoghi_obj = City.objects.get(nome_luogo=query)
    context = {
        "object" : luoghi_obj
    }
    return render(request, 'luoghi/home.html', context=context)
#funziana solo se sei su italia/


