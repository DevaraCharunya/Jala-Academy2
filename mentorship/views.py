


from .models import Mentor, Student, Enrollment
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Mentor
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, redirect



def example_view(request):
    student_id = 1  # Replace with the actual ID you are working with
    return redirect(reverse('student_details', kwargs={'student_id': student_id}))




def home(request):
    return render(request, 'home.html') 

from django.shortcuts import render
from .models import Enrollment

def dashboard(request):
    # Count statistics
    student_count = Student.objects.count()
    mentor_count = Mentor.objects.count()
    
    # # Group students by status
    # ongoing_students = Enrollment.objects.filter(status='active').select_related('student', 'course')
    # completed_students = Enrollment.objects.filter(status='completed').select_related('student', 'course')
    # stopped_students = Enrollment.objects.filter(status='dropped').select_related('student', 'course')

    ongoing_students = Enrollment.objects.filter(status='ongoing')
    completed_students = Enrollment.objects.filter(status='completed')
    stopped_students = Enrollment.objects.filter(status='stopped')

    # Prepare the data for display
    student_enrollments = Enrollment.objects.select_related('student', 'course')

    context = {
        'student_count': student_count,
        'mentor_count': mentor_count,
        'ongoing_students': ongoing_students,
        'completed_students': completed_students,
        'stopped_students': stopped_students,
        'student_enrollments': student_enrollments,
    }
    return render(request, 'dashboard.html', context)


  



       




def mentor(request):
    mentors = Mentor.objects.all()
    return render(request,'mentor.html', {'mentors': mentors})




def student(request):
    query = request.GET.get('search', '')
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})





def mentor_details(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id) 
    students = mentor.student_set.all() 
    return render(request, 'mentorship/mentor_details.html', {
        'mentor': mentor,
        'students': students})
        



def student_details(request, student_id):
    # Fetch the specific student
    student = get_object_or_404(Student, id=student_id)
    
    
   
    # Retrieve the student's enrollments using the reverse relationship
    enrollments = student.enrollment_set.all()  # Assuming `Enrollment` has a foreign key to `Student`

    

    # Pass the student and their enrollments to the template
    return render(request, 'mentorship/student_details.html', {'student': student, 'enrollments': enrollments})
    
   




