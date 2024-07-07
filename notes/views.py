from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm

def note_list(request):
    notes = StickyNote.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_new(request):
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = StickyNoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = StickyNoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect('note_list')
