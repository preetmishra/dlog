from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
)
from post import models as post_models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'post/index.html'

    # def get_queryset(self):
    #     return post_models.Entry.objects.filter(publish=True)

    def get(self, request, *args, **kwargs):
        entries = post_models.Entry.objects.filter(publish=True)
        tag_list = post_models.Tag.objects.filter(tags__isnull=False).distinct()
        return render(request, self.template_name, {'entries': entries,
                                                    'tag_list': tag_list})


class PostDetailView(DetailView):
    template_name = 'post/post_detail.html'
    model = post_models.Entry
