from django.db import models

class Enroll(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    selected_course = models.CharField(max_length=200)
    course_amount = models.DecimalField(max_digits=10, decimal_places=2)

