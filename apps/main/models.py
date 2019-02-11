from django.db import models

# Create your models here.

class JdFirstCate(models.Model):
    first_cate_id = models.AutoField(primary_key=True)
    first_cate_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'Jd_FirstCate'


class JdSecondCate(models.Model):
    second_cate_id = models.AutoField(primary_key=True)
    second_cate_name = models.CharField(max_length=200)
    first_cate_id = models.ForeignKey(to=JdFirstCate, on_delete=models.CASCADE, db_column='first_cate_id')

    class Meta:
        db_table = 'Jd_SecondCate'


class JdThirdCate(models.Model):
    third_cate_id = models.AutoField(primary_key=True)
    third_cate_name = models.CharField(max_length=200)
    second_cate_id = models.ForeignKey(to=JdSecondCate, on_delete=models.CASCADE, db_column='second_cate_id')

    class Meta:
        db_table = 'Jd_ThirdCate'