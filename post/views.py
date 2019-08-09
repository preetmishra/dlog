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
        entries = post_models.Entry.objects.filter(publish=True)
        tag_list = post_models.Tag.objects.filter(tags__isnull=False).distinct()
        return render(request, self.template_name, {'entries': entries,
                                                    'tag_list': tag_list})


class PostDetailView(DetailView):
    template_name = 'post/post_detail.html'
    model = post_models.Entry


class FilterByTagView(TemplateView):
    template_name = 'post/index.html'
    
    def get(self, request, *args, **kwargs):
        tag = resolve(request.path_info).kwargs['slug']
        tag_list = post_models.Tag.objects.filter(tags__isnull = False).distinct()

        if tag == 'all':
            tag = None
            entries = post_models.Entry.objects.filter(publish = True)
        else:
            tag_id = post_models.Tag.objects.get(tag = tag).id
            entries = post_models.Entry.objects.filter(publish = True).filter(tags = tag_id)

        return render(request, self.template_name, {'entries': entries,
                                                    'tag_list': tag_list,
                                                    'tag_selected': tag})
