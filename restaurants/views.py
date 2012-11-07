from django.views.generic import ListView, CreateView
from restaurants.models import Restaurant, Contract

class RestaurantListView(ListView):
    model = Restaurant

class CreateRestaurantView(CreateView):
    model = Restaurant
    success_url = '/restaurants/'

class ContractListView(ListView):
    model = Contract

class CreateContractView(CreateView):
    model = Contract
    success_url = '/contracts/'






