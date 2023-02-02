// Imports
using System;
using System.IO;
using System.Linq;

class Program {
  // Function that generates an int array of random integers
  static int[] numArrayGen() {
      int[] data = new int[10000];
      Random rmd = new Random();
      for (int i = 0; i < 10000; i++) {
        data[i] = rmd.Next(1, 20000);
      }
      return data;
  }

  // Function that takes an array of ints and calculates the max profit
  static int maxProfit(int[] data) {
    int[] filteredArray = data.Skip(Array.IndexOf(data, data.Min())).ToArray();
    int profit = filteredArray.Max() - data.Min();
    return profit;
  }

  // Main Function
  static void Main(string[] args) {
    int[] data = numArrayGen();
    Console.WriteLine(maxProfit(data));
  }
}