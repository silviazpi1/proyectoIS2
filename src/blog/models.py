from djongo import models
from djrichtextfield.models import RichTextField


class Post(models.Model):
    nombre = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    descripcion = RichTextField(verbose_name='descripción')
    foto = models.ImageField(upload_to='posts', default='')
    slug = models.SlugField(unique=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "/%s/" % self.slug
        