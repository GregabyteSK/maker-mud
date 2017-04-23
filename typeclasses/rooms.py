"""
Room

Rooms are simple containers that has no location of their own.

"""


import random
from evennia import DefaultRoom, TICKER_HANDLER
    
ECHOES = ["A saw fills the air with a tooth-chattering wail.",
          "You hear the yelp of a Maker getting their shirt tail stuck in the lathe... again.",
          "Someone tunelessly bangs on the piano keys.",
          "Somewhere, a Phil screeches its plantive cry.",
          "Someone suddenly shouts \"LOUD NOISES\" and turns on the tablesaw.",
]
class Room(DefaultRoom):
    pass

class InsideRoom(DefaultRoom):
    "This room is ticked at regular intervals"        
       
    def at_object_creation(self):
        "called only when the object is first created"
        TICKER_HANDLER.add(60 * 60, self.at_noise_update)

    def at_noise_update(self, *args, **kwargs):
        "ticked at regular intervals"
        echo = random.choice(ECHOES)
        self.msg_contents(echo)
