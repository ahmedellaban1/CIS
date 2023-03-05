from .models import Ticket
# from .models import ticket_status
from rest_framework import serializers


class AddTicketAPI(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            # 'status',
            'herafi',
            'description',
            'job_category_id',
            'city_id',
            'city_district',

        ]


class TicketAPIDetails(serializers.ModelSerializer):
    active = serializers.BooleanField(read_only=True)
    # status = serializers.ChoiceField(choices=ticket_status, read_only=True, )
    description = serializers.CharField(read_only=True)
    client_id = serializers.CharField(read_only=True)
    schedule_id = serializers.CharField(read_only=True)
    job_category_id = serializers.CharField(read_only=True)
    city_id = serializers.CharField(read_only=True)
    city_district = serializers.CharField(read_only=True)

    class Meta:
        model = Ticket
        # fields = '__all__'
        exclude = (
            'status',
                   )


class ALLTickets(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TicketStatusAPI(serializers.ModelSerializer):
    active = serializers.BooleanField(read_only=True)
    description = serializers.CharField(read_only=True)
    client_id = serializers.CharField(read_only=True)
    schedule_id = serializers.CharField(read_only=True)
    job_category_id = serializers.CharField(read_only=True)
    city_id = serializers.CharField(read_only=True)
    city_district = serializers.CharField(read_only=True)
    comment = serializers.CharField(read_only=True)
    evaluation = serializers.CharField(read_only=True)
    herafi = serializers.CharField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class ALLTickets(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
