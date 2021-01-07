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
        self.rotate(offset)
        tmp = ""
        for c in self.rotor:
            tmp += self.alphabet[(self.alphabet.index(c) + offset) % 26]
        self.rotor = tmp

    def reverse(self):
        tmp = ""
        for a in self.alphabet:
            for b in self.rotor:
                if a == b:
                    tmp += self.alphabet[self.rotor.index(b)]
        self.rotor = tmp

    def rotate(self, num = 1):
        for i in range(0, num):
            self.rotor = self.rotor[25:] + self.rotor[0:25]
