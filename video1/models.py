from django.db import models


class VideoRequests(models.Model):
    filename = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    font_color = models.CharField(max_length=255)
    bg_color = models.CharField(max_length=255)

    def __str__(self):
        return self.filename


def add(name, bg_color, font_color):
    new_request = VideoRequests(filename=name, bg_color=bg_color, font_color=font_color)
    new_request.save()
