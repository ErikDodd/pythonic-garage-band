class Band:
    band_instances = []
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []
        Band.band_instances.append(self)


    # Band instance should have play_solos method that asks each member to play a solo, in the order added to band.
    def play_solos(self):
        played_solo = [soloist.play_solo() for soloist in self.members]
        return played_solo


    #def __str__(self):
        #solos_strings = []
        #for solos in self.members:
            #return solos_strings.append(str(solos))



    # Check tests to see what repr for band needs to include. This is placeholder for now.
    def __repr__(self):
        return f"Band({self.members}"



# base class

class Musician:
    def __init__(self, name, solo, instrument):
        self.name = name
        self.solo = solo
        self.instrument = instrument

    def get_instrument(self):
        return f"{self.instrument}"

    # Each kind of Musician instance should have a play_solo method that returns string.
    def play_solo(self):
        return self.solo



# derived class
class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name, solo="face melting guitar solo", instrument="guitar")

    def get_instrument(self):
        return f"{self.instrument}"


    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, solo="bom bom buh bom", instrument="bass")


    def __str__(self):
        return f"My name is {self.name} and I play bass"


    def get_instrument(self):
        return f"{self.instrument}"


    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, solo="rattle boom crash", instrument="drums")


    def __str__(self):
        return f"My name is {self.name} and I play drums"


    def get_instrument(self):
        return f"{self.instrument}"


    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
