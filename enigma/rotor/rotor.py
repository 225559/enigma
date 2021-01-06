class Rotor:
    """Rotor ...
    """

    def __init__(self, num):
        if num == 1:
            self.sub = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        elif num == 2:
            self.sub = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        elif num == 3:
            self.sub = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        else:
            raise ValueError()
