class Guest:
    def __init__(self, input_guest_name, input_wallet, input_favourite_song):
        self.name = input_guest_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_entry_to_room(self, input_room):
        self.wallet -= input_room.entry_fee

    def sufficient_funds(self, input_room):
        return self.wallet >= input_room.entry_fee
    
    def is_favourite_song_on_room_playlist(self, input_room):
        for song in input_room.songs


