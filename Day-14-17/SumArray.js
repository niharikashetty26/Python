// You are tasked with creating a program that processes an array of positive integers.Your goal is to find the sum of all even numbers 
// in the array, but you need to implement a special condition: if you encounter a number that is a multiple of 5, you should skip it and 
// move on to the next element without including it in the sum.

// Expected Input
// [1, 6, 8, 3, 5, 20, 10]
// Expected Output
// 14
// Test Cases
// Find all the even elements in the array
// Omit those elements which are divisible by 5
// Sum all the the elements which satisfy the given conditions
// Return the sum

function sumOfArray(arr) {
    let sum = 0;

    for (let num of arr) {
        if (num % 2 === 0 && num % 5 !== 0) {
            sum += num;
        }
    }
    return sum;
}
console.log(sumOfArray([1, 6, 8, 3, 5, 20, 10]));
