class Guest:
    def __init__(self, input_guest_name, input_wallet):
        self.name = input_guest_name
        self.wallet = input_wallet

    def pay_entry_to_room(self, input_room):
        self.wallet -= input_room.entry_fee

    def sufficient_funds(self, input_room):
        return self.wallet >= input_room.entry_fee
    


