import random

from people.people import Fellow, Staff
from rooms.rooms import LivingSpace, Office

class Amity(object):
    """This class holds the system's core functionality"""
    rooms_list = {}
    people_list{}

    def create_room(self, room_name, room_type):
        """Create a new room and adds it to the rooms list"""
        room_type = self.room_type.upper()
        room_name = self.room_name.upper()
        if room_type != "L" or room_type != "O":
            print("Dang!: Invalid room type entered. Use either O or L")
        if room_name == None or room_type == None:
            print("Make sure you enter all details. See help for more")
        if not room_name.isalpha():
            print("Room name can only contain alphabets. Try again")
        if room_name in Amity.rooms_list.keys():
            print("Dang! Name already taken. Enter another")
        if self.room_type == "L":
            new_room = LivingSpace()
            Amity.rooms_list[room_name] = {}
            Amity.rooms_list[room_name]["Type"] = new_room.r_type
            Amity.rooms_list[room_name]["Capacity"] = new_room.capacity
            Amity.rooms_list[room_name]["Members"] = []
        elif self.room_type == "O":
            new_room = Office()
            Amity
