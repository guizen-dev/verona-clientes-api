from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=455, default='')
    phone_number = models.CharField(max_length=455, default='')
    email_address = models.CharField(max_length=455, default='')
    created_data = models.DateTimeField(auto_now_add=True)