from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class YearLevel(models.Model):
    level = models.CharField(max_length=255)

    def __str__(self):
        return self.level

class Student(models.Model):
    studentnumber = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    level = models.ForeignKey(YearLevel, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255 , null=True)


    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.studentnumber})"


