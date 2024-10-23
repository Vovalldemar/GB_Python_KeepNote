from models import Note
from storage import Storage
import itertools

class NoteManager:
    def __init__(self):
        self.notes = Storage.load_notes()
        self.next_id = self._get_next_id()

    def _get_next_id(self):
        if not self.notes:
            return 1
        last_id = max(itertools.chain([0], (int(note.note_id) for note in self.notes)))
        return last_id + 1

    def create_note(self, title, body):
        note = Note(
            note_id=self.next_id,
            title=title,
            body=body
        )
        self.notes.append(note)
        self.next_id += 1
        Storage.save_notes(self.notes)

    def list_notes(self):
        return self.notes

    def find_note_by_id(self, note_id):
        return next((note for note in self.notes if note.note_id == int(note_id)), None)

    def update_note(self, note_id, new_title, new_body):
        note = self.find_note_by_id(note_id)
        if note:
            note.title = new_title
            note.body = new_body
            note.timestamp = Note().timestamp
            Storage.save_notes(self.notes)

    def delete_note(self, note_id):
        note = self.find_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            Storage.save_notes(self.notes)
