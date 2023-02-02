using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

class Program {

    // Function that looks for a digit word within a string, returns -1 if no digit is found
    static int digitWord(string data) {
        var digits = new Dictionary<string, int>() {
            {"ONE", 1},
            {"TWO", 2},
            {"THREE", 3},
            {"FOUR", 4},
            {"FIVE", 5},
            {"SIX", 6},
            {"SEVEN", 7},
            {"EIGHT", 8},
            {"NINE", 9}
        };
        string[] digWords = digits.Keys.ToArray();
        foreach (string selDigWord in digWords) {
            int charCounter = 0;
            string word = data;
            foreach (char i in selDigWord) {
                if (!word.Contains(i)) {break;}
                charCounter += 1;
                word = word.Split(i)[1];
            }
            if (charCounter != selDigWord.Length) {continue;}
            return digits[selDigWord];
        }
        return -1;
    }

    // Main Function
    static void Main() {
        Console.WriteLine("Enter a Word:");
        string word = Console.ReadLine().ToUpper();
        if(word == "E") {return;}
        Console.WriteLine(digitWord(word));
        Main();
    }
}

//TODO Make it detect 'THREE', 'SEVEN', and 'NINE' correctly.