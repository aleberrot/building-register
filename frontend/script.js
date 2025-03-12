
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
        return true;
    }else{
        alert('RUT inválido');
        return false;
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
async function handleSubmit(e){
    e.preventDefault();
    const data = {
        rut: inputRUT.value,
        email: inputEmail.value,
        name: inputName.value,
        lastName: inputLastName.value,
        age: inputAge.value,
        phone: inputPhone.value
    }
    console.log(data);
    try {
        const response = await fetch("http://127.0.0.1:8000/visitas", {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)         
        });

        if(response.ok){
            const jsonResponse = await response.json();
            console.log(jsonResponse);
        }
    } catch (error) {
        
    }    
}

// TODO Validate Email
function validateEmail(email){
    // Basic regex pattern for emails
    // const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // More complex regex pattern for emails
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
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
document.addEventListener('DOMContentLoaded', () => {
    
    submitButton.addEventListener('click', handleSubmit);
});