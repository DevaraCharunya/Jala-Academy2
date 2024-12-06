
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='mentors')
    
    def __str__(self):
        return self.name

    def student_count(self):
        return self.student_set.count()

class Student(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('stopped', 'Stopped'),
    ]
     
    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    
    

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('stopped', 'Stopped'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ongoing'
    )
    status_description = models.CharField(max_length=255, blank=True, null=True, help_text="Reason for status")
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.course.name} ({self.status})"
