from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':5, 'cols':40})},
    }

admin.site.register(Post, PostAdmin)