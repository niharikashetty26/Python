function outerFunction() {
    let outerVariable = 'I am outer';

    function innerFunction() {
        console.log(outerVariable);
    }

    return innerFunction;
}

const innerFunc = outerFunction();
innerFunc(); 
