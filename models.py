import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Note(
            note_id=data['note_id'],
            title=data['title'],
            body=data['body'],
            timestamp=data['timestamp']
        )
