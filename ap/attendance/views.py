from itertools import chain

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from .models import Roll
from .serializers import RollSerializer
from schedules.serializers import EventSerializer
from leaveslips.serializers import IndividualSlipSerializer
from accounts.serializers import TraineeSerializer
from schedules.models import Schedule, Event
from leaveslips.models import IndividualSlip, GroupSlip
from terms.models import Term
from accounts.models import User
from leaveslips.models import IndividualSlip, IndividualSlipForm
from react import jsx
from templatetags import jsonify
from rest_framework.renderers import JSONRenderer
from rest_framework_bulk import mixins, ListBulkCreateUpdateDestroyAPIView



class AttendancePersonal(TemplateView):
    template_name = 'attendance/attendance_react.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        #jsx.transform('static/js/react/attendance/calendar.jsx', 'static/js/react/attendance/calendar.js')

        listJSONRenderer = JSONRenderer()

        context = super(AttendancePersonal, self).get_context_data(**kwargs)
        context['trainee'] = self.request.user.trainee
        context['trainee_bb'] = listJSONRenderer.render(TraineeSerializer(context['trainee']).data)

        print 'current term', Term.current_term()
        context['schedule'] = Schedule.objects.filter(term=Term.current_term()).get(trainee=self.request.user.trainee)
        context['events_bb'] = listJSONRenderer.render(EventSerializer(context['schedule'].events.all(), many=True).data)
        context['attendance'] = Roll.objects.filter(trainee=self.request.user.trainee).filter(event__term=Term.current_term())
        context['attendance_bb'] = listJSONRenderer.render(RollSerializer(context['attendance'], many=True).data)
        context['leaveslipform'] = IndividualSlipForm()
        print 'trainee', self.request.user.trainee, IndividualSlip.objects.filter(trainee=self.request.user.trainee), IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())
        context['leaveslips'] = IndividualSlip.objects.filter(trainee=self.request.user.trainee).filter(events__term=Term.current_term())
        context['groupslips'] = GroupSlip.objects.filter(trainee=self.request.user.trainee).filter(start__gte=Term.current_term().start).filter(end__lte=Term.current_term().end)
        print 'slips', context['leaveslips']
        context['leaveslips_bb'] = listJSONRenderer.render(IndividualSlipSerializer(context['leaveslips'], many=True).data)
        return context



class RollViewSet(mixins.BulkCreateModelMixin, mixins.BulkUpdateModelMixin, viewsets.ModelViewSet):
    queryset = Roll.objects.all()
    model = Roll
    # serializer_class = RollSerializer