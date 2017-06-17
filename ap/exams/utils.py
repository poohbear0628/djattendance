import json

from datetime import timedelta

from .models import Exam, Section, Responses, Retake
from .models import Class
from schedules.models import Event
import json
from terms.models import Term
import string

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
    section_obj = {}
    questions = []
    if (section == None):
        return None

    for i in range(section.first_question_index - 1, section.question_count):
        q = section.questions[str(i+1)]
        questions.append(json.loads(q))
    section_obj['type'] = questions[0]['type']
    section_obj['instructions'] = section.instructions
    section_obj['id'] = section.id
    section_obj['questions'] = questions

    return section_obj

# Returns an array containing the interesting data.  None is returned if the
# exam is invalid.
def get_exam_questions(exam):
    sections = []
    for i in range(0, exam.section_count):
        section_questions = get_exam_questions_for_section(exam, i)
        if (section_questions != None):
            sections.append(section_questions)
        else:
            return []

        # TODO(verification): We should sanity check that the question numbers
        # per section are vaguely correct whenever we have an exam that has
        # when we start having exams with more than one section.
    return sections

# Returns the section referred to by the args, None if it does not exist
def get_exam_sectionOLD(exam, section_id):
    try:
        section = Section.objects.get(exam=exam, section_index=section_id)
        return section
    except Section.DoesNotExist:
        return None

# Returns an array containing the interesting data for the given section. None
# returned if the exam is invalid
def get_exam_questions_for_sectionOLD(exam, section_id):
    section = get_exam_section(exam, section_id)
    questions = []
    if (section == None):
        return None

    for i in range(section.first_question_index - 1, section.question_count):
        q = section.questions[str(i+1)]
        questions.append(json.loads(q))

    return questions

# Returns an array containing the interesting data.  None is returned if the
# exam is invalid.
def get_exam_questionsOLD(exam):
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

# Returns a tuple of responses, grader_extras, and scores for the given exam
# in the given section
def get_responses_for_section(exam_pk, section_index, session):
    section = get_exam_section(exam_pk, section_index)
    responses = {}
    if section == None:
        return []

    try:
        responses_object = Responses.objects.get(session=session, section=section)
    except Responses.DoesNotExist:
        responses_object = None

    for i in range(section.first_question_index - 1, section.question_count):
        if responses_object and str(i+1) in responses_object.responses:
            r = responses_object.responses[str(i+1)]
            responses[i] = json.loads(r)
        else:
            responses[i] = json.loads('')
    return responses


# Returns a tuple of responses, grader_extras, and scores for the given exam
# in the given section
def get_responses_for_sectionOLD(exam_pk, section_id, session, current_question):
    section = get_exam_section(exam_pk, section_id)
    responses = []
    if section == None:
        return []

    try:
        responses_object = Responses.objects.get(session=session, section=section)
    except Responses.DoesNotExist:
        responses_object = None

    for i in range(section.first_question_index - 1, section.question_count):
        if responses_object and str(i+1) in responses_object.responses:
            r = responses_object.responses[str(i+1)]
            responses.append(json.loads(r))
        else:
            responses.append({})

    return responses

# Returns a tuple of responses, grader_extras, and scores for the given exam
def get_responses(exam, session):
    responses = []
    sections = Section.objects.filter(exam=exam)

    for i in range(0, len(sections)):
        responses.append(get_responses_for_section(exam, i, session))
    return responses

# Returns a tuple of responses, grader_extras, and scores for the given exam
def get_responsesOLD(exam, session):
    current_question = 1
    responses = []
    grader_extras = []
    scores = []

    for i in range(0, exam.section_count):
        responses += get_responses_for_section(exam, i, session, current_question)
        current_question += len(responses)
    return responses

def get_edit_exam_context_data(context, exam, training_class):
    questions = get_exam_questions(exam)
    duration = exam.duration.seconds / 60

    context['exam_not_available'] = False
    context['training_class'] = training_class
    context['term'] = exam.term
    context['exam_description'] = exam.description
    context['is_open'] = bool(exam.is_open)
    context['is_final'] = bool(exam.category == 'F')
    context['duration'] = duration
    context['data'] = questions
    return context

