from django.db import models
from django.contrib.auth.models import User, auth


class Item(models.Model):
    item_id = models.TextField(default="0000")
    name = models.TextField(default="name")

    Available = 'A'
    Check = 'C'
    Pass = 'P'
    ITEM_STATUS = [
        (Available, 'Available'),
        (Check, 'Check'),
        (Pass, 'Pass'),
    ]

    status = models.CharField(max_length = 1, choices = ITEM_STATUS, default = Available)
    is_apply = models.BooleanField(default=False)

class Applying(models.Model):
    apply_user = models.TextField(default="user")
    item_name = models.TextField(default="none")
    item_id = models.TextField(default="0000")
    is_lent = models.BooleanField(default=False)

class Record(models.Model):
    item_id = models.TextField(default="0000")
    item_name = models.TextField(default="none")
    apply_user = models.TextField(default="user")
    item_status = models.BooleanField(default=False)
    lent_time = models.DateTimeField(auto_now_add=True)
    back_time = models.DateTimeField(auto_now=True)
