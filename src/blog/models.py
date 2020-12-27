from djongo import models

class Post(models.Model):
    nombre = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000, verbose_name='descripción')
    foto = models.ImageField(upload_to='posts', default='')
    slug = models.SlugField(unique=True)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "/%s/" % self.slug
        