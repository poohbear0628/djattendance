from django.views.generic import TemplateView, DetailView, ListView
from django.views import generic
from .models import Chart, Seat

class ChartCreateView(generic.ListView):
    model = Chart
    template_name = 'seating/chart_create.html'

    # def get_queryset(self):


from rest_framework import viewsets
from .serializers import ChartSerializer, SeatSerializer

class ChartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows charts to be viewed or edited.
    """
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seats to be viewed or edited.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
