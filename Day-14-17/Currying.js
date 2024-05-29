function power(a) {
    return function (b) {
        return a + b
    }
}
const add = power(2)
console.log(add(2))