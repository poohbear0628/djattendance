from .models import ExamTemplateDescriptor, ExamTemplateSections, Exam2, ExamResponses

# Returns the section referred to by the args, None if it does not exist
def get_exam_section(exam_template_pk, section_number):
	section_pk = "_".join([str(exam_template_pk), str(section_number)])

	try:
		section = ExamTemplateSections.objects.get(pk=section_pk)
		return section
	except ExamTemplateSections.DoesNotExist:
		return None

# Returns an array containing the interesting data for the given section. None
# returned if the exam is invalid
def get_exam_questions_for_section(exam_template_pk, section_number):
	section = get_exam_section(exam_template_pk, section_number)

	if (section == None):
		return None

	# TODO(hstore)
	return section.questions.split('|')

# Returns an array containing the interesting data.  None is returned if the
# exam is invalid.
def get_exam_questions(exam_template_pk):
	questions = []
	exam_template = ExamTemplateDescriptor.objects.get(pk=exam_template_pk)
	for i in range(1, exam_template.section_count + 1):
		section_questions = get_exam_questions_for_section(exam_template_pk, i)
		if (section_questions != None):
			questions += section_questions
		else:
			return None

		# TODO(verification): We should sanity check that the question numbers
		# per section are vaguely correct whenever we have an exam that has 
		# when we start having exams with more than one section.
	return questions

# Returns a tuple of responses and grader_extras for the exam  for the given
# question range, includes question_start, but not question_end.
def get_response_grader_extras_range(exam_pk, trainee_pk, question_start, 
									 question_end):
	responses = []
	grader_extras = []

	for i in range(question_start, question_end):
		response_key = "_".join([str(exam_pk), str(trainee_pk), str(i)])
		print response_key
		try:
			response_data = ExamResponses.objects.get(pk=response_key)
			responses.append(response_data.response)
			grader_extras.append(response_data.grader_extra)
		except ExamResponses.DoesNotExist:
			responses.append("")
			grader_extras.append("")

	return (responses, grader_extras)

# Returns a tuple of responses and grader_extras for the given exam in the given
# section
def get_response_grader_extras_for_section(exam_template_pk, section_number, 
										   exam_pk, trainee_pk, current_question):
	section = get_exam_section(exam_template_pk, section_number)
	if section == None:
		return None, None

	return get_response_grader_extras_range(exam_pk, trainee_pk, current_question,
											current_question + section.question_count)

# Returns a tuple of responses and grader_extras for the given exam
def get_response_grader_extras(exam_template_pk, exam_pk, trainee_pk):
	exam_template = ExamTemplateDescriptor.objects.get(pk=exam_template_pk)
	current_question = 1
	responses = []
	grader_extras = []

	for i in range(1, exam_template.section_count + 1):
		section_responses, section_grader_extras = \
			get_response_grader_extras_for_section(exam_template_pk, i, exam_pk, 
												   trainee_pk, current_question)

		if (section_responses == None) or (section_grader_extras==None):
			return None, None

		responses += section_responses
		grader_extras += section_grader_extras
		current_question += len(responses)

		# TODO(verification): length of responses should be the same as the 
		# length of grader_extras.  Maybe combine in the section helper fx
		# so that we can also verify against first_question_index and
		# question_count under ExamTemplateSections

	print responses
	print grader_extras
	return (responses, grader_extras)