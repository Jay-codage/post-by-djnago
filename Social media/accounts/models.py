from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


class Users(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
