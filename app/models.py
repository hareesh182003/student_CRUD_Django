from django.db import models

# Create your models here.
class College(models.Model):
    col_id = models.IntegerField(primary_key=True)
    col_name = models.CharField(max_length=100)
    col_address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.col_name

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=40)
    stu_year = models.IntegerField()
    stu_address = models.CharField(max_length=50)
    col_id = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.stu_name

