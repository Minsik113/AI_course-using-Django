from django.db import models

# Create your models here.
class Member(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user_pw = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    c_date = models.DateTimeField() # 날짜 - 자동으로 넣어줄것이다.