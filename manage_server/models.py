from typing import Any
from django.db import models


# Create your models here.
#
class ManagedPC(models.Model):
    """Managed PC model"""
    hostname = models.CharField(max_length=100, help_text='PC hostname')
    device_id = models.CharField(max_length=100, help_text='PC device ID')
    management_id = models.CharField(max_length=100, help_text='PC management ID like "PXXX-XXX"')
    updated_at = models.DateTimeField('last update', auto_now=True, editable=False)

    def __str__(self) -> Any:
        return self.management_id

class ManagedPCUser(models.Model):
    """Managed PC user model"""
    user_id = models.CharField(max_length=100, help_text='User ID')
    user_displayname = models.CharField(max_length=100, help_text='User name')
    updated_at = models.DateTimeField('last update', auto_now=True, editable=False)

    def __str__(self) -> Any:
        return self.user_displayname

class ManagedPCUserRelation(models.Model):
    """Managed PC user relation model"""
    managed_pc = models.ForeignKey(ManagedPC, on_delete=models.CASCADE)
    managed_user = models.ForeignKey(ManagedPCUser, on_delete=models.CASCADE)
    updated_at = models.DateTimeField('last update', auto_now=True, editable=False)

    def __str__(self) -> Any:
        return self.managed_pc.management_id + ' - ' + self.managed_user.user_displayname

class AccessToken(models.Model):
    """Access token model"""
    access_token = models.CharField(max_length=100, help_text='Access token')
    managed_user = models.ForeignKey(ManagedPCUser, on_delete=models.SET_DEFAULT, default=None, null=True)
    created_at = models.DateTimeField('last update', auto_now=True, editable=False)
    expires_in = models.IntegerField(help_text='Expires in seconds', default=0)

class OperationLog(models.Model):
    """Operation log model"""
    managed_user = models.ForeignKey(ManagedPCUser, on_delete=models.CASCADE)
    managed_pc = models.ForeignKey(ManagedPC, on_delete=models.CASCADE)
    operation = models.CharField(max_length=100, help_text='Operation')
    operation_status = models.CharField(max_length=100, help_text='Operation status')
    operation_result = models.CharField(max_length=100, help_text='Operation result')
    operation_time = models.DateTimeField('operation time')
    updated_at = models.DateTimeField('last update', auto_now=True, editable=False)

    