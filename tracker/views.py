from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from tracker.forms import ParticipantForm
from tracker.models import Participant

def index(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker.index")
    else:
        form = ParticipantForm()

    participants = Participant.objects.all()
    template_data = {}
    template_data['title'] = 'Tracker'
    return render(request, 'tracker/index.html', {'template_data' : template_data, "form" : form, "participants" : participants,},)

def increment(request, participant_id, field):
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == "POST":
        if field == "wins":
            participant.wins += 1
        elif field == "tickets":
            participant.tickets += 1
        elif field == "pisses":
            participant.pisses += 1
        participant.save()
    return redirect("tracker.index")
def decrement(request, participant_id, field):
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == "POST":
        if field == "wins":
            participant.wins -= 1
        elif field == "tickets":
            participant.tickets -= 1
        elif field == "pisses":
            participant.pisses -= 1
        participant.save()
    return redirect("tracker.index")
def remove(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == "POST":
        participant.delete()
    return redirect("tracker.index")

def removeAll(request):
    if request.method == "POST":
        Participant.objects.all().delete()
    return redirect("tracker.index")

def currentWinner(request):
    most_wins_participant = Participant.objects.order_by('-wins').first()
    return JsonResponse({
        'name': most_wins_participant.name,
        'wins': most_wins_participant.wins,
    })
def currentTicketer(request):
    most_ticketer = Participant.objects.order_by('-tickets').first()
    return JsonResponse({
        'name': most_ticketer.name,
        'tickets': most_ticketer.tickets,
    })
def currentPisser(request):
    most_pisser = Participant.objects.order_by('-pisses').first()
    return JsonResponse({
        'name': most_pisser.name,
        'pisses': most_pisser.pisses,
    })