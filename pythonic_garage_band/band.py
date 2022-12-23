class Band:
    def __init__(self, musicians=None):
        self.musicians = musicians or []


    #def __str__(self):

        pass

# base class
class Musician:
    def __init__(self, name):
        self.name = name
        pass


# derived class
class Guitarist(Musician):
    pass


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass


