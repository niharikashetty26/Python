document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        let valid = true;

        const email = document.getElementById('email').value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert('Please enter a valid email address.');
            valid = false;
        }

        const password = document.getElementById('password').value;
        const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,15}$/;
        if (!passwordPattern.test(password)) {
            alert('Password must be 8-15 characters and include should have uppercase, lowercase letter, one digit, and special character.');
            valid = false;
        }

        const confirmPassword = document.getElementById('confirm_password').value;
        if (password !== confirmPassword) {
            alert('Passwords do not match.');
            valid = false;
        }

        const firstName = document.getElementById('first_name').value;
        const lastName = document.getElementById('last_name').value;
        if (!firstName && !lastName) {
            alert('Either First Name or Last Name should be entered.');
            valid = false;
        }

        const dob = document.getElementById('dob').value;
        const dobPattern = /^\d{4}-\d{2}-\d{2}$/;
        if (!dobPattern.test(dob)) {
            alert('Please enter a valid date in the format DD/MM/YYYY.');
            valid = false;
        }

        const gender = document.getElementById('gender').value;
        if (!gender) {
            alert('Please select a gender.');
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});
