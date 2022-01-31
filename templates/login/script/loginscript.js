const id = document.getElementById('id');
const pw = document.getElementById('pw');
const hit = document.querySelector('.input-pw');
const loginBtn = document.getElementById('login');
//* ---------------------------------------------------------------------
//아이디 1글자 비밀번호 5글자 이상 입력했을때만 로그인 버튼 활성화
function doAble() {
  const idValue = id.value;
  const pwValue = pw.value;
  if (idValue.length >= 1 && pwValue.length > 5) {
    loginBtn.disabled = false;
    loginBtn.style.cursor = 'pointer';
  } else {
    loginBtn.disabled = true;
    loginBtn.style.cursor = 'default';
  }
}

id.addEventListener('keyup', doAble);
pw.addEventListener('keyup', doAble);

//* ---------------------------------------------------------------------
// 실제 인스타그램 처럼 비밀번호 1글자 이상 쳤을시 비밀번호 표시 버튼 보이기
pw.addEventListener('keyup', () => {
  const pwValue = pw.value;
  if (pwValue.length >= 1) {
    hit.classList.remove('hidden');
  } else {
    hit.classList.add('hidden');
  }
});

//* ---------------------------------------------------------------------
// 비밀번호 표시 버튼 클릭하면 password가 text 로 바뀌면서 비밀번호 표시
// 한번 더 클릭하면 다시 비밀번호로 바뀜
let isTrue = true;
hit.addEventListener('click', () => {
  if (isTrue) {
    pw.setAttribute('type', 'text');
    hit.textContent = '숨기기';
    isTrue = false;
  } else {
    pw.setAttribute('type', 'password');
    hit.textContent = '비밀번호 표시';
    isTrue = true;
  }
});

//* ---------------------------------------------------------------------
// 실제 인스타그램과 동일한 로그인 화면 이미지 전환
const imgOne = document.querySelector('img:nth-child(1)');
const imgTwo = document.querySelector('img:nth-child(2)');
const imgThree = document.querySelector('img:nth-child(3)');
const imgFour = document.querySelector('img:nth-child(4)');
const imgFive = document.querySelector('img:nth-child(5)');

const oneImg = () => {
  console.log(1);
  imgFive.classList.remove('one');
  imgOne.classList.remove('two');
  imgOne.classList.add('one');
  imgTwo.classList.add('two');
  setTimeout(twoImg, 5000);
};

const twoImg = () => {
  imgOne.classList.remove('one');
  imgTwo.classList.remove('two');
  imgTwo.classList.add('one');
  imgThree.classList.add('two');
  setTimeout(threeImg, 5000);
};

const threeImg = () => {
  imgTwo.classList.remove('one');
  imgThree.classList.remove('two');
  imgThree.classList.add('one');
  imgFour.classList.add('two');
  setTimeout(fourImg, 5000);
};

const fourImg = () => {
  imgThree.classList.remove('one');
  imgFour.classList.remove('two');
  imgFour.classList.add('one');
  imgFive.classList.add('two');
  setTimeout(fiveImg, 5000);
};

const fiveImg = () => {
  imgFour.classList.remove('one');
  imgFive.classList.remove('two');
  imgFive.classList.add('one');
  imgOne.classList.add('two');
};

oneImg();
setInterval(oneImg, 25000);
