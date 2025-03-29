// Task 10: Get Last Character of a String
// Instructions:
// Write a function lastCharacter(str) that returns the last character of a string.
// Test Cases:
// console.log(lastCharacter("JavaScript")); // "t"
// console.log(lastCharacter("Hello")); // "o"
// console.log(lastCharacter("X")); // "X"
// console.log(lastCharacter("World!")); // "!"
// console.log(lastCharacter("")); // undefined

function lastCharacter(str){
    return str[str.length - 1]
}

console.log(lastCharacter("World!"))