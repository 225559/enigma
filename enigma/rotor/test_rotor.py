import unittest
import rotor

class TestRotor(unittest.TestCase):
    """TestRotor ...
    """

    def test_init(self):
        tt = [
            {"rotor" : 1, "expected" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ"},
            {"rotor" : 2, "expected" : "AJDKSIRUXBLHWTMCQGZNPYFVOE"},
            {"rotor" : 3, "expected" : "BDFHJLCPRTXVZNYEIWGAKMUSQO"},
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["rotor"])
            self.assertEqual(tc["expected"], rtor.rotor)


    # Example (Rotor 3 ring setting):
    #
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # BDFHJLCPRTXVZNYEIWGAKMUSQO (Rotor III - Ring setting A)
    #
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # PCEGIKMDQSUYWAOZFJXHBLNVTR (Rotor III - Ring setting B)
    #
    #
    #  Ring setting H    Ring setting G    Ring setting F     Ring setting E     Ring setting D     Ring setting C     Ring setting B     Ring setting A
    #    ---------         ---------         ---------          ---------          ---------          ---------          ---------          ---------
    #    Z       Z         Z       Z         Z    ---Z          Z       Z          Z       Z          Z       Z          Z       Z          Z       Z
    #    Y       Y         Y       Y         Y   /   Y          Y    ---Y          Y       Y          Y       Y          Y       Y          Y       Y
    #    X       X         X       X         X   |   X          X   /   X          X    ---X          X       X          X       X          X       X
    #    W       W         W       W         W   |   W          W   |   W          W   /   W          W     --W          W       W          W       W
    #    V       V         V       V         V   |   V          V   |   V          V   |   V          V   /   V          V    ---V          V       V
    #    U       U         U       U         U   |   U          U   |   U          U   |   U          U   |   U          U   /   U          U    ---U
    #    T       T         T       T         T   |   T          T   |   T          T   |   T          T   |   T          T   |   T          T   /   T
    #    S       S         S       S         S   |   S          S   |   S          S   |   S          S   |   S          S   |   S          S   |   S
    #    R---    R         R       R         R   |   R          R   |   R          R   |   R          R   |   R          R   |   R          R   |   R
    #    Q   \   Q         Q---    Q         Q   /   Q          Q   |   Q          Q   |   Q          Q   |   Q          Q   |   Q          Q   |   Q
    #    P   |   P         P   \   P         P---    P          P   /   P          P   |   P          P   |   P          P   |   P          P   |   P
    #    O   |   O         O   |   O         O       O          O---    O          O   /   O          O   |   O          O   |   O          O   |   O
    #    N   |   N         N   |   N         N       N          N       N          N---    N          N   /   N          N   |   N          N   |   N
    #    M   |   M         M   |   M         M       M          M       M          M       M          M---    M          M   /   M          M   |   M
    #    L   |   L         L   |   L         L       L          L       L          L       L          L       L          L---    L          L   /   L
    #    K   |   K         K   |   K         K       K          K       K          K       K          K       K          K       K          K---    K
    #    J   |   J         J   |   J         J       J          J       J          J       J          J       J          J       J          J       J
    #    I   |   I         I   |   I         I       I          I       I          I       I          I       I          I       I          I       I
    #    H   |   H         H   |   H         H       H          H       H          H       H          H       H          H       H          H       H
    #    G   |   G         G   |   G         G       G          G       G          G       G          G       G          G       G          G       G
    #    F   |   F         F   |   F         F       F          F       F          F       F          F       F          F       F          F       F
    #    E   |   E         E   |   E         E       E          E       E          E       E          E       E          E       E          E       E
    #    D   |   D         D   |   D         D       D          D       D          D       D          D       D          D       D          D       D
    #    C   \   C         C   |   C         C       C          C       C          C       C          C       C          C       C          C       C
    #    B    ---B         B   \   B         B       B          B       B          B       B          B       B          B       B          B       B
    # == A       A ==   == A    ---A ==   == A       A ==    == A       A ==    == A       A ==    == A       A ==    == A       A ==    == A       A == Ring Position
    #    ---------         ---------         ---------          ---------          ---------          ---------          ---------          ---------
    def test_ring_setting(self):
        tt = [
            # Test all ring settings for rotor I
            {"rotor" : 1, "ring_setting" : 'A', "expected" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ"},
            {"rotor" : 1, "ring_setting" : 'B', "expected" : "KFLNGMHERWAOUPXZIYVTQBJCSD"},
            {"rotor" : 1, "ring_setting" : 'C', "expected" : "ELGMOHNIFSXBPVQYAJZWURCKDT"},
            {"rotor" : 1, "ring_setting" : 'D', "expected" : "UFMHNPIOJGTYCQWRZBKAXVSDLE"},
            {"rotor" : 1, "ring_setting" : 'E', "expected" : "FVGNIOQJPKHUZDRXSACLBYWTEM"},
            {"rotor" : 1, "ring_setting" : 'F', "expected" : "NGWHOJPRKQLIVAESYTBDMCZXUF"},
            {"rotor" : 1, "ring_setting" : 'G', "expected" : "GOHXIPKQSLRMJWBFTZUCENDAYV"},
            {"rotor" : 1, "ring_setting" : 'H', "expected" : "WHPIYJQLRTMSNKXCGUAVDFOEBZ"},
            {"rotor" : 1, "ring_setting" : 'I', "expected" : "AXIQJZKRMSUNTOLYDHVBWEGPFC"},
            {"rotor" : 1, "ring_setting" : 'J', "expected" : "DBYJRKALSNTVOUPMZEIWCXFHQG"},
            {"rotor" : 1, "ring_setting" : 'K', "expected" : "HECZKSLBMTOUWPVQNAFJXDYGIR"},
            {"rotor" : 1, "ring_setting" : 'L', "expected" : "SIFDALTMCNUPVXQWROBGKYEZHJ"},
            {"rotor" : 1, "ring_setting" : 'M', "expected" : "KTJGEBMUNDOVQWYRXSPCHLZFAI"},
            {"rotor" : 1, "ring_setting" : 'N', "expected" : "JLUKHFCNVOEPWRXZSYTQDIMAGB"},
            {"rotor" : 1, "ring_setting" : 'O', "expected" : "CKMVLIGDOWPFQXSYATZUREJNBH"},
            {"rotor" : 1, "ring_setting" : 'P', "expected" : "IDLNWMJHEPXQGRYTZBUAVSFKOC"},
            {"rotor" : 1, "ring_setting" : 'Q', "expected" : "DJEMOXNKIFQYRHSZUACVBWTGLP"},
            {"rotor" : 1, "ring_setting" : 'R', "expected" : "QEKFNPYOLJGRZSITAVBDWCXUHM"},
            {"rotor" : 1, "ring_setting" : 'S', "expected" : "NRFLGOQZPMKHSATJUBWCEXDYVI"},
            {"rotor" : 1, "ring_setting" : 'T', "expected" : "JOSGMHPRAQNLITBUKVCXDFYEZW"},
            {"rotor" : 1, "ring_setting" : 'U', "expected" : "XKPTHNIQSBROMJUCVLWDYEGZFA"},
            {"rotor" : 1, "ring_setting" : 'V', "expected" : "BYLQUIOJRTCSPNKVDWMXEZFHAG"},
            {"rotor" : 1, "ring_setting" : 'W', "expected" : "HCZMRVJPKSUDTQOLWEXNYFAGIB"},
            {"rotor" : 1, "ring_setting" : 'X', "expected" : "CIDANSWKQLTVEURPMXFYOZGBHJ"},
            {"rotor" : 1, "ring_setting" : 'Y', "expected" : "KDJEBOTXLRMUWFVSQNYGZPAHCI"},
            {"rotor" : 1, "ring_setting" : 'Z', "expected" : "JLEKFCPUYMSNVXGWTROZHAQBID"},

            # Test all ring settings for rotor II
            {"rotor" : 2, "ring_setting" : 'A', "expected" : "AJDKSIRUXBLHWTMCQGZNPYFVOE"},
            {"rotor" : 2, "ring_setting" : 'B', "expected" : "FBKELTJSVYCMIXUNDRHAOQZGWP"},
            {"rotor" : 2, "ring_setting" : 'C', "expected" : "QGCLFMUKTWZDNJYVOESIBPRAHX"},
            {"rotor" : 2, "ring_setting" : 'D', "expected" : "YRHDMGNVLUXAEOKZWPFTJCQSBI"},
            {"rotor" : 2, "ring_setting" : 'E', "expected" : "JZSIENHOWMVYBFPLAXQGUKDRTC"},
            {"rotor" : 2, "ring_setting" : 'F', "expected" : "DKATJFOIPXNWZCGQMBYRHVLESU"},
            {"rotor" : 2, "ring_setting" : 'G', "expected" : "VELBUKGPJQYOXADHRNCZSIWMFT"},
            {"rotor" : 2, "ring_setting" : 'H', "expected" : "UWFMCVLHQKRZPYBEISODATJXNG"},
            {"rotor" : 2, "ring_setting" : 'I', "expected" : "HVXGNDWMIRLSAQZCFJTPEBUKYO"},
            {"rotor" : 2, "ring_setting" : 'J', "expected" : "PIWYHOEXNJSMTBRADGKUQFCVLZ"},
            {"rotor" : 2, "ring_setting" : 'K', "expected" : "AQJXZIPFYOKTNUCSBEHLVRGDWM"},
            {"rotor" : 2, "ring_setting" : 'L', "expected" : "NBRKYAJQGZPLUOVDTCFIMWSHEX"},
            {"rotor" : 2, "ring_setting" : 'M', "expected" : "YOCSLZBKRHAQMVPWEUDGJNXTIF"},
            {"rotor" : 2, "ring_setting" : 'N', "expected" : "GZPDTMACLSIBRNWQXFVEHKOYUJ"},
            {"rotor" : 2, "ring_setting" : 'O', "expected" : "KHAQEUNBDMTJCSOXRYGWFILPZV"},
            {"rotor" : 2, "ring_setting" : 'P', "expected" : "WLIBRFVOCENUKDTPYSZHXGJMQA"},
            {"rotor" : 2, "ring_setting" : 'Q', "expected" : "BXMJCSGWPDFOVLEUQZTAIYHKNR"},
            {"rotor" : 2, "ring_setting" : 'R', "expected" : "SCYNKDTHXQEGPWMFVRAUBJZILO"},
            {"rotor" : 2, "ring_setting" : 'S', "expected" : "PTDZOLEUIYRFHQXNGWSBVCKAJM"},
            {"rotor" : 2, "ring_setting" : 'T', "expected" : "NQUEAPMFVJZSGIRYOHXTCWDLBK"},
            {"rotor" : 2, "ring_setting" : 'U', "expected" : "LORVFBQNGWKATHJSZPIYUDXEMC"},
            {"rotor" : 2, "ring_setting" : 'V', "expected" : "DMPSWGCROHXLBUIKTAQJZVEYFN"},
            {"rotor" : 2, "ring_setting" : 'W', "expected" : "OENQTXHDSPIYMCVJLUBRKAWFZG"},
            {"rotor" : 2, "ring_setting" : 'X', "expected" : "HPFORUYIETQJZNDWKMVCSLBXGA"},
            {"rotor" : 2, "ring_setting" : 'Y', "expected" : "BIQGPSVZJFURKAOEXLNWDTMCYH"},
            {"rotor" : 2, "ring_setting" : 'Z', "expected" : "ICJRHQTWAKGVSLBPFYMOXEUNDZ"},

            # Test all ring settings for rotor III
            {"rotor" : 3, "ring_setting" : 'A', "expected" : "BDFHJLCPRTXVZNYEIWGAKMUSQO"},
            {"rotor" : 3, "ring_setting" : 'B', "expected" : "PCEGIKMDQSUYWAOZFJXHBLNVTR"},
            {"rotor" : 3, "ring_setting" : 'C', "expected" : "SQDFHJLNERTVZXBPAGKYICMOWU"},
            {"rotor" : 3, "ring_setting" : 'D', "expected" : "VTREGIKMOFSUWAYCQBHLZJDNPX"},
            {"rotor" : 3, "ring_setting" : 'E', "expected" : "YWUSFHJLNPGTVXBZDRCIMAKEOQ"},
            {"rotor" : 3, "ring_setting" : 'F', "expected" : "RZXVTGIKMOQHUWYCAESDJNBLFP"},
            {"rotor" : 3, "ring_setting" : 'G', "expected" : "QSAYWUHJLNPRIVXZDBFTEKOCMG"},
            {"rotor" : 3, "ring_setting" : 'H', "expected" : "HRTBZXVIKMOQSJWYAECGUFLPDN"},
            {"rotor" : 3, "ring_setting" : 'I', "expected" : "OISUCAYWJLNPRTKXZBFDHVGMQE"},
            {"rotor" : 3, "ring_setting" : 'J', "expected" : "FPJTVDBZXKMOQSULYACGEIWHNR"},
            {"rotor" : 3, "ring_setting" : 'K', "expected" : "SGQKUWECAYLNPRTVMZBDHFJXIO"},
            {"rotor" : 3, "ring_setting" : 'L', "expected" : "PTHRLVXFDBZMOQSUWNACEIGKYJ"},
            {"rotor" : 3, "ring_setting" : 'M', "expected" : "KQUISMWYGECANPRTVXOBDFJHLZ"},
            {"rotor" : 3, "ring_setting" : 'N', "expected" : "ALRVJTNXZHFDBOQSUWYPCEGKIM"},
            {"rotor" : 3, "ring_setting" : 'O', "expected" : "NBMSWKUOYAIGECPRTVXZQDFHLJ"},
            {"rotor" : 3, "ring_setting" : 'P', "expected" : "KOCNTXLVPZBJHFDQSUWYAREGIM"},
            {"rotor" : 3, "ring_setting" : 'Q', "expected" : "NLPDOUYMWQACKIGERTVXZBSFHJ"},
            {"rotor" : 3, "ring_setting" : 'R', "expected" : "KOMQEPVZNXRBDLJHFSUWYACTGI"},
            {"rotor" : 3, "ring_setting" : 'S', "expected" : "JLPNRFQWAOYSCEMKIGTVXZBDUH"},
            {"rotor" : 3, "ring_setting" : 'T', "expected" : "IKMQOSGRXBPZTDFNLJHUWYACEV"},
            {"rotor" : 3, "ring_setting" : 'U', "expected" : "WJLNRPTHSYCQAUEGOMKIVXZBDF"},
            {"rotor" : 3, "ring_setting" : 'V', "expected" : "GXKMOSQUITZDRBVFHPNLJWYACE"},
            {"rotor" : 3, "ring_setting" : 'W', "expected" : "FHYLNPTRVJUAESCWGIQOMKXZBD"},
            {"rotor" : 3, "ring_setting" : 'X', "expected" : "EGIZMOQUSWKVBFTDXHJRPNLYAC"},
            {"rotor" : 3, "ring_setting" : 'Y', "expected" : "DFHJANPRVTXLWCGUEYIKSQOMZB"},
            {"rotor" : 3, "ring_setting" : 'Z', "expected" : "CEGIKBOQSWUYMXDHVFZJLTRPNA"},
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["rotor"])
            rtor.ring_setting(tc["ring_setting"])
            self.assertEqual(tc["expected"], rtor.rotor)


    # Example (reverse rotor I):
    #
    # EKMFLGDQVZNTOWYHXUSPAIBRCJ original rotor I
    # ||||||||||||||||||||||||||
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ mapping
    # ||||||||||||||||||||||||||
    # UWYGADFPVZBECKMTHXSLRINQOJ reversed rotor I
    def test_reverse(self):
        tt = [
            {"rotor" : 1, "expected" : "UWYGADFPVZBECKMTHXSLRINQOJ"},
            {"rotor" : 2, "expected" : "AJPCZWRLFBDKOTYUQGENHXMIVS"},
            {"rotor" : 3, "expected" : "TAGBPCSDQEUFVNZHYIXJWLRKOM"}
        ]
        for tc in tt:
            rtor = rotor.Rotor(tc["rotor"])
            rtor.reverse()
            self.assertEqual(tc["expected"], rtor.rotor)


    # Example (encrypting a letter):
    #
    # Ring setting                  AAA
    # Rotor position before input   AAZ
    # Keyboard input                  A
    # TODO: plugboard
    # Right rotor III steps
    # Rotor position                AAA
    # TODO: plugboard
    # Output                          U
    #
    # --------------------------
    # A becomes B:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # BDFHJLCPRTXVZNYEIWGAKMUSQO (Right Rotor III)
    # --------------------------
    #
    # --------------------------
    # B becomes J:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # AJDKSIRUXBLHWTMCQGZNPYFVOE (Middle Rotor II)
    #
    # --------------------------
    # J becomes Z:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # EKMFLGDQVZNTOWYHXUSPAIBRCJ (Left Rotor I)
    #
    # --------------------------
    # Z becomes T:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # YRUHQSLDPXNGOKMIEBFZCWVJAT (Reflector B)
    #
    # --------------------------
    # T becomes L:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # UWYGADFPVZBECKMTHXSLRINQOJ (Reverse Left Rotor I)
    # --------------------------
    #
    # --------------------------
    # L becomes K:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # AJPCZWRLFBDKOTYUQGENHXMIVS (Reverse Middle Rotor II)
    # --------------------------
    #
    # --------------------------
    # K becomes U:
    # --------------------------
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ||||||||||||||||||||||||||
    # TAGBPCSDQEUFVNZHYIXJWLRKOM (Reverse Right Rotor III)
    def test_encrypt(self):
        pass
