import json

from datetime import timedelta

from .models import Exam, Section, Responses, Retake
from .models import Class
from schedules.models import Event
import json
from terms.models import Term
import string
import random
import re

# Returns the section referred to by the args, None if it does not exist
def get_exam_section(exam, section_id):
    try:
        section = Section.objects.get(exam=exam, section_index=section_id)
        return section
    except Section.DoesNotExist:
        return None

# Returns an array containing the interesting data for the given section. None
# returned if the exam is invalid
def get_exam_questions_for_section(exam, section_id, include_answers):
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
    matching_answers = []
    if not include_answers:
        for each in section_obj['questions']:
            answer = each.pop('answer', None)
            if section_obj['type'] == 'matching' and answer != None:
                matching_answers.append(answer)
    random.shuffle(matching_answers)
    if matching_answers != []:
        section_obj['matching_answers'] = matching_answers
    return section_obj

# Returns an array containing the interesting data.  None is returned if the
# exam is invalid.
def get_exam_questions(exam, include_answers):
    sections = []
    for i in range(0, exam.section_count):
        section_questions = get_exam_questions_for_section(exam, i, include_answers)
        if (section_questions != None):
            sections.append(section_questions)
        else:
            return []

        # TODO(verification): We should sanity check that the question numbers
        # per section are vaguely correct whenever we have an exam that has
        # when we start having exams with more than one section.
    print "sections of exam: " + str(sections)
    return sections

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
            if section.section_type == 'FB':
                regex = re.compile('[^;]')
                responses[i] = json.loads('"' + regex.sub('',section.questions[str(i+1)]) + '"')
            else:
                responses[i] = json.loads('""')
            #responses[i] = {}
    #print "responses for section: " + str(responses)
    return responses

# Returns a tuple of responses, grader_extras, and scores for the given exam
def get_responses(exam, session):
    responses = []
    sections = Section.objects.filter(exam=exam)

    for i in range(0, len(sections)):
        responses.append(get_responses_for_section(exam, i, session))
    return responses

def get_responses_score_for_section(exam_pk, section_index, session):
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
            section_score = responses_object.score
            responses[i] = json.loads('"' + str(section_score) + '"')
    #print "scores for section: " + str(responses)
    return responses        

#data context is: [({'type': u'essay', 'id': 102, 'questions': [{u'prompt': u'How is your time with the Lord?', u'points': u'2', u'type': u'essay'}], 'instructions': u'write an essay'}, {0: u'I think it was okay'}), ({'type': u'mc', 'id': 103, 'questions': [{u'answer': u'A;B', u'prompt': u'What is life?', u'points': u'1', u'type': u'mc', u'options': u'Eternal;Christ;Dog;Cat;Fish'}, {u'answer': u'A', u'prompt': u'What is living in the Divine Trinity?', u'points': u'1', u'type': u'mc', u'options': u"John 15:4;I don't know;Huh;I think...;another choice"}], 'instructions': u'multiple choice choose up to 2'}, {0: u'1', 1: u'1;2'}), ({'type': u'matching', 'id': 104, 'questions': [{u'answer': u'Gal 2:20', u'prompt': u'I am crucified', u'points': u'1', u'type': u'matching'}, {u'answer': u'Rom 15', u'prompt': u'Hope', u'points': u'1', u'type': u'matching'}], 'instructions': u'match to the best answer'}, {0: u'Gal 2:20', 1: u'Rom'}), ({'type': u'tf', 'id': 105, 'questions': [{u'answer': u'true', u'prompt': u'God is Triune', u'points': u'1', u'type': u'tf'}], 'instructions': u'select true or false'}, {0: u'true'})]
def get_responses_score(exam, session):
    responses_score = []
    sections = Section.objects.filter(exam=exam)
    for i in range(0, len(sections)):
        responses_score.append(get_responses_score_for_section(exam, i, session))
    return responses_score

def get_responses_comments_for_section(exam_pk, section_index, session):
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
            section_comments = responses_object.comments
            responses[i] = json.loads('"' + str(section_comments) + '"')
    #print "comments for section: " + str(responses)
    return responses

def get_responses_comments(exam, session):
    responses_comments = []
    sections = Section.objects.filter(exam=exam)
    for i in range(0, len(sections)):
        responses_comments.append(get_responses_comments_for_section(exam, i, session))
    return responses_comments

