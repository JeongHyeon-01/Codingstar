# Codingstar

드디어 완료했네요 긴시간 다들 고생많았습니다 

- 미구현 목록 
    - 마이페이지 저장됨 태그됨 페이지 



- 현재 구현 목록 ( 로그인 회원가입 로그아웃 피드 올리기 (계정별)
    - 로그인
    - 회원가입
    - 로그아웃
    - 피드올리기(계정별)
    - 프로필사진 올리기
    - 프로필 사진 변경시 기존 피드에ㅐ 업로드 완료
    - Default프로필사진 완료
    - 댓글
    - 좋아요
    - 친구추천 목록 수정
    - 스토리 부분 수정(프로필 사진만 나오게끔)


이정도 구현 해두었고
실행방법 적어드리겠습니다.
1. 가상환경이 설치가 되어있는지 확인 한다 . 설치 가 되어있지 않다면 virtualenv venv 입력 (venv라는 가상환경 설치) - > source venv/bin/acitvate 입력 -> 터미널창에 (venv)(base)라는 문구가 왼쪽에 
붙어있으면 성공
2. pip install -r requirements.txt  을 터미널에 입력한다
3. 터미널에서 python manage.py runserver 실행!
이후 문의사항은 슬랙에 문의

수정해야할 목록
1. 프로필 사진 변경부분 CSS 다시 해주세요 
2. 메인페이지 - 댓글 (게시 부분 현재 아무글씨도 안써지면 alert올라오는데 음.. .if (length >=1) 일때 색상 변경으로 활성화 되게 해주면 될듯합니다,.. 변경해서 죄송합니다..
3. 메인페이지 피드 사진 부분하고 뒤에 article부분이 살짝? 떠있는것같습니다… 아니면 말구요
4. 메인페이지 피드 업로드 부분 modal 새로 달아 두었습니다. 혹시 시간이 괜찮으시다면 디자인 수정 부탁드립니다. 
    1. Modal.js 및 main.html, modal.css 에 있습니다
5. 메인페이지 562 번째줄… replace안하고 등록되게 해주세요
6. 팔로우부분 본인이름 제외하고 나오게 if문 걸어야할듯



20220217 메인페이지 부분 수정완료 -정현
