from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_scout = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=False)


class Scout(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Patrol(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=5)
    is_youth_position = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    child = models.ManyToManyField(Scout)

    def __str__(self):
        return self.user.username


class Leader(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class MeritBadge(models.Model):
    name = models.CharField(max_length=30, unique=True)
    short_name = models.CharField(max_length=17, blank=True, null=True)
    is_eagle_required = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RankRequirement(models.Model):
    sort_order = models.IntegerField()
    number = models.CharField(max_length=4)
    revision = models.CharField(max_length=5)
    short_desc = models.CharField(max_length=36, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_header = models.BooleanField(default=False)
    header = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.short_desc, self.rank)


class ScoutRankSignoff(models.Model):
    req_1a = models.DateField()
    req_1b = models.DateField()
    req_1c = models.DateField()
    req_2a = models.DateField()
    req_2b = models.DateField()
    req_2c = models.DateField()
    req_3a = models.DateField()
    req_3b = models.DateField()
    req_3c = models.DateField()
    req_3d = models.DateField()
    req_4a = models.DateField()
    req_4b = models.DateField()
    req_4c = models.DateField()
    req_4d = models.DateField()
    req_5a = models.DateField()
    req_5b = models.DateField()
    req_5c = models.DateField()
    req_6a = models.DateField()
    req_6b = models.DateField()
    req_6c = models.DateField()
    req_7a = models.DateField()
    req_7b = models.DateField()
    req_8 = models.DateField()
    req_9 = models.DateField()
    req_10 = models.DateField()
    req_11 = models.DateField()
