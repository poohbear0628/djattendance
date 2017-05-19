import django_filters

from itertools import chain
from datetime import datetime

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q

from rest_framework import viewsets, filters

from .models import LeaveSlip, IndividualSlip, GroupSlip
from .forms import IndividualSlipForm, GroupSlipForm
from .serializers import IndividualSlipSerializer, IndividualSlipFilter, GroupSlipSerializer, GroupSlipFilter
from accounts.models import Trainee
from rest_framework_bulk import BulkModelViewSet

from aputils.trainee_utils import trainee_from_user

def modify_status(request, classname, status, id):
    if classname == "individual":
        leaveslip = get_object_or_404(IndividualSlip, pk=id)
    if classname == "group":
        leaveslip = get_object_or_404(GroupSlip, pk=id)
    leaveslip.status = status
    leaveslip.save()

    message =  "%s's %s leaveslip was " % (leaveslip.trainee, leaveslip.get_type_display().upper())
    if status == 'A':
        message += "approved."
    if status == 'D':
        message += "denied."
    if status == 'F':
        message += "marked for fellowship."
    messages.add_message(request, messages.SUCCESS, message)

    return redirect('leaveslips:ta-leaveslip-list')


""" API Views """

class IndividualSlipViewSet(BulkModelViewSet):
    queryset = IndividualSlip.objects.all()
    serializer_class = IndividualSlipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = IndividualSlipFilter
    def get_queryset(self):
        trainee = trainee_from_user(self.request.user)
        individualslip=IndividualSlip.objects.filter(trainee=trainee)
        return individualslip
    def allow_bulk_destroy(self, qs, filtered):
        return filtered

        # failsafe- to only delete if qs is filtered.
        # return not all(x in filtered for x in qs)

class GroupSlipViewSet(BulkModelViewSet):
    queryset = GroupSlip.objects.all()
    serializer_class = GroupSlipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupSlipFilter
    def get_queryset(self):
        trainee = trainee_from_user(self.request.user)
        groupslip=GroupSlip.objects.filter(Q(trainees=trainee)).distinct()
        return groupslip
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)

class AllIndividualSlipViewSet(BulkModelViewSet):
    queryset = IndividualSlip.objects.all()
    serializer_class = IndividualSlipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = IndividualSlipFilter
    def allow_bulk_destroy(self, qs, filtered):
        return not all(x in filtered for x in qs)

class AllGroupSlipViewSet(BulkModelViewSet):
    queryset = GroupSlip.objects.all()
    serializer_class = GroupSlipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupSlipFilter
    def allow_bulk_destroy(self, qs, filtered):
        return filtered
        # return not all(x in filtered for x in qs)
