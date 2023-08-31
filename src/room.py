class Room:
    def __init__(self, input_room_name):
        self.name = input_room_name
        self.guests = []
        self.songs = []

    def add_guest(self, input_guest):
        self.guests.append(input_guest)

    def remove_guest(self, input_guest):
        self.guests.remove(input_guest)

    def add_song(self, input_song):
        self.songs.append(input_song)

    