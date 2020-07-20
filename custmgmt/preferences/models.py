from django.db import models

# Create your models here.

class Topic(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name

class Preference(models.Model):

    ENTITY_CHOICES = [
        ('asset', 'Asset'),
        ('account', 'Account'),
        ('customer', 'Customer'),
        ('user', 'User'),
        ('marketing', 'Marketing'),
    ]
    
    topic = models.ForeignKey('Topic', related_name='topic', on_delete=models.CASCADE)
    user_ref = models.CharField(max_length=255, db_index=True)
    opted_in = models.BooleanField(default=True)
    entity = models.CharField(max_length=50, blank=True, choices=ENTITY_CHOICES)
    entity_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return ("{0}-{1}-{2}".format(self.topic, self.user_ref, self.opted_in))

class MediumManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Medium(models.Model):

    MEDIUM_CHOICES =[
        ('email', 'eMail'),
        ('sms', 'SMS'),
        ('push', 'Push Notification'),
        ('inapp', 'In-App'),
    ]

    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES)
    medium_value = models.CharField(max_length=255)
    status = models.BooleanField(default=True) 
    preference = models.ForeignKey('Preference', on_delete=models.CASCADE, related_name='mediums')

    objects = MediumManager()

    def __str__(self):
        return ("{0}-{1}-{2}".format(self.medium, self.medium_value, self.status))
