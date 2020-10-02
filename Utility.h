#pragma once


#include <iostream>
using namespace std;


// C++ lacks the correct modulus functionality for negative numbers
// Found alternative mod function here: https://stackoverflow.com/questions/43018206/modulo-of-negative-integers-in-go
int Mod (int D, int M)
{
        int R = D % M;
        if ((R < 0 && M > 0) || (R > 0 && M < 0))
        {
                return R + M;
        }
        return R;
}


bool Is_Upper_Case (char c)
{
        if (c >= 'A' && c <= 'Z') return true;
        else                      return false;
}


bool Is_Lower_Case (char c)
{
        if (c >= 'a' && c <= 'z') return true;
        else                      return false;
}


// Credits to: https://catonmat.net/ascii-case-conversion-trick
char Toggle_Case (char c)
{
        return c ^ 0b00100000;
}


bool Is_ASCII (char c)
{
        return (Is_Upper_Case (c) || Is_Lower_Case (c));
}


int Alphabet_Index (char C)
{
        if (Is_Upper_Case (C)) return C - 'A';
        if (Is_Lower_Case (C)) return C - 'a';
        else                   return -1;
}


int Index (char * Source, int Length, char C)
{
        for (int I = 0; I < Length; ++I)
        {
                if (C == Source [I])
                {
                        return I;
                }
        }
        return -1;
}


void Rotate_Left (char * R, int Length)
{
        char C = R [0];
        for (int I = 0; I < Length; ++I)
        {
                R [I] = R [Mod (I + 1, Length)];
        }
        R [Length - 1] = C;
}


void Rotate_Left (char * R, int Length, int Steps)
{
        for (int I = 0; I < Steps; ++I)
        {
                Rotate_Left (R, Length);
        }
}


void Copy (char * Source, char * Destination, int Length)
{
        for (int I = 0; I < Length; ++I)
        {
                Destination [I] = Source [I];
        }
}


void Print (char * Source, int Length)
{
        for (int I = 0; I < Length; ++I)
        {
                cout << Source [I];
        }
        cout << endl;
}
