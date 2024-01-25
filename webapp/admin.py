from django.contrib import admin

from .models import Course,Section,Gender,YearLevel,Student

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Gender)
admin.site.register(YearLevel)
admin.site.register(Student)