def get_edit_exam_context_data(context, exam, training_class):
    questions = get_exam_questions(exam, True)
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
    #P = request.POST
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print "BODY: " + str(body)
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
    print "SECTIONS: " + str(sections)
    section_index = 0
    for section in sections:
        try:
            section_instructions = section['instructions']
            section_questions = section['questions']
            print "section_instructions: " + str(section_instructions)
            print "section_questions: " + str(section_questions)
            question_hstore = {}
            question_count = 0
            section_type = "E"
            for question in section_questions:
                print "******************** QUESTION ********************" + str(question)
                #Avoid saving hidden questions that are blank
                if question['question-prompt'] == '':
                    continue
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
                    for numeral in range(1, 100):
                        choice = 'question-option-' + str(numeral)
                        if choice in question:
                            #every choice in the MC question will go here
                            options += question[choice] + ";"
                        if str(numeral) in question:
                            #every checked choice i.e. the answer to the question will go here
                            answer += str(numeral) + ";"
                    options = options.rstrip(';')
                    answer = answer.rstrip(';')
                    section_type = "MC"
                elif question_type == "matching":
                    answer = question["question-match"]
                    section_type = "M"
                elif question_type == "tf":
                    section_type = "TF"
                    #i.e. id="tf_0" name="true0"
                    true_option = re.findall(r'true[0-9]+', str(question))
                    false_option = re.findall(r'false[0-9]+', str(question))
                    if len(true_option) > 0 and question[true_option[0]] == "on":
                        answer = "true"
                        tf_index = re.findall(r'[0-9]+', true_option[0])[0]
                        qPack['options'] = str(tf_index) + ";" + str(int(tf_index) + 1)
                    elif len(false_option) > 0 and question[false_option[0]] == "on":
                        answer = "false"
                        tf_index = re.findall(r'[0-9]+', false_option[0])[0]
                        qPack['options'] = str(tf_index) + ";" + str(int(tf_index) - 1)
                elif question_type == "fitb":
                    section_type = "FB"
                    for numeral in range(1, 100):
                        answer_text_x = "answer-text-" + str(numeral)
                        if answer_text_x in question:
                            answer += question[answer_text_x] + ";"
                if options != "":
                    qPack['options'] = options
                if answer != "":
                    answer = answer.rstrip(';')
                    qPack['answer'] = answer
                question_hstore[str(question_count+1)] = json.dumps(qPack)
                print "**************QUESTION HSTORE***************" + str(question_hstore)
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
            #if section id is already in existing sections of exam, save over existing section
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

def get_exam_context_data(context, exam, is_available, session, role, include_answers):
    context['role'] = role
    context['exam'] = exam
    if hasattr(session, 'trainee'):
        context['examinee'] = session.trainee

    if not is_available:
        context['exam_available'] = False
        return context

    context['exam_available'] = True
    #print "QUESTIONS AND RESPONES CONTEXT: "
    questions = get_exam_questions(exam, include_answers)
    responses = get_responses(exam, session)
    score_for_responses = get_responses_score(exam, session)
    comments_for_responses = get_responses_comments(exam, session)
    #print "RESPONSES: "
    #print str(responses)
    current_question = 0
    for each in questions:
        questions_in_section = len(each['questions'])

    #print "result of questions: " + str(questions)

    context['data'] = zip(questions, responses, score_for_responses, comments_for_responses)
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
            #print "key: " + str(i) + "; responses: " + str(responses[str(i)])
            responses_hstore[str(i).decode('utf-8')] = json.dumps(responses[str(i)])
        except KeyError:
            responses_hstore[str(i).decode('utf-8')] = json.dumps(str('').decode('utf-8'))
    #print "resulting hstore: " + str(responses_hstore)

    responses_obj.responses = responses_hstore
    #print "responses in saved: " + str(responses_obj.responses)
    responses_obj.save()

def save_grader_scores_and_comments(session, section, responses):
    try:
        responses_obj = Responses.objects.get(session=session, section=section)
    except Responses.DoesNotExist:
        responses_obj = Responses(session=session, section=section, score=0)
    responses_obj.score = responses['score']
    responses_obj.comments = responses['comments']
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
