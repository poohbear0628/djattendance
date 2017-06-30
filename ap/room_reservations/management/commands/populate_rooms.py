from django.core.management.base import BaseCommand

from rooms import Room

def new_room(rooms=[], access='C',):
    for room in rooms:
        code = room
        u = Room(code=code, name=, floor=, type= , access=, reservable=)
