class Band:
    def __init__(self, name, members=None):
        self.members = members or []
        self.name = name
        # Use a loop for the play_solos() to iterate over the list

    # Band instance should have play_solos method that asks each member to play a solo, in the order added to band.


    def __str__(self):
        band_strings = [str(band) for band in self.musicians]

    # Check tests to see what repr for band needs to include. This is placeholder for now.
    def __repr__(self):
        return f"Band({self.members}"


    def play_solo(self, solo=""):
        self.solo = solo
        return f""


    # should have a class method to_list which returns a list of previously created Band instances
    def to_list(self):
        pass


# base class

class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self, instrument=""):
        self.instrument = instrument
        return f"{instrument}"

    # Each kind of Musician instance should have a play_solo method that returns string.
    def play_solo(self, solo=""):
        self.solo = solo
        return f""

    def __str__(self):
        pass

    def __repr__(self):
        pass


# derived class
class Guitarist(Musician):

    def __init__(self, name):
        self.solo = None
        self.name = name

    def get_instrument(self, instrument="guitar"):
        self.instrument = instrument
        return f"{instrument}"

    def play_solo(self, solo=""):
        self.solo = solo
        return f"face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"


    def get_instrument(self, instrument="bass"):
        self.instrument = instrument
        return f"{instrument}"


    def play_solo(self, solo=""):
        self.solo = solo
        return f"bom bom buh bom"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def get_instrument(self, instrument="drums"):
        self.instrument = instrument
        return f"{instrument}"


    def play_solo(self, solo=""):
        self.solo = solo
        return f"rattle boom crash"


    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
