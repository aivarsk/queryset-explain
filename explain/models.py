from django.db import models


class CardRange(models.Model):
    start_range = models.CharField(max_length=19)
    end_range = models.CharField(max_length=19)
    # Just something to store along the range
    info = models.CharField(max_length=64)

    class Meta:
        indexes = [
            models.Index(
                fields=["-start_range", "end_range"], name="card_range_start_end_idx"
            ),
        ]

class FlatRange(models.Model):
    pan = models.CharField(max_length=19)
    klass = models.IntegerField()
    # Just something to store along the range
    info = models.CharField(max_length=64)

    class Meta:
        indexes = [
            models.Index(
                fields=["pan", "klass"], name="card_range_pan_idx"
            ),
        ]
