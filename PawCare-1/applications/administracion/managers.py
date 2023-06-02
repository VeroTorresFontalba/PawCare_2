from django.shortcuts import render
from django.db import models
from django.db.models import Q

class ColabManager(models.Manager):
    def listar_colaboradores(self):
        return self.all()