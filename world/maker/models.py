from django.db import models

class Noise(models.Model):
    text = models.TextField()

    class Meta:
        app_label = "maker"

    def __unicode__(self):
        return self.text
