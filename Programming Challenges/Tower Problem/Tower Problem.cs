using System;
class Program {
	static void Main(string[] args) {
        int number = Convert.ToInt32(Console.ReadLine());
		for (int i = 1; i <= number; i = i + 1) {
            for (int n = 1; n <= ((((number - 1) + number) - ((i - 1) + i)) / 2); n++) {
                Console.Write(" ");
            }
            for (int n = 1; n <= (i - 1) + i; n++) {
                Console.Write("#");
            }
            Console.WriteLine();
		}
	}
}