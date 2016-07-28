from .models import Exam

from exams.utils import trainee_can_take_exam

def exams_available(request):
  user = request.user
  exams = Exam.objects.filter(is_open=True)
  exam_count = 0
  for exam in exams:
    if trainee_can_take_exam(user, exam):
      exam_count += 1

  return {'exams_available' : exam_count}
