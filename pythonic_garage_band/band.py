

class Band():
    def __init__(self, name="unknown", members=None):
        self.name = name
        self.members = members or []

    def play_solos(self):
        solos = [member.play_solo() for member in self.members]
        return solos

    def __str__(self):
        band_members = [str(member) for member in self.members]
        return " ".join(band_members)

    def __repr__(self):
        return f"Band({self.members})"


class Musician():
    def __init__(self, name="unknown", instrument="unknown"):
        self.name = name
        self.instrument = instrument
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


    def get_instrument(self):
        return f"{self.instrument}"



class Guitarist(Musician):
    def __init__(self, name="unknown", instrument="guitar"):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    #"face melting guitar solo"
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name="unknown", instrument="bass"):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name="unknown", instrument="drums"):
        self.name = name
        self.instrument = instrument

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def play_solo(self):
        return "rattle boom crash"

