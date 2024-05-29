function asyncFunction() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const randomNumber = Math.random();
            if (randomNumber > 0.5) {
                resolve(randomNumber);
            } else {
                reject(new Error('Random number is less than 0.5'));
            }
        }, 1000);
    });
}

asyncFunction()
    .then(result => console.log('Resolved:', result))
    .catch(error => console.error('Rejected:', error.message));
