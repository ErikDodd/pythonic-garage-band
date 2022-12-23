class Band:
    def __init__(self, name, members=None):
        self.members = members or []
        self.name = name
        # Use a loop for the play_solos() to iterate over the list

    # A Band instance should have a play_solos method that asks each member to play a solo, in the order they were added to band.
    # play_solos():

    def __str__(self):
        band_strings = [str(band) for band in self.musicians]

    # Check tests to see what repr for band needs to include. This is placeholder for now.
    def __repr__(self):
        return f"Band({self.members}"

    # should have a class method to_list which returns a list of previously created Band instances
    def to_list(self):
        pass


# base class
class Musician:
    def __init__(self, name):
        self.name = name

    # Hard-coded guitar. Need to figure out how to get all instruments there
    def get_instrument(self, instrument):
        self.instrument = instrument
        return f"{instrument}"

    def __str__(self):
        pass

    def __repr__(self):
        pass

    # Each kind of Musician instance should have a play_solo method that returns string.

    # play_solo():


# derived class
class Guitarist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    pass

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

# Band (derived class)
# class Nirvana(Band):
# def __int__(self, name="Nirvana"):
# self.name = name
# pass
