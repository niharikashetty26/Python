// You are assigned the task of developing a program to count the number of words in a given string. Count and return the number of words present in the string.
// Note
// An extra space has been inserted after the last word of the string
// Expected Input
// "I am a Ninja Coder "
// Expected Output
// 5
// Test Cases
// Count the total number of words in the given string
// Return the count of words


function countWords(str) {
    str = str.trim();

    let words = str.split(" ");

    return words.length;
}

console.log(countWords("I am a Ninja Coder ")); 
