from django.db import models


class Student(models.Model):
    StudentName = models.CharField(max_length = 15)
    Rollnumber = models.IntegerField(default=0)
    Email = models.EmailField(max_length = 50)
    MobileNumber =models.BigIntegerField()
    DateOfBirth = models.DateField(max_length = 50)

    def __str___(self):
        return self.Student