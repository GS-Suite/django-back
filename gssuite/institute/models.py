from django.db import models
from accounts.models import User

# Create your models here.


class Institute(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    email = models.EmailField()
    
class Course(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    is_staff = models.BooleanField(default = False)
    is_institute = models.BooleanField(default = False)