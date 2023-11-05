from django.db import models
from django.contrib.auth.models import User
import random
import string


class Class(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='classes')
    class_code = models.CharField(max_length=6, unique=True, default='', editable=False)

    def save(self, *args, **kwargs):
        if not self.class_code:
            self.class_code = self.generate_class_code()
        super(Class, self).save(*args, **kwargs)

    def generate_class_code(self):
        # Generate a random 6-character alphanumeric code
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(6))

    def __str__(self):
        return self.name
