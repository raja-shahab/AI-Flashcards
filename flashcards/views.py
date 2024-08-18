from .models import Flashcard
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == 'POST':
        front = request.POST['front']
        back = request.POST['back']
        Flashcard.objects.create(front=front, back=back)
        return redirect('index')

    flashcards = Flashcard.objects.all()

    context = {
        'flashcards': flashcards
    }
    return render(request, 'flashcards/index.html', context)


def home(request):
    return render(request, 'templates/home.html')
