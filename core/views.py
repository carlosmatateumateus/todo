from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def home(request):

    notes = Note.objects.all()

    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'notes':notes, 'notes_number':notes.count(),'form':form}
    return render(request, 'core/home.html', context)

def active_completed(request, pk):
    
    notes = None
    if (pk == 'active'):
          notes = Note.objects.filter(finish=False)
    else:
          notes = Note.objects.filter(finish=True)

    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'notes':notes, 'notes_number':notes.count(),'form':form}

    return render(request, 'core/home.html', context)
def delete(request, pk):

    note = Note.objects.get(id=pk)
    note.delete()
    
    return redirect('home')

def edit(request, pk):

    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form_edit':form}
    return render(request, 'core/edit.html', context)
