using System;

bool HasTargetsBlood = true;
bool IsInCircle = false;

void Jutsu()
{
    if (IsInCircle == true && HasTargetsBlood == true)
    {
        Console.WriteLine("Jutsu is Active!");
    }

    else
    {
        Console.WriteLine("Jutsu not active!");
    }
}

Jutsu();