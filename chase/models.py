from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_lives = models.IntegerField(default=3)  # Adjust based on game logic
    tabs_switched = models.IntegerField(default=0)  # Count of tab switches

    def __str__(self):
        return self.name
