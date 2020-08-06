from django.db import models

# Create your models here.

class OrganizationUrl(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField()
    create_date = models.DateTimeField(default=None)
