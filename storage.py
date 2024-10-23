import csv
import os
from models import Note

class Storage:
    FILE_PATH = 'notes.csv'

    @staticmethod
    def save_notes(notes):
        with open(Storage.FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['note_id', 'title', 'body', 'timestamp'])
            for note in notes:
                writer.writerow([note.note_id, note.title, note.body, note.timestamp])

    @staticmethod
    def load_notes():
        if not os.path.exists(Storage.FILE_PATH):
            return []

        notes = []
        with open(Storage.FILE_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                note = Note.from_dict(row)
                notes.append(note)
        return notes
