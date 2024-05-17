function createCounter() {
    let count = 0;

    const increment = () => {
        count++;
        console.log('Count:', count);
    };

    const decrement = () => {
        count--;
        console.log('Count:', count);
    };

    const getCount = () => {
        return new Promise(resolve => {
            setTimeout(() => {
                resolve(count);
            }, 1000);
        });
    };

    return { increment, decrement, getCount };
}

const counter = createCounter();
counter.increment();
counter.decrement();
counter.getCount().then(count => console.log('Current count:', count));
