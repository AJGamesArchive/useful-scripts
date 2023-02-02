// Script generates an array of random integers
using System;
using System.IO;
using System.Linq;

class Program {
    // Generates an int array of size n, with random or static ints, based on given params
    static int[] intArrayGen(int amount, int randomRange) {
        int[] data = new int[amount]; // Int Array of Size n
        Random rmd = new Random();
        for (int i = 0; i < amount; i++) {
            if (randomRange != 0) {
                data[i] = rmd.Next(1, randomRange); // Generate Numbers Between 1 and 100
                continue;
            }
            data[i] = (i + 1);
        }
        Console.WriteLine(String.Join(",", data));
        return data;
    }

    static void Main() {
        intArrayGen(100, 0); // Generates 100 numbers, in order from 1 to 100
        intArrayGen(100, 100); // Generates 100 random numbers from 1 to 100, can have repeats
    }
}