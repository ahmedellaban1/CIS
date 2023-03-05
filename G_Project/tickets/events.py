from accounts.models import HerafiInformation  # type:ignore
from .models import Ticket
from datetime import datetime

def views_requests_event(herafi_id):
    try:
        instance = HerafiInformation.objects.get(id=herafi_id)
        views = int(instance.views)+1
        requests = int(instance.requests)+1
        instance.views = views
        instance.requests = requests
        instance.save()
    except:
        print('')


def decrement_requests(herafi_id):
    try:
        instance = HerafiInformation.objects.get(id=herafi_id)
        requests = int(instance.requests)-1
        instance.requests = requests
        instance.save()
    except:
        print('')


def rating(herafi_id, client_rate):
    print(f'{herafi_id}', f'{client_rate}')
    try:
        instance = HerafiInformation.objects.get(id=herafi_id)
        people_rated = int(instance.people_rated)
        people_rated += 1
        new_rate = float(int(int(instance.stars)+client_rate) / int(people_rated*5))
        instance.people_rated = people_rated
        instance.stars += client_rate
        instance.percentage_ratings = (new_rate * 100)
        instance.save()
        print('done')
    except:
        print('error')


def check_herafi_ticket_expiry(herafi_id):
    tickets = Ticket.objects.filter(herafi=herafi_id, status='pending')
    date = datetime.today().strftime('%Y-%m-%d')
    date = date.split('-')
    for i in tickets:
        i_date = str(i.date).split('-')
        print(i_date)
        print('___________')
        print(date)
        if i_date[-1] != date[-1] and i_date[1] == date[1]:
            days = int(i_date[-1])-int(date[-1])
            if days >= 7:
                i.status = 'expired'
                decrement_requests(herafi_id=herafi_id)
        elif i_date[-1] == date[-1] and i_date[1] != date[1]:
            i.status = 'expired'
            decrement_requests(herafi_id=herafi_id)
        elif i_date[-1] != date[-1] and i_date[1] != date[1]:
            month = int(i_date) - int(date[1])
            if month > 1:
                i.status = 'expired'
                decrement_requests(herafi_id=herafi_id)
            elif month == 1 and int(date[1]) != 2 and int(i_date[1]) != 2:
                days = int(30 - int(date[-1])) + int(30 - int(i_date[-1]))
                if days > 7:
                    i.status = 'expired'
                    decrement_requests(herafi_id=herafi_id)
            elif month == 1 and int(date[1]) == 2 and int(i_date[1]) == 2:
                if type(int(date[0])/4) != type(int(1)):
                    days = int(28 - int(date[-1])) + int(28 - int(i_date[-1]))
                    if days > 7:
                        i.status = 'expired'
                        decrement_requests(herafi_id=herafi_id)
                elif type(int(date[0])/4) == type(int(1)):
                    days = int(29 - int(date[-1])) + int(29 - int(i_date[-1]))
                    if days > 7:
                        i.status = 'expired'
        else:
            print('done')


def check_client_ticket_expiry(client_id):
    tickets = Ticket.objects.filter(client_id=client_id, status='pending')
    date = datetime.today().strftime('%Y-%m-%d')
    date = date.split('-')
    for i in tickets:
        i_date = str(i.date).split('-')
        print(i_date)
        print('___________')
        print(date)
        if i_date[-1] != date[-1] and i_date[1] == date[1]:
            days = int(i_date[-1])-int(date[-1])
            if days >= 7:
                i.status = 'expired'
                decrement_requests(herafi_id=i.herafi.id)
        elif i_date[-1] == date[-1] and i_date[1] != date[1]:
            i.status = 'expired'
        elif i_date[-1] != date[-1] and i_date[1] != date[1]:
            month = int(i_date) - int(date[1])
            if month > 1:
                i.status = 'expired'
                decrement_requests(herafi_id=i.herafi.id)
            elif month == 1 and int(date[1]) != 2 and int(i_date[1]) != 2:
                days = int(30 - int(date[-1])) + int(30 - int(i_date[-1]))
                if days > 7:
                    i.status = 'expired'
                    decrement_requests(herafi_id=i.herafi.id)
            elif month == 1 and int(date[1]) == 2 and int(i_date[1]) == 2:

                if type(int(date[0])/4) != type(int(1)):
                    days = int(28 - int(date[-1])) + int(28 - int(i_date[-1]))
                    if days > 7:
                        i.status = 'expired'
                        decrement_requests(herafi_id=i.herafi.id)
                elif type(int(date[0])/4) == type(int(1)):
                    days = int(29 - int(date[-1])) + int(29 - int(i_date[-1]))
                    if days > 7:
                        i.status = 'expired'
                        decrement_requests(herafi_id=i.herafi.id)

        else:
            print('done')

