/*
        Copyright 2020 Sorn Naser Zupanic Maksumic

        Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/


// Links that helped me a lot:
//      https://piotte13.github.io/enigma-cipher/               (for understanding wiring, best emulator)
//      https://cryptii.com/pipes/enigma-machine                (for testing output)
//      https://www.101computing.net/enigma-machine-emulator/   (emulator which shows basic encryption steps)


#pragma region Include
#include "Utility.h"
#include <iostream>
using namespace std;
#pragma endregion


enum LMR { Left, Middle, Right }; // Used to access rotors 0, 1, and 2 respectively (default ordering is I, II, III)

char Alphabet [26] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };


#pragma region Forward Declaration
char Encrypt_Character (char const Plugboard [10][2], char C);
char Encrypt_Character (char Rotor [26], char Ring_Position, char Plain_Character);
void Reverse (char Source [26]);
void Set_Ring_Setting (char Source [26], char RS);
void Step (char * C);
void Format_Plaintext (string * Plaintext);
#pragma endregion


int main ()
{
        #pragma region Setup Settings
        char Rotor [3][26] =
        {
                { 'E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J' },
                { 'A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E' },
                { 'B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O' },
        };
        char Ring_Setting  [3] = { 'A', 'B', 'C' };
        char Ring_Position [3] = { 'D', 'E', 'F' };
        char Rotor_Notch   [3] = { 'Q', 'E', 'V' };
        char Reflector_B  [26] = { 'Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T' };
        char const Plugboard [10][2] =
        {
                {'A', 'T'},
                {'B', 'S'}, 
                {'D', 'E'},
                {'F', 'M'},
                {'I', 'R'},
                {'K', 'N'},
                {'L', 'Z'},
                {'O', 'W'},
                {'P', 'V'},
                {'X', 'Y'}
        };
        #pragma endregion

        #pragma region Apply Ring Setting
        Set_Ring_Setting (Rotor [Left],   Ring_Setting [Left]);
        Set_Ring_Setting (Rotor [Middle], Ring_Setting [Middle]);
        Set_Ring_Setting (Rotor [Right],  Ring_Setting [Right]);
        #pragma endregion

        #pragma region Calculate Reverse Rotors
        char Rotor_Reverse [3][26];

        Copy (Rotor [Left],   Rotor_Reverse [Left], 26);
        Copy (Rotor [Middle], Rotor_Reverse [Middle], 26);
        Copy (Rotor [Right],  Rotor_Reverse [Right], 26);

        Reverse (Rotor_Reverse [Left]);
        Reverse (Rotor_Reverse [Middle]);
        Reverse (Rotor_Reverse [Right]);
        #pragma endregion

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        string Plaintext = "This is the first assignment of four assignments for this course";
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        #pragma region Print Information and Format Plaintext
        cout << "----------------------------------------------------------------------------------------------------------------" << endl;
        cout << "WEHRMACHT ENIGMA I" << endl;
        cout << "----------------------------------------------------------------------------------------------------------------" << endl;
        cout << "Ring Setting:   " << Ring_Setting  [Left] << "-" << Ring_Setting  [Middle] << "-" << Ring_Setting  [Right] << endl;
        cout << "Start Position: " << Ring_Position [Left] << "-" << Ring_Position [Middle] << "-" << Ring_Position [Right] << endl;
        cout << "Rotor Notch:    " << Rotor_Notch   [Left] << "-" << Rotor_Notch   [Middle] << "-" << Rotor_Notch   [Right] << endl;
        cout << "Plugboard:      ";
        for (int I = 0; I < 10; ++I)
        {
                cout << Plugboard [I][0] << Plugboard [I][1] << " ";
        }
        cout << endl;

        cout << "----------------------------------------------------------------------------------------------------------------" << endl;
        cout << "Plaintext:" << endl << Plaintext << endl;
        cout << "----------------------------------------------------------------------------------------------------------------" << endl;

        Format_Plaintext (& Plaintext);

        cout << "----------------------------------------------------------------------------------------------------------------" << endl;
        cout << "Ciphertext:" << endl;
        #pragma endregion

        for (int I = 0; I < Plaintext.length(); ++I)
        {
                #pragma region Output Spacing
                if (I > 0 && Mod (I, 5) == 0)
                {
                        cout << " ";
                }
                #pragma endregion

                char Cipher_Character = Plaintext [I];
           
                #pragma region Plugboard In
                Cipher_Character = Encrypt_Character (Plugboard, Cipher_Character);
                #pragma endregion

                #pragma region Rotate
                if (Ring_Position [Right] == Rotor_Notch [Right])
                {
                        if (Ring_Position [Middle] == Rotor_Notch [Middle])
                        {
                                Step (& Ring_Position [Left]);
                        }
                        Step (& Ring_Position [Middle]);
                }
                else
                {
                        if (Ring_Position [Middle] == Rotor_Notch [Middle])
                        {
                                Step (& Ring_Position [Middle]);
                                Step (& Ring_Position [Left]);
                        }
                }
                Step (&Ring_Position [Right]);
                #pragma endregion

                #pragma region Encrypt Character
                Cipher_Character = Encrypt_Character (Rotor [Right],  Ring_Position [Right],  Cipher_Character);
                Cipher_Character = Encrypt_Character (Rotor [Middle], Ring_Position [Middle], Cipher_Character);
                Cipher_Character = Encrypt_Character (Rotor [Left],   Ring_Position [Left],   Cipher_Character);

                Cipher_Character = Alphabet [Alphabet_Index (Reflector_B [Alphabet_Index (Cipher_Character)])];

                Cipher_Character = Encrypt_Character (Rotor_Reverse [Left],   Ring_Position [Left],   Cipher_Character);
                Cipher_Character = Encrypt_Character (Rotor_Reverse [Middle], Ring_Position [Middle], Cipher_Character);
                Cipher_Character = Encrypt_Character (Rotor_Reverse [Right],  Ring_Position [Right],  Cipher_Character);
                #pragma endregion

                #pragma region Plugboard Out
                Cipher_Character = Encrypt_Character (Plugboard, Cipher_Character);
                #pragma endregion

                cout << Cipher_Character;
        }
        cout << endl;
        cout << "----------------------------------------------------------------------------------------------------------------" << endl;
}


// Encrypt C with given plugboard
char Encrypt_Character (char const Plugboard [10][2], char C)
{
        for (int X = 0; X < 10; ++X)
        {
                if      (C == Plugboard [X][0]) return Plugboard [X][1];
                else if (C == Plugboard [X][1]) return Plugboard [X][0];
        }
        return C;
}


// Encrypt character C with given rotor and ring position
char Encrypt_Character (char Rotor [26], char Ring_Position, char C)
{
        int Offset = 0;
        Offset = Mod (Alphabet_Index (C)               + Alphabet_Index (Ring_Position), 26);
        Offset = Mod (Alphabet_Index (Rotor [Offset])  - Alphabet_Index (Ring_Position), 26);
        return Alphabet [Offset];
}


// EKMFLGDQVZNTOWYHXUSPAIBRCJ = Original Left Rotor I (input)
//
// ABCDEFGHIJKLMNOPQRSTUVWXYZ
// ||||||||||||||||||||||||||
// UWYGADFPVZBECKMTHXSLRINQOJ = Reversed Left Rotor I (output)
void Reverse (char Source [26])
{
        char Temp [26];
        // For each character in the alphabet
        for (int I = 0; I < 26; ++I)
        {
                // For each character in the source
                for (int J = 0; J < 26; ++J)
                {
                        if (Alphabet_Index (Source [J]) == I)
                        {
                                Temp [I] = 'A' + J;
                        }
                }
        }
        Copy (Temp, Source, 26);
}


/*
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        ||||||||||||||||||||||||||
        BDFHJLCPRTXVZNYEIWGAKMUSQO (Rotor III - Ringstellung A)

        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        ||||||||||||||||||||||||||
        PCEGIKMDQSUYWAOZFJXHBLNVTR (Rotor III - Ringstellung B)


 Ringstellung H    Ringstellung G    Ringstellung F     Ringstellung E     Ringstellung D     Ringstellung C     Ringstellung B     Ringstellung A
   ---------         ---------         ---------          ---------          ---------          ---------          ---------          ---------
   Z       Z         Z    ---Z         Z       Z          Z       Z          Z       Z          Z       Z          Z       Z          Z       Z
   Y       Y         Y   /   Y         Y    ---Y          Y       Y          Y       Y          Y       Y          Y       Y          Y       Y
   X       X         X   |   X         X   /   X          X    ---X          X    ---X          X       X          X       X          X       X
   W       W         W   |   W         W   |   W          W   /   W          W   /   W          W     --W          W       W          W       W
   V       V         V   |   V         V   |   V          V   |   V          V   |   V          V   /   V          V    ---V          V       V
   U       U         U   |   U         U   |   U          U   |   U          U   |   U          U   |   U          U   /   U          U    ---U
   T       T         T   |   T         T   |   T          T   |   T          T   |   T          T   |   T          T   |   T          T   /   T
   S       S         S   |   S         S   |   S          S   |   S          S   |   S          S   |   S          S   |   S          S   |   S
   R---    R         R   /   R         R   |   R          R   |   R          R   |   R          R   |   R          R   |   R          R   |   R
   Q   \   Q         Q---    Q         Q   /   Q          Q   |   Q          Q   |   Q          Q   |   Q          Q   |   Q          Q   |   Q
   P   |   P         P       P         P---    P          P   /   P          P   |   P          P   |   P          P   |   P          P   |   P
   O   |   O         O       O         O       O          O---    O          O   /   O          O   |   O          O   |   O          O   |   O
   N   |   N         N       N         N       N          N       N          N---    N          N   /   N          N   |   N          N   |   N
   M   |   M         M       M         M       M          M       M          M       M          M---    M          M   /   M          M   |   M
   L   |   L         L       L         L       L          L       L          L       L          L       L          L---    L          L   /   L
   J   |   J         J       J         K       K          K       K          K       K          K       K          K       K          K---    K
   J   |   J         J       J         J       J          J       J          J       J          J       J          J       J          J       J
   I   |   I         I       I         I       I          I       I          I       I          I       I          I       I          I       I
   H   |   H         H       H         H       H          H       H          H       H          H       H          H       H          H       H
   G   |   G         G       G         G       G          G       G          G       G          G       G          G       G          G       G
   F   |   F         F       F         F       F          F       F          F       F          F       F          F       F          F       F
   E   |   E         E       E         E       E          E       E          E       E          E       E          E       E          E       E
   D   |   D         D       D         D       D          D       D          D       D          D       D          D       D          D       D
   C   |   C         C       C         C       C          C       C          C       C          C       C          C       C          C       C
   B   \   B         B       B         B       B          B       B          B       B          B       B          B       B          B       B
== A    ---A      == A       A ==   == A       A ==    == A       A ==    == A       A ==    == A       A ==    == A       A ==    == A       A == Ring Position
   ---------         ---------         ---------          ---------          ---------          ---------          ---------          ---------
*/
void Set_Ring_Setting (char Source [26], char RS)
{
        char Temp [26];
        for (int I = 0; I < 26; ++I)
        {
                int Offset = Source [Mod (I - Alphabet_Index (RS), 26)] - Alphabet [Mod (I - Alphabet_Index (RS), 26)];
                char C = Alphabet [I] + Offset;
                if (C < 'A') C = Alphabet [I] + Mod (Offset, 26);
                if (C > 'Z') C = Alphabet [I] + Offset - 26;
                Temp [I] = C;
        }
        Copy (Temp, Source, 26);
}


