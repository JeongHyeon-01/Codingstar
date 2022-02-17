// 모달 띄우기 코드
const modal = document.getElementById("modal_add_feed");
const buttonAddFeed = document.getElementById("add_feed");
buttonAddFeed.addEventListener("click", e => {
    modal.style.top = window.pageYOffset + 'px'; // top을 이용해 시작 y위치를 바꿔줌
    modal.style.display = "flex";
    document.body.style.overflowY = "hidden"; // 스크롤 없애기
});

<!-- jquery 부분 -->

$('.close_modal').on("click", () => {
    closeModal();
});

$('.go_home').on("click", () => {
    location.replace('/');
});

function closeModal() {
    $('.modal').css({
        display: 'none'
    });
    $(document.body).css({
        overflowY: 'visible'
    });
};

$('.modal_image_upload')
    .on("dragover", dragOver)
    .on("dragleave", dragOver)
    .on("drop", uploadFiles);

function dragOver(e) {
    e.stopPropagation();
    e.preventDefault();

    if (e.type == "dragover") {
        $(e.target).css({
            "background-color": "black",
            "outline-offset": "-20px"
        });
    } else {
        $(e.target).css({
            "background-color": "white",
            "outline-offset": "-10px"
        });
    }
};

let files;

function uploadFiles(e) {
    e.stopPropagation();
    e.preventDefault();
    console.log(e.dataTransfer)
    console.log(e.originalEvent.dataTransfer)

    e.dataTransfer = e.originalEvent.dataTransfer;

    files = e.dataTransfer.files;
    if (files.length > 1) {
        alert('하나만 올려라.');
        return;
    }

    if (files[0].type.match(/image.*/)) {
        $('#modal_add_feed_content').css({
            display: 'flex'
        });
        $('.modal_image_upload_content').css({
            "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
            "outline": "none",
            "background-size": "contain",
            "background-repeat": "no-repeat",
            "background-position": "center"
        });
        $('#modal_add_feed').css({
            display: 'none'
        })
    } else {
        alert('이미지가 아닙니다.');
        return;
    }
};

$('#button_write_feed').on('click', () => {
    let file = files[0];
    let image = files[0].name;
    let content = $('#input_feed_content').val();
    let user_id = $('#input_user_id').val();
    let profile_image = $('#input_profile_image').val();


    let fd = new FormData();

    fd.append('file', file);
    fd.append('image', image);
    fd.append('content', content);
    fd.append('profile_image', profile_image);
    fd.append('user_id', user_id);

    $.ajax({
        url: "./upload",
        data: fd,
        method: "post",
        processData: false,
        contentType: false,
        success:function (data){
            console.log('성공')
        },
        error:function (request, status, error){
            console.log('실패')
        },
        complete:function (){
            console.log('완료')
            closeModal();
            location.reload();

        }
    })
});




//     if (image.length <= 0) {
//         alert("이미지가 비어있습니다.");
//     } else if (content.length <= 0) {
//         alert("설명을 입력하세요");
//     } else if (profile_image.length <= 0) {
//         alert("프로필 이미지가 비어있습니다.");
//     } else if (user_id.length <= 0) {
//         alert("사용자 id가 없습니다.");
//     } else {
//         writeFeed(fd);
//         console.log(files[0]);
//     }
//
//
// function writeFeed(fd) {
//     $.ajax({
//         url: "/content/upload",
//         data: fd,
//         method: "POST",
//         processData: false,
//         contentType: false,
//         success: function (data) {
//             console.log("성공");
//         },
//         error: function (request, status, error) {
//             console.log("에러");
//         },
//         complete: function () {
//             console.log("무조건실행");
//             closeModal();
//             location.reload();
//         }
//     })
// }