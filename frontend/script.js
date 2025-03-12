// Inputs elements
const inputRUT = document.getElementById('rut');
const inputEmail = document.getElementById('email');
const inputName = document.getElementById('name');
const inputLastName = document.getElementById('lastName');
const inputAge = document.getElementById('age');
const inputPhone = document.getElementById('phone');

// Message element
const message = document.getElementById('message');

// Submit button
const submitButton = document.getElementById('submit');

// TODO Validate the RUT
function validateRUT(rut){
    let reversedRUT = reverseRUT(rut);
    const dv = isNaN(+reversedRUT[0]) ? reversedRUT.shift : +reversedRUT.shift();
    let counter = 2;
    let sum = 0;

    // Iterates over the reversed RUT
    for (let digit of reversedRUT) {
        // Converts the digit to a number    
        digit = +digit;
        // Checks if the digit is not a number
        if (isNaN(digit)) return false;
        let product = digit * counter;
        sum += product;
        counter++;
        // Resets the counter
        if (counter === 8) counter = 2;
    }
    // Gets the remainder of the sum divided by 11
    let remainder = sum % 11;
    // Calculates the expected DV
    let expectedDV = 11 - remainder;

    if (expectedDV === 10) expectedDV = 'K';
    else if (expectedDV === 11) expectedDV = 0;
    
    if (expectedDV === dv) return true;
    else return false;

}

// TODO Handle the RUT
function handleRUT(){
    let rut = inputRUT.value;
    if (validateRUT(rut)){
        alert('RUT válido');
    }else{
        alert('RUT inválido');
    }
}

// TODO Reverse the RUT
function reverseRUT(rut){
    if (typeof rut !== 'string') return 'Invalid input';
    else if  (rut.length < 1) return 'Empty input';
    else if (rut.length === 1) return rut;
    return rut.split('').reverse();

}

// TODO Handle Submission
function handleSubmit(){
    if (handleRUT() && handleEmail()){
        alert('Formulario enviado con éxito');
    }else{
        console.error('Error en el formulario');
    }
}

// TODO Validate Email
function validateEmail(email){
    // Basic regex pattern for emails
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// TODO Handle Email
function handleEmail(){
    let email = inputEmail.value;
    if (validateEmail(email)){
        alert('Email válido');
        return true;
    }else{
        alert('Email inválido');
        return false;
    }
}

// TODO Add Event Listeners
submitButton.addEventListener('click', handleSubmit);