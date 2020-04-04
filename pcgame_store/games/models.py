from django.db import models
# from .models import User


class Game(models.Model):
    GENRE_CHOICES = [
        ("ACT", "Action"),
        ("ANM", "Anime"),
        ("2v2", "2 vs 2"),
    ]
    game_title = models.CharField(max_length=200)
    game_price = models.IntegerField()
    game_size = models.IntegerField()
    game_genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    game_min_graphics = models.IntegerField()
    game_short_description = models.CharField(max_length=500)

    def __str__(self):
        return "%s - %s" % (self.game_title, self.pk)


# class DownloadedGame(models.Model):
#     game_downloader = models.ForeignKey(to=User)
#     game_owned = models.ForeignKey(to=Game)
