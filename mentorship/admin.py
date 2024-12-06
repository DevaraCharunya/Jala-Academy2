
from django.contrib import admin
from .models import Mentor, Student, Course, Enrollment

admin.site.register(Mentor)

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)




