// Imports
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

class Program {

    // Function that generates a random string of characters based on a given length
    static string stringGen(int length) {
        Random random = new Random();
        string data = "";
        for (int i = 0; i < 100; i++) {
            char letter = Convert.ToChar(random.Next(97, 123)); // ASCII character codes 97-123, produces a lowercase letter
            data = String.Concat(data, letter);
        }
        return data;
    }

    // Function that counts the occurrence of characters in a string and returns the character with the greatest occurrence
    static object[] inARow(string data) {
        char[] repeatChecker = new char[10000];
        var results = new Dictionary<char, int>();
        foreach(char i in data) {
            if(repeatChecker.Contains(i)) {
                continue;
            }
            repeatChecker[i] = i;
            results.Add(i, data.Count(f => (f == i)));
        }
        char[] keys = results.Keys.ToArray();
        int[] values = results.Values.ToArray();
        object[] result = {keys[Array.IndexOf(values, values.Max())], values[Array.IndexOf(values, values.Max())]};
        return result;
    }

    // Main function
    static void Main() {
        string data = stringGen(10);
        Console.WriteLine(data); //! Debug line, remove later
        object[] finalResult = inARow(data);
        Console.WriteLine(String.Join(", ", finalResult));
    }
}

//TODO Make the program output the full results dictionary
//TODO Check that the program works with a string of any data type