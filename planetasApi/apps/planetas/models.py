from django.db import models

class PlanetasApi(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100, blank=False, null=False, unique=True)

    overview_content= models.CharField(max_length=350)
    overview_source= models.URLField(max_length=350)

    structure_content= models.CharField(max_length=350)
    structure_source= models.URLField(max_length=350)

    geology_content= models.CharField(max_length=350)
    geology_source= models.URLField(max_length=350)

    rotation = models.CharField(max_length=50)
    revolution = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)

    img_planet = models.ImageField(upload_to ='images')
    img_internal = models.ImageField(upload_to ='images')
    img_geology = models.ImageField(upload_to ='images')

    class Meta:

        verbose_name = 'Planeta'
        verbose_name_plural = 'Planetas'

    def __str__(self):
        return self.name
