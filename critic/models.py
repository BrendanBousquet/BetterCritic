from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Game(models.Model):
    game_name = models.CharField(max_length=30)
    game_score = models.IntegerField()

    def __unicode__(self):
        return self.game_name