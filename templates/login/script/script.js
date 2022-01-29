const input = document.querySelectorAll('input');
const inputBox = document.querySelector('.form-log__idpw');

input.forEach((e) =>
  e.addEventListener('focus', () => {
    console.log('yes');
  })
);
