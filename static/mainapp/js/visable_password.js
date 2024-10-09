document.addEventListener('DOMContentLoaded', function() {
    const togglePasswordButtonLogin = document.getElementById('togglePassword'),
          togglePasswordButtonReg1 = document.getElementById('togglePassword1'),
          togglePasswordButtonReg2 = document.getElementById('togglePassword2'),
        
          passwordInputLogin = document.getElementById('exampleInputPassword1'),
          passwordInputReg1 = document.getElementById('id_password1'),
          passwordInputReg2 = document.getElementById('id_password2');

    function togglePasswordVisibility(passwordInput, button) {
        const type = passwordInput.type === 'password' ? 'text' : 'password';

        passwordInput.type = type;
        button.innerHTML = type === 'password' ?
            '<i class="bi bi-eye"></i>' : '<i class="bi bi-eye-slash"></i>';
    }

    if (togglePasswordButtonLogin && passwordInputLogin) {
        togglePasswordButtonLogin.addEventListener('click', function() {
            togglePasswordVisibility(passwordInputLogin, togglePasswordButtonLogin);
        });
    }
    else {
        togglePasswordButtonReg1.addEventListener('click', function() {
            togglePasswordVisibility(passwordInputReg1, togglePasswordButtonReg1);
        });

        togglePasswordButtonReg2.addEventListener('click', function() {
            togglePasswordVisibility(passwordInputReg2, togglePasswordButtonReg2);
        });
    }
});