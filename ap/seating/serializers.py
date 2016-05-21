from .models import Chart, Seat
from terms.models import Term
from rest_framework import serializers

class ChartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chart
        fields = ('name', 'desc', 'height', 'width', 'trainees')
    def to_internal_value(self, data):
        internal_value = super(ChartSerializer, self).to_internal_value(data)
        internal_value.update({
            "trainees": data.get("trainees"),
        })
        return internal_value
    def create(self, validated_data):
        # print 'LOOK HERE!!!!!!!'
        # print validated_data
        # validated_data['term'] = Term.current_term()
        new_chart = Chart.objects.create(**validated_data)

        seats = validated_data.get('trainees')
        for x in range(0, validated_data.get('width')):
            for y in range(0, validated_data.get('height')):
                print seats[x][y]

        return new_chart


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ('trainee', 'chart', 'x', 'y')