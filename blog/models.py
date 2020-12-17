from django.db import models

class Post(models.Model):
    nombre = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    foto = models.ImageField(upload_to='productos', default='')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "/ocasion/%s/" % self.slug
        