# if exam is new, pk will be a negative value
def save_exam_creation(request, pk):
    P = request.POST
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    #print "BODY: " + str(body)
    total_score = 0

    #METADATA
    training_class = Class.objects.get(id=body['metadata']['training-class'])
    term = Term.objects.get(id=body['metadata']['term'])
    exam_description = body['metadata']['exam_description']
    is_open = body['metadata']['is-open'] 
    is_open = is_open and is_open == 'True'
    exam_category = body['metadata']['exam-category']
    duration = timedelta(minutes=int(body['metadata']['duration']))
    #print "metadata: " + str(body['metadata'])
    #print "training-class:" + str(training_class)
    #print "term: " + str(term)
    #print "exam_description: " + str(exam_description)
    #print "is open: " + str(is_open)
    #print "exam_category: " + str(exam_category)
    #print "duration: " + str(duration)
    #print "********************************************************************"

    existing_sections = []
    if pk < 0:
        exam = Exam(training_class=training_class,
            term=term,
            description=exam_description,
            is_open=is_open,
            duration=duration,
            category=exam_category,
            total_score=total_score)
        exam.save()
        #section = Section(exam=exam,
        #    instructions=instructions,
        #    section_index=section_index,
        #    question_count=question_count)
    else:
        exam = Exam.objects.get(pk=pk)
        exam.is_open = is_open
        exam.duration = duration
        exam.description = exam_description
        exam.category = exam_category
        exam.total_score = total_score
        exam.save()
        for existing_section in exam.sections.all():
            existing_sections.append(int(existing_section.id))

    #SECTIONS
    sections = body['sections']
    #print "SECTIONS: " + str(sections)
    section_index = 0
    for section in sections:
        try:
            section_instructions = section['instructions']
            section_questions = section['questions']
            #print "section_instructions: " + str(section_instructions)
            #print "section_questions: " + str(section_questions)

            question_hstore = {}
            question_count = 0
            section_type = "E"
            for question in section_questions:
                qPack = {}
                qPack['prompt'] = question['question-prompt']
                qPack['points'] = question['question-point']
                qPack['type'] = question['question-type']
                question_point = question['question-point']
                #print "question prompt, point, type, point: " + str(question['question-prompt']) + ";" + str(question['question-point']) + ";" + str(question['question-type']) + ";" + str(question['question-point'])
                total_score += int(question_point)
                #question_prompt = question['question-prompt']
                question_type = question['question-type']
                options = ""
                answer = ""
                if question_type == "mc":
                    for letter in list(string.ascii_lowercase):
                        choice = 'question-option-' + letter
                        if choice in question:
                            #every choice in the MC question will go here
                            options += question[choice] + ";"
                        if letter.upper() in question:
                            #every checked choice i.e. the answer to the question will go here
                            answer += letter.upper() + ";"
                    options = options.rstrip(';')
                    answer = answer.rstrip(';')
                    section_type = "MC"
                elif question_type == "matching":
                    answer = question["question-match"]
                    section_type = "M"
                elif question_type == "tf":
                    section_type = "TF"
                    if "true" in question and question["true"] == "on":
                        answer = "true"
                    elif "false" in question and question["false"] == "on":
                        answer = "false"
                if options != "":
                    qPack['options'] = options
                if answer != "":
                    qPack['answer'] = answer     
                question_hstore[str(question_count+1)] = json.dumps(qPack)
                question_count += 1

            #SECTION SEE EXISTING TO MODIFY OR DELETE
            section_id = section.get('section_id')
            existing_questions = []

            #QUESTION find existing to modify or delete
            
            if pk < 0:
                section_obj = Section(exam=exam,
                    instructions=section_instructions,
                    section_index=section_index,
                    section_type=section_type,
                    questions=question_hstore,
                    question_count=question_count)    
            elif int(section.get('section_id')) in existing_sections:
                section_obj = Section.objects.get(pk=int(section.get('section_id')))
                #section = existing_sections[section_index]
                
                section_obj.instructions = section_instructions
                section_obj.section_type = section_type
                section_obj.questions = question_hstore
                section_obj.question_count = question_count
                existing_sections.remove(int(section.get('section_id')))
            else:
                section_obj = Section(exam=exam,
                    instructions=section_instructions,
                    section_index=section_index,
                    section_type=section_type,
                    questions=question_hstore,
                    question_count=question_count)
                
            section_index += 1
            section_obj.save()
        except KeyError:
            pass
    for remaining_id in existing_sections:
        Section.objects.filter(id=remaining_id).delete()
    exam.total_score = total_score
    exam.save()

