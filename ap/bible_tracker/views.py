from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
#from django.views.decorators.csrf import csrf_exempt

from terms.models import Term
from .models import BibleReading, Trainee
from verse_parse.bible_re import *
import json

def changeWeek(request):
    myUser = request.user;
    if request.is_ajax():
        week_id = request.POST['week'] 
        current_term = Term.current_term()
        term_id = current_term.id
        term_week_code = str(term_id) + "_" + str(week_id) 
        try:
            trainee_weekly_reading = BibleReading.objects.get(trainee=myUser.trainee).weeklyReadingStatus[term_week_code]
            json_weekly_reading = json.loads(trainee_weekly_reading)
            weekly_status = str(json_weekly_reading['status'])
        except:
            weekly_status="_______"
        return HttpResponse(weekly_status)

def updateStatus(request):
    myUser = request.user;
    if request.is_ajax():
        day_id = request.POST['day'] 
        week_id = request.POST['week_id'] 

        print "day:" + day_id
        print "week:" + week_id

        status = request.POST['status']
        current_term = Term.current_term()
        term_id = current_term.id
        term_week_code = str(term_id) + "_" + str(week_id) 
        
        try:
            trainee_bible_reading = BibleReading.objects.get(trainee=myUser.trainee)
        except:
            trainee_bible_reading = BibleReading(trainee=myUser.trainee, weeklyReading={term_week_code:"{\"status\": \"_______\", \"finalized\": \"N\"}"}, booksRead={} ) 

        if term_week_code not in trainee_bible_reading.weeklyReadingStatus: 
            trainee_bible_reading.weeklyReadingStatus[term_week_code]="{\"status\": \"_______\", \"finalized\": \"N\"}"

        trainee_weekly_reading = trainee_bible_reading.weeklyReadingStatus[term_week_code]
        json_weekly_reading = json.loads(trainee_weekly_reading)
        weekly_status = list(json_weekly_reading['status'])
        weekly_status[int(day_id)]=status
        json_weekly_reading['status']=''.join(weekly_status)
        hstore_weekly_reading = json.dumps(json_weekly_reading)
        trainee_bible_reading.weeklyReadingStatus[term_week_code] = hstore_weekly_reading
        trainee_bible_reading.save()

        return HttpResponse(weekly_status)


def index(request):
    myUser = request.user;
    #AJAX for first-year and second-year bible reading 
    if request.is_ajax():
        try:
            #Setup
            isChecked = request.POST['checked']     
            myYear = request.POST['year']

            trainee_bible_reading = BibleReading.objects.get(trainee = myUser.trainee)
            book_code = request.POST['year'] + "_" + request.POST['book']

            #If checked, adds book to the database
            if isChecked == "true":
                trainee_bible_reading.booksRead[book_code] = 'Y'
                trainee_bible_reading.save()
                
            #If not checked, deletes book from the database
            else:
                del trainee_bible_reading.booksRead[book_code]
                trainee_bible_reading.save()
            
            #Calculates how much the progress bar changes for both first-year and second-year bible reading 
            user_checked_list = BibleReading.objects.get(trainee = myUser.trainee).booksRead
            bible_books = testaments['ot'] + testaments['nt']
            bible_books_list = [book[0] for book in bible_books]

            if( myYear == "1" ):
                first_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('1_')]
                first_year_progress = 0;
                for checked_book in first_year_checked_list:
                    first_year_progress = first_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])
                first_year_progress = int(float(first_year_progress)/31102.0 * 100)
                return HttpResponse(str(first_year_progress))
            else:
                second_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('2_')]
                second_year_progress = 0;
                for checked_book in second_year_checked_list:
                    second_year_progress = second_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])
                second_year_progress = int(float(second_year_progress)/7957.0 * 100);
                return HttpResponse(str(second_year_progress))
        except:
            selected_book = 0
    else:
        selected_book = 0

    #Default for Daily Bible Reading
    current_term = Term.current_term()
    term_id=current_term.id
    base = current_term.start
    start_date = current_term.start.strftime('%Y%m%d')
   
    weeks = current_term.length
    week = 0
    date_list = []
    weeks_list ={}
    while week < weeks:
        date_list = [(base + datetime.timedelta(days=x)).strftime("%a %b %d") for x in range(0, 7)]
        base = base + datetime.timedelta(days=7)
        weeks_list[week]=date_list
        week += 1

    #Default for First-year and Second-year bible reading
    bible_books=testaments['ot']+testaments['nt']
    bible_books_list = [book[0] for book in bible_books]

    try:
        user_checked_list = BibleReading.objects.get(trainee=myUser.trainee).booksRead
    except:
        user_checked_list={}

    first_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('1_')]
    second_year_checked_list = [int(book_code.split("_")[1]) for book_code in user_checked_list.keys() if book_code.startswith('2_')]
    
    first_year_progress = 0;
    for checked_book in first_year_checked_list:
        first_year_progress = first_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])
    first_year_progress = int(float(first_year_progress)/31102.0 * 100)

    second_year_progress = 0;
    for checked_book in second_year_checked_list:
        second_year_progress = second_year_progress + sum([int(chapter_verse_count) for chapter_verse_count in bible_books[checked_book][3]])
    second_year_progress = int(float(second_year_progress)/7957.0 * 100)
    
    # first_year_is_complete = first_year_checked_list.count();
    # year = int((myUser.trainee.current_term+1)/2)

    current_date = datetime.date.today()
    current_week = Term.reverse_date(current_term, current_date)[0]
    term_week_code = str(term_id) + "_" + str(current_week) 

    try:
        weekly_reading = BibleReading.objects.get(trainee=myUser.trainee).weeklyReadingStatus[term_week_code]
        json_weekly_reading = json.loads(weekly_reading)
        weekly_status = list(json_weekly_reading['status'])
        print weekly_status
    except:
        weekly_status="_______"

    #Send data to the template!!!
    template = loader.get_template('bible_tracker/index.html')
    context = RequestContext(request, {
        'bible_books_list': bible_books_list,
        'first_year_checked_list': first_year_checked_list,
        'second_year_checked_list': second_year_checked_list,
        # 'first_year_is_complete': first_year_is_complete,
        # 'year': year,
        'first_year_progress': first_year_progress,
        'second_year_progress': second_year_progress,
        'weekly_status': weekly_status,
        'weeks_list': weeks_list,
        'current_week':current_week,
        'start_date':start_date,
    })
    return HttpResponse(template.render(context))

import datetime

# def get_current_time(request):
#   # Create a 'context' dictionary,
#   # populate it with the current time
#   # and return it
#   context = {}
#   context['current_time'] = datetime.datetime.now()
#   return context
