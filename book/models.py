from django.db import models
from django.contrib.postgres.indexes import GinIndex

class BookModel(models.Model):
    title:models = models.CharField(max_length=1200, db_index=True)
    authors:models = models.CharField(max_length=1000)

    class Meta:
        indexes = [
            GinIndex(name="BookIndex", fields=["title"])
        ]