def save_exam_creationOLD(request, pk):
    P = request.POST
    exam_desc = P.get('exam_description')
    print P, exam_desc
    # bool(request.POST.get('exam-category')=='1')
    exam_category = P.get('exam-category','')
    is_open = P.get('is-open','')
    is_open = is_open and is_open == 'True'
    duration = timedelta(minutes=int(P.get('duration',0)))

    # questions are saved in an array
    question_prompt = P.getlist('question-prompt')
    question_point = P.getlist('question-point')
    question_type = P.getlist('question-type')
    print "question type: " + str(question_type)
    #add question-match and question-option
    question_count = len(question_prompt)

    total_score = 0
    for point in question_point:
        total_score += int(point)

    section_index = 0
    instructions = "Place Holder"
    # section_index = int(request.POST.get('section-index', ''))
    # description = request.POST.get('description', '')

    question_hstore = {}
    for index, (prompt, points, qtype) in enumerate(zip(question_prompt, question_point, question_type)):
        qPack = {}
        qPack['prompt'] = prompt
        qPack['points'] = points
        qPack['type'] = qtype
        question_hstore[str(index+1)] = json.dumps(qPack)

    if pk < 0:
        training_class = Class.objects.get(id=P.get('training-class'))
        term = Term.objects.get(id=P.get('term'))
        exam = Exam(training_class=training_class,
            term=term,
            description=exam_desc,
            is_open=is_open,
            duration=duration,
            category=exam_category,
            total_score=total_score)
        exam.save()
        section = Section(exam=exam,
            instructions=instructions,
            section_index=section_index,
            question_count=question_count)
    else:
        exam = Exam.objects.get(pk=pk)
        training_class = Class.objects.get(id=exam.training_class.id)
        term = Term.objects.get(id=P.get('term'))
        exam.is_open = is_open
        exam.duration = duration
        exam.description = exam_desc
        exam.category = exam_category
        exam.total_score = total_score
        exam.save()

        '''
        Modify to work for exams with multiple sections
        '''
        section = get_exam_section(exam, 0)

    section.questions = question_hstore
    section.question_count = question_count
    section.save()

def get_exam_context_data(context, exam, is_available, session, role):
    context['role'] = role
    context['exam'] = exam
    if hasattr(session, 'trainee'):
        context['examinee'] = session.trainee

    if not is_available:
        context['exam_available'] = False
        return context

    context['exam_available'] = True
    #print "QUESTIONS AND RESPONES CONTEXT: "
    questions = get_exam_questions(exam)
    responses = get_responses(exam, session)
    #print "RESPONSES: "
    #print str(responses)
    current_question = 0
    for each in questions:
        questions_in_section = len(each['questions'])
        #for i in range(0, questions_in_section):

        

    #print str(questions)
    #print str(responses)
    print "result of questions: " + str(questions)

    context['data'] = zip(questions, responses)
    #print "data context is: " + str(context['data'])

    return context

def retake_available(exam, trainee):
    try:
        retake = Retake.objects.filter(exam=exam,
                                    trainee=trainee,
                                    is_complete=False)
        # implicit assumption here that there is only one retake possible
        if  retake and not retake[0].is_complete:
            return True
    except Retake.DoesNotExist:
        pass
    return False

def save_responses(session, section, responses):
    try:
        responses_obj = Responses.objects.get(session=session, section=section)
    except Responses.DoesNotExist:
        responses_obj = Responses(session=session, section=section, score=0)

    responses_hstore = responses_obj.responses
    if responses_hstore is None:
        responses_hstore = {}
    
    #for key in responses:
    #    print "key: " + str(key) + "; responses: " + str(responses[str(key)])
    #    print "type: " + str(type(key))
    #    responses_hstore[key] = json.dumps(responses[str(key)])
    #for index, response in enumerate(responses):
    #    print "index: " + str(index) + "; response: " + str(response)
     #   responses_hstore[str(index+1)] = json.dumps(response)


    #NEW CODE TO TAKE CARE OF BLANK ANSWERS
    for i in range(1, section.question_count + 1):
        try:
            print "key: " + str(i) + "; responses: " + str(responses[str(i)])
            responses_hstore[str(i).decode('utf-8')] = json.dumps(responses[str(i)])
        except KeyError:
            responses_hstore[str(i).decode('utf-8')] = json.dumps(str('').decode('utf-8'))
    print "resulting hstore: " + str(responses_hstore)

    responses_obj.responses = responses_hstore
    #print "responses in saved: " + str(responses_obj.responses)
    responses_obj.save()

def trainee_can_take_exam(trainee, exam):
    #print 'can take exam', exam, trainee.is_active, exam.training_class, exam.training_class.class_type, trainee.current_term
    if exam.training_class.class_type == 'MAIN':
        return trainee.is_active
    elif exam.training_class.class_type == '1YR':
        return trainee.current_term <= 2
    elif exam.training_class.class_type == '2YR':
        return trainee.current_term >= 3
    else:
        #fix when pushing
        return trainee.is_active
        #return False  #NYI
