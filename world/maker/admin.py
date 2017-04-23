from django.contrib import admin
import models

for model in [models.Noise]:
    admin.site.register(model)
