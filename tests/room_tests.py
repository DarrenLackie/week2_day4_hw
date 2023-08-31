import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("shania twain", "man i feel like a woman")
        self.song2 = Song("s club 7", "reach")
        self.song3 = Song("steps", "5, 6, 7, 8")
        self.guest1 = Guest("hip hop harry")
        self.guest2 = Guest("rocky richard")
        self.guest3 = Guest("bluesy bob")
        self.guest4 = Guest("indie ian")
        self.guest5 = Guest("poppy poppy")
        self.guest6 = Guest("jazzy jeff")
        self.room = Room("the hydro")

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