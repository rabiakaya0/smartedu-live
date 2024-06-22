from django.contrib import admin

# Register your models here.
#
from . models import Student

#4. ADIM model kaydedildi
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')
