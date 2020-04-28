# Class p(H|E)
class HE:
    nameH = ""
    nameE = ""
    value = 0

    def __init__(self, nameh, namee, value):
        self.nameE = namee
        self.nameH = nameh
        self.value = value


# class p(E|H)
class EH:
    nameH = ""
    nameE = ""
    value = 0

    def __init__(self, nameh, namee, value):
        self.nameE = namee
        self.nameH = nameh
        self.value = value


# class p(H)
class H:
    def __init__(self, nameH, value):
        self.nameH = nameH
        self.value = value


# class hasil
class Hasil:
    def __init__(self, nameH, value):
        self.nameH = nameH
        self.value = value
