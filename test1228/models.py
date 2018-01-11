# models.py
from django.db import models

class Z_hosts(models.Model):
    ZID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    InnerIP = models.CharField(max_length=50)
    InnerPort = models.CharField(max_length=50)
    OuterIP = models.CharField(max_length=50)
    OuterPort = models.CharField(max_length=50)
    AddDate = models.DateTimeField(auto_now_add=True)
    ModifyDate = models.DateTimeField(auto_now=True)
    IsVM = models.BooleanField(default=1)
    ZVIP = models.CharField(max_length=50,default='none')
    ZHaveVIP = models.BooleanField(default=0)


class Z_IP(models.Model):
    ZID = models.AutoField(primary_key=True)
    ZIP = models.CharField(max_length=50)
    ZIPType = models.IntegerField()
    ZMask = models.CharField(max_length=50)
    ZGateway = models.CharField(max_length=50)
    ZWanIP = models.CharField(max_length=50)
    ZSwitch = models.IntegerField()
    ZRouter = models.IntegerField()
    ZUserGroup = models.IntegerField()
    ZProjGroup = models.IntegerField()

class Z_User(models.Model):
    ZID = models.AutoField(primary_key=True)
    ZName = models.CharField(max_length=50)
    ZPassword = models.CharField(max_length=255)
    ZEmail = models.EmailField(unique=True)
    ZUserGroup = models.IntegerField()
    ZProjGroup = models.IntegerField()
    ZIsDismission = models.BooleanField(default=0)
    ZisDisabled = models.BooleanField(default=0)

    def __str__(self):
        return self.ZName



