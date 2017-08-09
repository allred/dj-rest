# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    message_text = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.message_text)
