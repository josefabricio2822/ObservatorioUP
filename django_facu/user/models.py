from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Creamos la clase Perfil.
class Profile(models.Model):
    # Un usuario solo puede tener un Perfil.
    # Si se borra el ususario se borra el perfil pero no viceversa. Ya que es en orden cascada
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade automaticamente una foto default de perfil.
    # En se caso tenga una, la extrae de la carpeta profile_pics.
    # Por la configuracion del proyecto (settings) esta se buscara en la carpeta /media/
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #Al crearse se asignara el nombre de "(Nombre de Uusrio) Profile"
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)