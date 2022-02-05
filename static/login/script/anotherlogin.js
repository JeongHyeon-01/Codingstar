const id = document.getElementById('id');
const password = document.getElementById('password');
const hit = document.querySelector('.input-pw');
const btn = document.getElementById('btn');
//* ---------------------------------------------------------------------
//아이디 1글자 비밀번호 5글자 이상 입력했을때만 로그인 버튼 활성화
function doAble() {
  const idValue = id.value;
  const pwValue = password.value;
  if (idValue.length >= 1 && pwValue.length > 5) {
    btn.disabled = false;
    btn.style.cursor = 'pointer';
  } else {
    btn.disabled = true;
    btn.style.cursor = 'default';
  }
}

id.addEventListener('keyup', doAble);
password.addEventListener('keyup', doAble);

//* ---------------------------------------------------------------------
// 실제 인스타그램 처럼 비밀번호 1글자 이상 쳤을시 비밀번호 표시 버튼 보이기
password.addEventListener('keyup', () => {
  const pwValue = password.value;
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
    password.setAttribute('type', 'text');
    hit.textContent = '숨기기';
    isTrue = false;
  } else {
    password.setAttribute('type', 'password');
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

//* ---------------------------------------------------------------------

// 로그인 fetch 함수
btn.addEventListener('click', (e) => {
  e.preventDefault();

  const req = {
    id: id.value,
    password: password.value,
  };
  console.log('사용자정보', req);

  fetch('백엔드 API 주소', {
    method: 'POST',
    body: JSON.stringify(req),
  })
    .then((res) => res.json())
    .then((res) => {
      if (res.success) {
        location.href = '/main';
      } else {
        alert(res.msg);
      }
    })
    .catch((err) => {
      console.error('로그인 실패');
    });
});
