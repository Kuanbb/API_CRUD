from django.db import models

class Usuario(models.Model):
    apelido_usuario = models.CharField(max_length=100, primary_key=True, default='')
    email_usuario = models.EmailField(default='')

    def __str__(self):
        return f'Apelido: {self.apelido_usuario} | E-mail: {self.email_usuario}'