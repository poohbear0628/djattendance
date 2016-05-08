from .models import Exam

def exams_available(request):
    exams = Exam.objects.all()
    for exam in exams:
        if exam.is_available(request.user.trainee):
            return {'exam_available' : True}

    return {'exam_available' : False}