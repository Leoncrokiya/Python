using System.Collections.Specialized;
using System.Text;
// using System.Diagnostics;
// using System.Text;

// string name = "FRIEND";

// Console.WriteLine($"MERRY CHRISTMAS, {name}!");

// using System;

// class Program
// {
//     static void Main()
//     {
//         // Declare variables
//         string name;
//         int age;
//         double height;

//         // Get string input
//         Console.Write("Enter your name: ");
//         name = Console.ReadLine();

//         // Get integer input with validation
//         Console.Write("Enter your age: ");
//         while (!int.TryParse(Console.ReadLine(), out age) || age < 0)
//         {
//             Console.Write("Invalid input. Please enter a valid non-negative age: ");
//         }

//         // Get double input with validation
//         Console.Write("Enter your height in meters (e.g., 1.75): ");
//         while (!double.TryParse(Console.ReadLine(), out height) || height <= 0)
//         {
//             Console.Write("Invalid input. Please enter a positive number: ");
//         }

//         // Output the collected data
//         Console.WriteLine("\n--- Profile Summary ---");
//         Console.WriteLine($"Name: {name}");
//         Console.WriteLine($"Age: {age}");
//         Console.WriteLine($"Height: {height} m");
//     }
// }

Console.WriteLine("Enter your name: ");
string name = Console.ReadLine();

Console.WriteLine($"Hello, {name}!");