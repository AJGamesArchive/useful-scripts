def TowerGen(towerHight: int):
  # Generate each line of the tower to print individually
  for i in range(towerHight):
    hashString = str("");
    for n in range(int((((towerHight - 1) + towerHight) - (i + (i + 1))) / 2)):
      hashString = str(hashString + " ");
    for n in range(int(i + (i + 1))):
      hashString = str(hashString + "#");
    print(hashString);

# Run and output function
towerHight = str(input("Enter a whole number: "));
if not towerHight.isdigit():
  print("That is not a whole number!");
  exit();
towerHight = int(towerHight)
TowerGen(towerHight)