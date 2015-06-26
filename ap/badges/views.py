from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse,reverse_lazy
from django.shortcuts import render_to_response
from django.db.models import Q
from django.views.generic import ListView
from .models import Badge
from accounts.models import User, Trainee
from terms.models import Term
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .forms import BadgeForm, BadgeUpdateForm, BadgePrintForm
from .printtopdf import render_to_pdf
import xhtml2pdf.pisa as pisa
import datetime

class index(ListView):
    model = Badge
    template_name = "badge_list.html"

def batch(request):
    if request.method == 'POST':
        b = Badge(type='T')
        b.term_created = Term.current_term()
        b.original = request.FILES['file']
        b.avatar = request.FILES['file']
        b.save()
        
        # grab the trainee name. filename in form of:
        # /path/to/Ellis_Armad.jpg or /path/to/Ellis_Armad_1.jpg
        name = b.original.name.split('/')[-1].split('.')[0].split('_')

        try:
            user = User.objects.get(Q(is_active=True), 
                                Q(firstname__exact=name[0]), 
                                Q(lastname__exact=name[1]))
        except User.DoesNotExist:
            print "Error User does not exist"

        if user:
            user.trainee.badge = b
            user.save()
            user.trainee.save()

    return render_to_response('badges/batch.html', context_instance=RequestContext(request))

def badgeprintout(request):
    return render_to_response('badges/print.html', Badge.objects.filter(term_created__exact=Term.current_term()))

def pictureRange(begin, end):
    if begin>end:
        return []

    pictureRangeArray = []
    for num in range(int(begin-end)/8):
        pictureRangeArray = pictureRangeArray.append(begin+num*8)

    return pictureRangeArray

class BadgePrintFrontView(ListView):

    model = Badge

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_template_names(self):
        return ['badges/print.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(Q(term_created__exact=Term.current_term()) & Q(type__exact='T'))
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFrontView, self).get_context_data(**kwargs)

        if 'choice' in self.request.POST:
            context['object_list'] = Badge.objects.filter(id__in=self.request.POST.getlist('choice'))

        return context

class BadgePrintMassFrontView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/print.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(Q(term_created__exact=Term.current_term()) & Q(type__exact='T'))
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintMassFrontView, self).get_context_data(**kwargs)
  
        numTrainees = Trainee.objects.filter().all().count()
        #Signifies the range of pictures to place on the right side
        context['need_bottom_rightside'] = pictureRange(6, numTrainees)
        #Signifies the range of pictures to place on the left side
        context['need_bottom_leftside'] = pictureRange(7, numTrainees)

        return context

class BadgePrintBostonFrontView(ListView):

    model = Badge

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_template_names(self):
        return ['badges/printboston.html']
    
    def get_queryset(self, **kwargs):
        #return Badge.objects.filter(Q(term_created__exact=Term.current_term()) | Q(type__exact='X'))
        return Badge.objects.filter(Q(term_created__exact=Term.current_term()) & Q(type__exact='X'))
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintBostonFrontView, self).get_context_data(**kwargs)
        return context

class BadgePrintMassBostonFrontView(ListView):

    model = Badge

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_template_names(self):
        return ['badges/printmassboston.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(Q(term_created__exact=Term.current_term()) & Q(type__exact='X'))
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintMassBostonFrontView, self).get_context_data(**kwargs)
        return context


class BadgePrintAllInclusiveFrontView(ListView):

    model = Badge

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_template_names(self):
        return ['badges/printallinclusive.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintAllInclusiveFrontView, self).get_context_data(**kwargs)
  
        numTrainees = Trainee.objects.filter().all().count()
        #Signifies the range of pictures to place on the right side
        context['need_bottom_rightside'] = pictureRange(6, numTrainees)
        #Signifies the range of pictures to place on the left side
        context['need_bottom_leftside'] = pictureRange(7, numTrainees)

        return context

class BadgePrintBackView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printback.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintBackView, self).get_context_data(**kwargs)
        return context

