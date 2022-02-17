const email = document.getElementById('email');
const name = document.getElementById('name');
const username = document.getElementById('username');
const password = document.getElementById('password');
const hit = document.querySelector('.input-pw');
const btn = document.getElementById('btn');

//* ---------------------------------------------------------------------
//아이디 1글자, 닉네임 자 이상 1글자, 비밀번호 5글입력했을때만 로그인 버튼 활성화
function doAble() {
  const emailValue = email.value;
  const pwValue = password.value;
  const usernameValue = username.value;

  if (emailValue.length >= 1 && usernameValue.length >= 1 && pwValue.length > 5) {
    btn.disabled = false;
    btn.style.cursor = 'pointer';
  } else {
    btn.disabled = true;
    btn.style.cursor = 'default';
  }
}

email.addEventListener('keyup', doAble);
username.addEventListener('keyup', doAble);
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
// 회원가입 api 연결
// btn.addEventListener('click', (e) => {
//   e.preventDefault();
//
//   const req = {
//     email: email.value,
//     name: name.value,
//     id: id.value,
//     password: password.value,
//   };
//   console.log('사용자정보', req);
//
//   fetch('백엔드 API 주소', {
//     method: 'POST',
//     body: JSON.stringify(req),
//   })
//     .then((res) => res.json())
//     .then((res) => {
//       if (res.success) {
//         location.href = '/users';
//       } else {
//         alert(res.msg);
//       }
//     })
//     .catch((err) => {
//       console.error('회원가입 실패');
//     });
// });
