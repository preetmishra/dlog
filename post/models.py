from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.SlugField(max_length = 256, unique = True)

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return self.tag

class Entry(models.Model):
    title = models.CharField(max_length = 256)
    body = models.TextField()
    slug = models.SlugField(max_length = 256, unique = True)
    publish = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    tags = models.ManyToManyField(Tag)

    class Meta :
        verbose_name_plural = "Entries"
        ordering = ['-date_created']

    def __str__(self) :
        return self.title

    