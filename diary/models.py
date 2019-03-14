from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug():
    return '-'+ str(int(time()))



class Articles (models.Model):
    body = models.TextField(db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail_url',  kwargs={'slug':self.slug})

    def __str__ (self):
        return self.body

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug= gen_slug()
        super().save(*args,**kwargs)

    def get_update_url(self):
        return reverse('post_update_url',kwargs={'slug':slug})
    def get_delete_url(self):
        return reverse('post_delete_url',kwargs={'slug':slug})