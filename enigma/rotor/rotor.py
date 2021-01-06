class Rotor:
    """Rotor ...
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, rotor):
        if rotor == 1:
            self.rotor = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        elif rotor == 2:
            self.rotor = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        elif rotor == 3:
            self.rotor = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        else:
            raise ValueError()

    def ring_setting(self, setting):
        offset = self.alphabet.index(setting)
        self.rotor = self.rotor[26 - offset:] + self.rotor[0:26 - offset]
        tmp = ""
        for c in self.rotor:
            tmp += self.alphabet[(self.alphabet.index(c) + offset) % 26]
        self.rotor = tmp
