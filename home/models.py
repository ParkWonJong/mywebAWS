# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Authuser(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authuser'


class Beacon(models.Model):
    seq = models.IntegerField(db_column='Seq', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=50)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'beacon'
