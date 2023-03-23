from django.db import models

# Create your models here.

class DatosHome(models.Model):
    """ modelo para la pagina de inicio """
    
    contador_clicks_wthasapp = models.IntegerField()
    
    def __str__(self):
        return str(self.id) + ' ' + str(self.contador_clicks_wthasapp)
    