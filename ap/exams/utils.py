from .models import Exam, Section, Responses

# Returns the section referred to by the args, None if it does not exist
def get_exam_section(exam, section_id):
    try:
        section = Section.objects.get(exam=exam, section_index=section_id)
        return section
    except Section.DoesNotExist:
        return None

# Returns an array containing the interesting data for the given section. None
# returned if the exam is invalid
def get_exam_questions_for_section(exam, section_id):
    section = get_exam_section(exam, section_id)
    questions = []
    if (section == None):
        return None

    for i in range(section.first_question_index - 1, section.question_count):
        questions.append(section.questions[str(i+1)])

    return questions

# Returns an array containing the interesting data.  None is returned if the
# exam is invalid.
def get_exam_questions(exam):
    questions = []
    for i in range(0, exam.section_count):
        section_questions = get_exam_questions_for_section(exam, i)
        if (section_questions != None):
            questions += section_questions
        else:
            return []

        # TODO(verification): We should sanity check that the question numbers
        # per section are vaguely correct whenever we have an exam that has 
        # when we start having exams with more than one section.
    return questions

def get_exam_questions_for_section(exam, section_id):
    section = get_exam_section(exam, section_id)
    questions = []
    if (section == None):
        return None

    for i in range(section.first_question_index - 1, section.question_count):
        questions.append(section.questions[str(i+1)])

    return questions


# Returns a tuple of responses, grader_extras, and scores for the given exam 
# in the given section
def get_responses_for_section(exam_pk, section_id, session, 
                             trainee_pk, current_question):
    section = get_exam_section(exam_pk, section_id)
    responses = []
    if section == None:
        return []

    try:
        responses_object = Responses.objects.get(session=session, trainee=trainee_pk, section=section)
    except Responses.DoesNotExist:
        responses_object = None

    for i in range(section.first_question_index - 1, section.question_count):
        if responses_object:
            responses.append(responses_object.responses[str(i+1)])
        else:
            responses.append("")

    return responses

# Returns a tuple of responses, grader_extras, and scores for the given exam
def get_responses(exam, session, trainee_pk):
    current_question = 1
    responses = []
    grader_extras = []
    scores = []

    for i in range(0, exam.section_count):
        responses += get_responses_for_section(exam, i, session, trainee_pk, current_question)
        current_question += len(responses)

    return responses