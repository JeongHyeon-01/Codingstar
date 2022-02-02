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
