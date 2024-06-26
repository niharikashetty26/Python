// Variable declaration and assignment
let greeting = "Hello,";
const name = "John";

// Function declaration and calling
function greet(person) {
    return `${greeting} ${person}!`;
}
console.log(greet(name));

// Arrays and array methods
let numbers = [1, 2, 3, 4, 5];
numbers.push(6);
numbers.pop();
numbers.forEach(num => console.log(num));

// Objects and object methods
let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    greet: function () {
        return `Hello, ${this.firstName} ${this.lastName}!`;
    }
};
console.log(person.greet());

// Conditional statements
let x = 5;
if (x > 0) {
    console.log("Positive");
} else if (x < 0) {
    console.log("Negative");
} else {
    console.log("Zero");
}

// Loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Arrow functions
const multiply = (a, b) => a * b;
console.log(multiply(2, 3));

// Classes and objects
class Car {
    constructor(brand) {
        this.brand = brand;
    }
    drive() {
        console.log(`Driving ${this.brand}`);
    }
}
let myCar = new Car("Toyota");
myCar.drive();

// Promises and asynchronous code
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data fetched successfully!");
        }, 2000);
    });
}
fetchData().then(data => console.log(data));

// Error handling
try {
    throw new Error("Something went wrong!");
} catch (error) {
    console.log(error.message);
}