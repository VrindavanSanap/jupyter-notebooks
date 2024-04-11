// Define your array
const a = [
  [1, 2, 3, 4, 5, 6],
  [7, 8, 9, 10, 11, 12],
  [13, 14, 15, 16, 17, 18],
];

function slice2DArray(array, rowStart, rowEnd, colStart, colEnd) {
  return array.slice(rowStart, rowEnd ).map(row => row.slice(colStart, colEnd ));
}


// Function to slice a 2D array
// Usage
const result = slice2DArray(a, 1, 3, 3, 5);
console.log(result);

