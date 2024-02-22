from django.db import models
from django.utils import timezone

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

class Region(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Device(models.Model):#id os ip mac regione
    username = models.CharField(max_length=30, unique = True)
    ip = models.GenericIPAddressField(unique=True)
    port = models.PositiveIntegerField()
    so = models.CharField(max_length=30)
    mac = models.TextField(unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Agent(models.Model):#id pid permission  disc location
    ROLES = [("U", "USER"), ("E", "ELEVATED")
             ]
    
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    pid = models.PositiveIntegerField()
    agent_permission = models.CharField(max_length=1, choices=ROLES)
    location = models.TextField()

class Message(models.Model):#tipo esito descrizione payload
    TYPE = [("R", "REPLY"), ("E", "EXECUTE")
            ]
    RESULT = [("O", "OK"), ("N","NOK"), ("E", "ERROR")
              ]
    
    agent = models.ManyToManyField(Agent)
    mess_type = models.CharField(max_length=1, choices=TYPE)
    mess_res = models.CharField(max_length=1, choices=RESULT)
    description = models.CharField(max_length=100)
    payload = models.CharField(max_length=50)
    timestamp = models.DateTimeField(default=timezone.now)