class BadgePrintGeneralBackView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printgeneralback.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintGeneralBackView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgePrintFacebookView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printfbpdf.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    # Praise the Lord!!!!!!!
    def get_context_data(self, **kwargs):
        context = super(BadgePrintFacebookView, self).get_context_data(**kwargs)

        context['current_term'] = Term().current_term
        termObject = Term().current_term()

        if Term().current_term().season == "Spring":
            yearone = termObject.year
            yeartwo = termObject.year - 1
            yearthree = termObject.year - 1
            yearfour = termObject.year - 2
            firstseason  = 'Spring'
            secondseason = 'Fall'
            thirdseason  = 'Spring'
            fourthseason = 'Fall'

        else:
            yearone = Term().current_term().year
            yeartwo = Term().current_term().year
            yearthree = Term().current_term().year - 1
            yearfour = Term().current_term().year -1
            firstseason  = 'Fall'
            secondseason = 'Spring'
            thirdseason  = 'Fall'
            fourthseason = 'Spring'

        context['first_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearone, season=firstseason), gender__exact='M') & Q(type__exact='T'))
        context['first_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearone, season=firstseason), gender__exact='F') & Q(type__exact='T'))

        context['second_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yeartwo, season=secondseason), gender__exact='M') & Q(type__exact='T'))
        context['second_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yeartwo, season=secondseason), gender__exact='F') & Q(type__exact='T'))

        context['third_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearthree, season=thirdseason), gender__exact='M') & Q(type__exact='T'))
        context['third_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearthree, season=thirdseason), gender__exact='F') & Q(type__exact='T'))

        context['fourth_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearfour, season=fourthseason), gender__exact='M') & Q(type__exact='T'))
        context['fourth_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=yearfour, season=fourthseason), gender__exact='F') & Q(type__exact='T'))

        return context

class BadgePrintBostonFacebookView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printbostonfbpdf.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(Q(term_created__exact=Term.current_term()) & Q(type__exact='X'))

    # Praise the Lord!!!!!!!
    def get_context_data(self, **kwargs):
        context = super(BadgePrintBostonFacebookView, self).get_context_data(**kwargs)

        termObject = Term().current_term()

        if Term().current_term().season == "Spring":
            bostonone = termObject.year
            bostontwo = termObject.year - 1
            firstseason  = 'Spring'
            secondseason = 'Fall'

        else:
            bostonone = Term().current_term().year
            bostontwo = Term().current_term().year
            firstseason  = 'Fall'
            secondseason = 'Spring'


        context['first_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=bostonone, season=firstseason), gender__exact='M') & Q(type__exact='X'))
        context['first_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=bostonone, season=firstseason), gender__exact='F') & Q(type__exact='X'))

        context['second_term_brothers'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=bostontwo, season=secondseason), gender__exact='M') & Q(type__exact='X'))
        context['second_term_sisters'] = Badge.objects.filter(Q(term_created__exact=Term.objects.get(year=bostontwo, season=secondseason), gender__exact='F') & Q(type__exact='X'))

        context['current_term'] = Term().current_term

        return context

class BadgePrintStaffView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printstaff.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintStaffView, self).get_context_data(**kwargs)
        return context

class BadgePrintShorttermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printshortterm.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintShorttermView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgeTermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/term.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeTermView, self).get_context_data(**kwargs)
        return context

class BadgeXBTermView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/xbterm.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeXBTermView, self).get_context_data(**kwargs)
        return context

class BadgeStaffView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/staff.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgeStaffView, self).get_context_data(**kwargs)
        return context

class BadgeListView(ListView):
    model = Badge
    queryset = Badge.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BadgeListView, self).get_context_data(**kwargs)
        return context

class BadgeCreateView(CreateView):
    form_class = BadgeForm
    model = Badge
    success_url='/badges/'

    def get_context_data(self, **kwargs):
        context = super(BadgeCreateView, self).get_context_data(**kwargs)
        return context

class BadgeUpdateView(UpdateView):
    model = Badge
    template_name = 'badges/badge_detail.html'
    form_class = BadgeUpdateForm
    success_url='/badges/'
    
    def get_context_data(self, **kwargs):
        context = super(BadgeUpdateView, self).get_context_data(**kwargs)
        return context

class BadgeDeleteView(DeleteView):
    model = Badge
    template_name = 'badges/badge_delete.html'
    success_url='/badges/'

class BadgePrintUsherView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printusher.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintUsherView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

class BadgePrintTempView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printtemp.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintTempView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(50)]
        return context

class BadgePrintVisitorView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printvisitor.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintVisitorView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(50)]
        return context

class BadgePrintOfficeView(ListView):

    model = Badge

    def get_template_names(self):
        return ['badges/printoffice.html']
    
    def get_queryset(self, **kwargs):
        return Badge.objects.filter(term_created__exact=Term.current_term())
    
    def get_context_data(self, **kwargs):
        context = super(BadgePrintOfficeView, self).get_context_data(**kwargs)
        context['loop_times'] = [i+1 for i in range(8)]
        return context

def genpdf(request):
    return render_to_response('badges/print.html')






