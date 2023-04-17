class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class NoteApp:
    def __init__(self):
        self.notes = []
    
    def add_note(self, note):
        self.notes.append(note)
    
    def remove_note(self, note):
        self.notes.remove(note)
    
    def display_notes(self):
        for note in self.notes:
            print(note.title)


note_app = NoteApp()

while True:
    print("1. Add note")
    print("2. Remove note")
    print("3. Display notes")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note = Note(title, content)
        note_app.add_note(note)
    elif choice == "2":
        title = input("Enter note title: ")
        for note in note_app.notes:
            if note.title == title:
                note_app.remove_note(note)
                break
    elif choice == "3":
        note_app.display_notes()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
