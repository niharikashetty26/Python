document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        let valid = true;

        const email = document.getElementById('email').value;
        if (!email) {
            alert('Email is required.');
            valid = false;
        } else {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid email address.');
                valid = false;
            }
        }

        const password = document.getElementById('password').value;
        if (!password) {
            alert('Password is required.');
            valid = false;
        } else {
            const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,15}$/;
            if (!passwordPattern.test(password)) {
                alert('Password must be 8-15 characters and include an uppercase letter, a lowercase letter, one digit, and a special character.');
                valid = false;
            }
        }

        const confirmPassword = document.getElementById('confirm_password').value;
        if (!confirmPassword) {
            alert('Confirm Password is required.');
            valid = false;
        } else if (password !== confirmPassword) {
            alert('Passwords do not match.');
            valid = false;
        }
        const firstName = document.getElementById('first_name').value;
        if (!firstName) {
            alert('First Name is required.');
            valid = false;
        }
        const lastName = document.getElementById('last_name').value;
        if (!lastName) {
            alert('Last Name is required.');
            valid = false;
        }

        const dob = document.getElementById('dob').value;
        if (!dob) {
            alert('Date of Birth is required.');
            valid = false;
        } else {
            const dobPattern = /^\d{4}-\d{2}-\d{2}$/;
            if (!dobPattern.test(dob)) {
                alert('Please enter a valid date in the format YYYY-MM-DD.');
                valid = false;
            }
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
