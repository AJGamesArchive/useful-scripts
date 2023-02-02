import random;

# Prints numbers from 1 to 100, replacing multiples of 3 with 'Fizz' and multiples of 5 with 'Buzz'.
for i in range(0, 101):
  output = str("");
  if(i % 3 == 0):
    output += "Fizz";
  if(i % 5 == 0):
    output += "Buzz";
  if(output == ""):
    output = str(i);
  print(output);