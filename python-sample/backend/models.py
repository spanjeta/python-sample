from django.db import models
from django.utils import timezone
from accounts.models import *
# Create your models here.


class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    value = models.TextField()
    state_id = models.IntegerField()
    type_id = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    created_by_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_setting'
        managed = True
