class Room:
    def __init__(self, input_room_name, input_till, input_entry_fee):
        self.name = input_room_name
        self.guests = []
        self.songs = []
        self.room_capacity = 3
        self.till = input_till
        self.entry_fee = input_entry_fee

    def add_guest(self, input_guest):
        self.guests.append(input_guest)

    def remove_guest(self, input_guest):
        self.guests.remove(input_guest)

    def add_song(self, input_song):
        self.songs.append(input_song)

    def check_room_capacity(self, input_guest):
        if len(self.guests) < self.room_capacity:
            return self.add_guest(input_guest)
        else:
            return
        
    def take_payment_for_room_entry_fee(self, input_room, input_guest):
        if self.customer_can_afford_entry(input_room, input_guest):
            self.till += input_room.entry_fee
        
    def customer_can_afford_entry(self, input_guest, input_room):
        return input_guest.sufficient_funds(input_room.entry_fee)

        
    

    