from django.shortcuts import render
from django.http import HttpResponse

from .utils import av_dir

def index(request):
  return HttpResponse(av_dir())
