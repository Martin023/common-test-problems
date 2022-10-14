// Filter and map are two of the most common array methods.
//  Filter returns a new array with all the elements that pass a test. Hence used with a callback function where he test is actually written
// ---------------------Code------------------------------
// const input = [1,2,5,66,77,89,99,9]
// const output = input.filter(x => x == 2).length
// console.log(output)


//  Map returns a new array with the results of calling a function on every element.
// map creates another array with the results of calling a function for every array element.
// ---------------------Code------------------------------
// const input = [1,2,5,66,77,89,99,9]
// const output = input.map(x => x == 2)
// console.log(output)
//  Reduce is a more general form of map and filter.
//  It can be used to calculate a single value from an array.
//  It takes a function and an initial value as arguments. 
// The function is called with two arguments, the current value and the current sum.
//  The current value is the next element in the array, and the current sum is the value returned by the previous call to the function. The initial value is the starting value for the sum. If the array is empty, the initial value is returned.
// ---------------------------code--------------------------------
const input = [1,2,5,66,77,89,99,9]
const output = input.reduce((sum, x) => sum + x, 0)
console.log(output)




