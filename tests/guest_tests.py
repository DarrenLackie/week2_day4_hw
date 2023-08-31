import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest = Guest("hip hop harry", 20, "jump around")
        self.room = Room("the hydro", 100, 5)

    def test_amount_in_wallet(self,):
        self.assertEqual(20, self.guest.wallet)

    def test_guest_has_name(self):
        self.assertEqual("hip hop harry", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("jump around", self.guest.favourite_song)

    def test_entry_fee_payment(self):
        self.guest.pay_entry_to_room(self.room)
        self.assertEqual(15, self.guest.wallet)

    def test_customer_can_afford_entry__true_if_can(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.room))

    def test_favourite_song_on_room_playlist(self):
        self.guest.is_favourite_song_on_room_playlist(self.room)