from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
)
from post import models as post_models
from django.urls import resolve

# Create your views here.


class IndexView(TemplateView):
    template_name = 'post/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
