from django.contrib import admin
from .models import Course, Group, Lesson, Student, Credit

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Credit)
