// Array of Items
const array = [
  "Item 1",
  "Item 2",
  "Item 3",
  "Item 4",
] as const

// Const function to pull random element from array
const operation = () => array[Math.floor(Math.random() * array.length)]