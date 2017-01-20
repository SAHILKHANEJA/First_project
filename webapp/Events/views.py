from django.shortcuts import get_object_or_404, render
from .models import Event ,Ticket
from .forms import EventForm , TicketForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, \
    require_GET, require_POST
from django.http import HttpResponse, JsonResponse, Http404

# Create your views here.
@csrf_exempt
def events(request):
    return render(request , 'Events/eventspage.html')

@csrf_exempt
def addevent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save_event()
        data = {}
        data['event_title'] = event.event_title
        data['event_date'] = event.event_date
        return JsonResponse(data=data,safe=False)


@require_GET
def fetchEvents(requests):
    data =[]
    event_objects = Event.objects.all()
    for event_object in event_objects:
        data.append({"event_id":event_object.id,"event_title":event_object.event_title,"event_date":event_object.event_date})
    return JsonResponse(data = data,safe=False) 

@require_GET
def fetch_event_tickets(request,event_id):
    data = []
    event = Event.objects.get(pk=event_id)
    tickets = event.tickets.all()
    for ticket in tickets:
        data.append({"ticket_id":ticket.id,"ticket_title":ticket.ticket_title,"ticket_starts":ticket.start_date,"ticket_ends":ticket.last_date})
    return JsonResponse(data = data)

@csrf_exempt
def addTicket(request,event_id):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save_ticket(event_id)
        data = {}
        data['ticket_title'] = ticket.ticket_title
        data['start_date'] = ticket.start_date
        data['last_date'] = ticket.last_date
        return JsonResponse(data=data)

@csrf_exempt
def tickets(request,event_id):
    return render(request,'Events/ticketspage.html')
