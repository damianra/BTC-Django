from django.db import models

# Create your models here.
class BtcHistory(models.Model):
    date = models.CharField(primary_key=True, max_length=20)
    close = models.CharField(max_length=20)
    open = models.CharField(max_length=20)
    max_value = models.CharField(max_length=20)
    min_value = models.CharField(max_length=20)
    vol = models.CharField(max_length=20, blank=True, null=True)
    var = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'btc_history'