from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User
# Create your models here.
#burda değişiklik yaptıysan terminale python manage.py makemigrations && python manage.py migrate

class Category(models.Model):
    name = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length = 50, unique=True, null = True)

    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length = 50, null = True)
    slug = models.SlugField(max_length = 50, unique=True, null = True)

    def __str__(self):
        return self.name

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null = True, on_delete = models.CASCADE)#öğretmen silinince öğretmenin verdiği dersler de silinecek 
    name = models.CharField(max_length = 200, unique=True)
    category = models.ForeignKey(Category, null = True, on_delete = models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank = True)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    description = models.TextField(blank = True, null = True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/defaultImage.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default = True)

    def __str__(self):
        return self.name

  
        
#  terminal komutları
# from courses.models import Course    
#Course.objects.all()
#Course.objects.create(name='yeni kurs', description='sdjfhn')
#courses_ids = courses.values_list('id') 
#course2 = Course.objects.get(id=2)
#course2.name = 'yorgunluık' 
#course2.save()
#Course.objects.get(id=7).delete()
#Course.objects.order_by('-name') 
#Course.objects.filter(available=True)  
#Course.objects.filter(name__startswith='aş')  
#Course.objects.exclude(name__startswith='aş')  
# from courses.models import Category, Course
#Category.objects.get(id=1).course_set.all()
#parent_object.childmodel_set.all()
#Course.objects.get(id=1).category.name 
#