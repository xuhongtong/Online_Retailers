from django.db import models

# Create your models here.
from account.models import User


class QuestionSafety(models.Model):
    qid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(to=User,on_delete=models.CASCADE,db_column='uid')
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'question'
        verbose_name = '安全问题'

