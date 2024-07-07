from django.test import TestCase
from .models import StickyNote, Post
from django.urls import reverse

class StickyNoteModelTests(TestCase):

    def test_string_representation(self):
        note = StickyNote.objects.create(title="Test Note", content="This is a test.")
        self.assertEqual(str(note), note.title)

class StickyNoteViewTests(TestCase):

    def setUp(self):
        self.note = StickyNote.objects.create(title="Test Note", content="This is a test.")

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertTemplateUsed(response, 'notes/note_detail.html')

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'New note content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(StickyNote.objects.last().title, 'New Note')

    def test_note_update_view(self):
        response = self.client.post(reverse('note_update', args=[self.note.id]), {
            'title': 'Updated Note',
            'content': 'Updated note content'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self):
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse
