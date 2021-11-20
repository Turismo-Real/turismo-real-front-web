import { sha256 } from './SHA256.js';
import { validateEmail } from './validations.js'

window.onload = () => {
    const loginForm = document.querySelector('#loginForm');

    loginForm.addEventListener('submit', (e) => prepareToSendLogin(e));
    //btnLogin.addEventListener('click', () => prepareToSendLogin());

    // Pop up login
    document.querySelector("#show-login").addEventListener("click",function(){
        document.querySelector(".popup").classList.add("active");
    });
    document.querySelector(".popup .close-btn").addEventListener("click",function(){
        document.querySelector(".popup").classList.remove("active");
    });

    // Functions
    const prepareToSendLogin = (e) => {
        let email = document.querySelector('#email');
        let password = document.querySelector('#password');
        let isValidEmail = validateEmail(email.value);

        if(isValidEmail){
            let hashedPassword = sha256(password.value);
            createHiddenInput(hashedPassword);
        } else {
            console.log('correo no valido');
            e.preventDefault();
        }
    }

    const createHiddenInput = (message) => {
        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'password';
        hiddenInput.style.visibility = 'hidden';
        hiddenInput.name = 'hashedPassword';
        hiddenInput.value = message;
        loginForm.appendChild(hiddenInput);
    }
}