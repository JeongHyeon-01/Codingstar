const btn = document.querySelector('.drop-down');
let isHidden = true;
btn.addEventListener('click', () => {
  const menu = document.querySelector('.drop-down__menu');
  const tap = document.querySelector('.tap');

  if (isHidden) {
    menu.classList.remove('hidden');
    tap.classList.remove('hidden');
    isHidden = false;
  } else {
    menu.classList.add('hidden');
    tap.classList.add('hidden');
    isHidden = true;
  }
});

const cross = document.querySelector('.search-bar__cross');
let search = document.querySelector('.search-input');

cross.addEventListener('click', () => {
  search.value = '';
  console.log('aa');
});
