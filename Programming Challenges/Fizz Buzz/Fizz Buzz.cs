using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.ComponentModel;

class Program {
    static void Main() {
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                Console.WriteLine("FizzBuzz");
                continue;
            }
            if (i % 3 == 0) {
                Console.WriteLine("Fizz");
                continue;
            }
            if (i % 5 == 0) {
                Console.WriteLine("Buzz");
                continue;
            }
            Console.WriteLine(i);
            continue;
        }
    }   
}

// TODO Clean this up so there's no duplicate logic