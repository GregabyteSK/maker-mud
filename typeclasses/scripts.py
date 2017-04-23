"""
Example script for testing. This adds a simple timer that has your
character make observations and notices at irregular intervals.

To test, use
  @script me = tutorial_examples.bodyfunctions.BodyFunctions

The script will only send messages to the object it is stored on, so
make sure to put it on yourself or you won't see any messages!

"""
import random
from world.maker import models
from evennia import DefaultScript

class ACAir(DefaultScript):
    """
    This class defines the script itself
    """

    def at_script_creation(self):
        self.key = "ac_air"
        self.desc = "Adds random air events to the AC unit"
        self.interval = 10  # seconds
        #self.repeats = 5  # repeat only a certain number of times
        self.start_delay = True  # wait self.interval until first call
        #self.persistent = True

    def at_repeat(self):
        """
        This gets called every self.interval seconds. We make
        a random check here so as to only return 33% of the time.
        """

        if random.random() < 0.5:
            # no message this time
            return
        rand = random.random()
        # return a random message
        if rand < 0.5:
            string = "You get randomly blasted by freezing air.  Half of the people in the room complain about the temperature."
        elif rand < 0.5:
            string = "You get randomly blasted by hot air.  Half of the people in the room complain about the temperature."

        # echo the message to the object
        self.location.msg(string)

class BackgroundNoise(DefaultScript):
    def at_script_creation(self):
        self.key = "background_noise"
        self.description = "Adds random noise events"
        self.interval = 60
        self.start_delay = False

    def at_repeat(self):
#        noises = ["A saw fills the air with a tooth-chattering wail.",
#                  "You hear the yelp of a Maker getting their shirt tail stuck in the lathe... again.",
#                  "Someone tunelessly bangs on the piano keys.",
#                  "Somewhere, a Phil screeches its plantive cry.",
#                  "Someone suddenly shouts \"LOUD NOISES\" and turns on the tablesaw.",
#        ]
        noises = models.Noise.objects.all()
        noise = random.choice(noises)
        if noise:
            self.obj.msg_contents(noise)
