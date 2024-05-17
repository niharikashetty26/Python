document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        let valid = true;

        let errorMessages = [];



        const email = document.getElementById('email').value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            errorMessages.push('Please enter a valid email address.');
            valid = false;
        }

        const password = document.getElementById('password').value;
        const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,15}$/;
        if (!passwordPattern.test(password)) {
            errorMessages.push('Password must be 8-15 characters and include an uppercase letter, a lowercase letter, a digit, and a special character.');
            valid = false;
        }

        const confirmPassword = document.getElementById('confirm_password').value;
        if (password !== confirmPassword) {
            errorMessages.push('Passwords do not match.');
            valid = false;
        }

        const firstName = document.getElementById('first_name').value;
        const lastName = document.getElementById('last_name').value;
        if (!firstName && !lastName) {
            errorMessages.push('Either First Name or Last Name is required.');
            valid = false;
        }

        const dob = document.getElementById('dob').value;
        const dobPattern = /^\d{4}-\d{2}-\d{2}$/;
        if (!dobPattern.test(dob)) {
            errorMessages.push('Please enter a valid date in the format YYYY-MM-DD.');
            valid = false;
        }

        const gender = document.getElementById('gender').value;
        if (!gender) {
            errorMessages.push('Please select a gender.');
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
            alert(errorMessages.join('\n'));
        }
    });
});
