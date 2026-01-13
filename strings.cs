using System.Diagnostics;

Console.WriteLine("konnichiwa sekai");

Console.WriteLine("こんにちは世界");

string one = "asta";

one = one.Trim();

string two = "yuno";

string rivals = $"{one} and {two} are friends and rivals.";

Console.WriteLine(rivals);
Console.WriteLine(rivals.Replace("asta", "yuno"));
Console.WriteLine(rivals);