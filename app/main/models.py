from django.db import models


class AboutU(models.Model):
    about_us = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.about_us