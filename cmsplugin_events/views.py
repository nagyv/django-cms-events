from django.views.generic import ListView, DetailView

from .models import Event, Category


class EventListView(ListView):
    model = Event


class EventDetailView(DetailView):
    model = Event


class CategoryListView(ListView):
    model = Category
