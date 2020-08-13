import cipheydists
import random

class galactic_encode():
    '''
    (Attempts to) encode an input string with the Standard Galactic Alphabet.
    '''
    def __init__(self, text:str):
        self.text = text.lower()
        self.ctext = ""

        imported = dict(cipheydists.get_translate("galactic"))
        self.galactic_dict = {value: key for (key, value) in imported.items()}

    def encode(self):
        for char in self.text:
            if char in self.galactic_dict.keys():
                self.ctext += self.galactic_dict[char]
            else:
                self.ctext += char
        return self.ctext


class XY_encrypt():
    '''
    TODO docstring
    '''
    def __init__(self, text: str, flip: bool = bool(random.randint(0, 1)), randomize:bool = True, key: list = None):
        self.ASCII = list((chr(x).encode() for x in range(128))
        self.text = text.lower()
        self.ctext = ""
        self.flip = flip
        self.randomize = randomize
        self.key = key

    def randomizer(self):
        s = list(self.ctext)
        for i in range(len(s)-1):
            while random.randrange(2):
                s[i] = s[i] + " "
        return "".join(s)

    def to_binary(self):
        return " ".join(f"{ord(i):08b}" for i in self.text)

    def encrypt(self):
        self.ctext = self.to_binary().replace(" ", "")

        if self.key:
            one, two = self.key[0], self.key[1]
        else:
            one, two = random.choice(self.ASCII), random.choice(self.ASCII)

        self.ctext = self.ctext.replace(str(int(self.flip)), one).replace(str(int(not self.flip)), two)
        self.ctext = self.randomizer() if self.randomize == True else self.ctext

        return self.ctext
