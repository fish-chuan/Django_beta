from django.db import models
from django.contrib.auth.models import User, auth


class Item(models.Model):
    item_id = models.TextField(default="0000")
    name = models.TextField(default="name")
    status = models.BooleanField(default=False)

class Applying(models.Model):
    apply_user = models.TextField(default="name")
    item_num = models.TextField(default="0000")
    is_pass = models.BooleanField(default=False)