// Ringstellung         AAA
// Rotor position       AAZ
// Keyboard input       A
// Right Rotor III 	Rotate_Left
// Rotor position       AAA
//
//	--------------------------
//	A becomes B:
//	--------------------------
//      ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//	BDFHJLCPRTXVZNYEIWGAKMUSQO (Right Rotor III)
//	--------------------------
//
//
//	--------------------------
//	B becomes J:
//	--------------------------
//      ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//	AJDKSIRUXBLHWTMCQGZNPYFVOE (Middle Rotor II)
//
//
//	--------------------------
//	J becomes Z:
//	--------------------------
//	ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//      EKMFLGDQVZNTOWYHXUSPAIBRCJ (Left Rotor I)
//
//
//	--------------------------
//	Z becomes T:
//	--------------------------
//      ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//	YRUHQSLDPXNGOKMIEBFZCWVJAT (Reflector B)
//
//
//	--------------------------
//	T becomes L:
//	--------------------------
//	ABCDEFGHIJKLMNOPQRSTUVWXYZ
//	||||||||||||||||||||||||||
//	UWYGADFPVZBECKMTHXSLRINQOJ (Reverse Left Rotor I)
//	--------------------------
//
//	--------------------------
//      L becomes K:
//      --------------------------
//      ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//	AJPCZWRLFBDKOTYUQGENHXMIVS (Reverse Middle Rotor II)
//	--------------------------
//
//
//	--------------------------
//	K becomes U:
//	--------------------------
//	ABCDEFGHIJKLMNOPQRSTUVWXYZ
//      ||||||||||||||||||||||||||
//	TAGBPCSDQEUFVNZHYIXJWLRKOM (Reverse Right Rotor III)


void Step (char * C)
{
        *C = Alphabet [Mod (Alphabet_Index (*C) + 1, 26)];
}


void Format_Plaintext (string * Plaintext)
{
        // Remove invalid characters (only a-zA-Z is valid) and make all uppercase
        string Tmp;
        for (int I = 0; I < Plaintext->length (); ++I)
        {
                if (Is_Lower_Case (Plaintext->at (I)))
                {
                        Plaintext->at (I) = Toggle_Case (Plaintext->at (I));
                }
                if (Is_Upper_Case (Plaintext->at (I)))
                {
                        Tmp += Plaintext->at (I);
                }
        }
        *Plaintext = Tmp;
}
