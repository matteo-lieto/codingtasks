from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import StickyNote
from .forms import StickyNoteForm

class NoteListView(ListView):
    model = StickyNote
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = StickyNote
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = StickyNote
    form_class = StickyNoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = StickyNote
    form_class = StickyNoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = StickyNote
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
