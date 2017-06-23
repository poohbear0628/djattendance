from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .utils import av_dir
from .models import AVFile
from terms.models import Term

class AVHome(generic.ListView):
  model = AVFile
