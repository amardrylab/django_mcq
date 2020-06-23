from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AddUser(models.Model):
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	name = models.CharField(max_length=30)

class Set(models.Model):
        opts = (('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'))
        AnsQ1 = models.CharField(max_length=1, choices=opts)
        AnsQ2 = models.CharField(max_length=1, choices=opts)
        AnsQ3 = models.CharField(max_length=1, choices=opts)
        AnsQ4 = models.CharField(max_length=1, choices=opts)
        AnsQ5 = models.CharField(max_length=1, choices=opts)
        AnsQ6 = models.CharField(max_length=1, choices=opts)
        AnsQ7 = models.CharField(max_length=1, choices=opts)
        AnsQ8 = models.CharField(max_length=1, choices=opts)
        AnsQ9 = models.CharField(max_length=1, choices=opts)
        AnsQ10 = models.CharField(max_length=1, choices=opts)
        submitby= models.ForeignKey(User, on_delete=models.CASCADE)

        def get_absolute_url(self):
                return reverse('success')

