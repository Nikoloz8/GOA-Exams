// Task 9: Check if a Number is Positive
// Instructions:
// Write a function isPositive(num) that returns true if the number is positive, otherwise false.
// Test Cases:
// console.log(isPositive(10)); // true
// console.log(isPositive(-5)); // false
// console.log(isPositive(0)); // false
// console.log(isPositive(100)); // true
// console.log(isPositive(-1)); // false

function isPositive(num){
    if (num > 0){
        return true
    } else{
        return false
    }
}

console.log(isPositive(0))