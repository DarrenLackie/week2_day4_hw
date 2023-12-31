import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("shania twain", "man i feel like a woman")
        self.song2 = Song("s club 7", "reach")
        self.song3 = Song("steps", "5, 6, 7, 8")
        self.song4 = Song("house of pain", "jump around")
        self.song5 = Song("the blues brothers", "gimme some lovin'")
        self.song6 = Song("george michael", "faith")
        self.guest1 = Guest("hip hop harry", 20, "jump around")
        self.guest2 = Guest("rocky richard", 10, "enter sandman")
        self.guest3 = Guest("bluesy bob", 15, "gimme some lovin'")
        self.guest4 = Guest("indie ian", 50, "mr brightside")
        self.guest5 = Guest("poppy poppy", 17, "5, 6, 7, 8")
        self.guest6 = Guest("jazzy jeff", 25, "man i feel like a woman")
        self.room = Room("the hydro", 100, 10)
        self.room2 = Room("liquid room", 100, 5)

    def test_room_has_same_name(self):
        self.assertEqual("the hydro", self.room.name)

    def test_room_can_add_guest(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(self.guest1, self.room.guests[0])

    def test_room_can_remove_guest(self):
        self.room.add_guest(self.guest1)
        self.room.remove_guest(self.guest1)
        self.assertEqual([], self.room.guests)

    def test_room_can_add_song(self):
        self.room.add_song(self.song1)
        self.assertEqual(self.song1, self.room.songs[0])

    def test_room_capacity(self):
        self.room.check_room_capacity(self.guest1)
        self.room.check_room_capacity(self.guest2)
        self.room.check_room_capacity(self.guest3)
        self.room.check_room_capacity(self.guest4)
        self.assertEqual(self.guest1, self.room.guests[0])
        self.assertEqual(self.guest2, self.room.guests[1])
        self.assertEqual(self.guest3, self.room.guests[2])
        # self.assertEqual(self.guest4, self.room.guests[3]) #fails, too many people in room

    def test_take_payment_for_room(self):
        self.room.take_payment_for_room_entry_fee(self.guest1)
        self.assertEqual(110, self.room.till)