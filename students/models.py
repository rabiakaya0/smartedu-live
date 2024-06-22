from django.db import models

# Create your models here.
# 3. ADIM model oluşturuldu
class Student(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to="students/%Y/%m/%d/", default="students/defaultImage.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default = True)

    def __str__(self): 
        return self.name
