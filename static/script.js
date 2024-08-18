const loginr = document.querySelector('.login-section')
const login_link = document.querySelector('.login-link')
const register_link = document.querySelector('.register-link')

register_link.addEventListener('click',() =>{
  loginr.classList.add('active')
});

login_link.addEventListener('click',() =>{
  loginr.classList.remove('active')
});