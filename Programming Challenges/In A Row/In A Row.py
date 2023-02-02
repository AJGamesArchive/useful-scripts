def inARow(data: str):
  # Declare data stores
  results = dict({});
  repeatChecker = list([]);

  # Loop through data and count occurrence of each different character once, appends results to dict
  for i in data:
    if i in repeatChecker:
      continue;
    repeatChecker.append(i);
    charCount = int(data.count(i));
    results[i] = int(charCount);
  
  # Filter through results dictionary and returns char with highest occurrences
  highestIterVals = list(results.values());
  highestIterKeys = list(results.keys());
  finalResult = tuple((highestIterKeys[highestIterVals.index(max(highestIterVals))], highestIterVals[highestIterVals.index(max(highestIterVals))]));
  return finalResult;

# Run and output function
charCount = inARow(str(input("Please enter some data.\n: ")));
print(f"Character: {charCount[0]}\nOccurrence: {charCount[1]}");