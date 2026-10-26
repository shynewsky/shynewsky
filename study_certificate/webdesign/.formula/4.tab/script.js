$(function(){

    let tabBtn = $(".tab-btn > ul > li"); // 버튼 설정
    let tabCont = $(".tab-cont > div");   // 콘텐츠 설정

    tabCont.hide().eq(0).show(); // 첫번째 콘텐츠만 보이게 설정
    tabBtn.click(function(){
        const index = $(this).index(); // 클릭한 번호를 저장
        $(this).addClass("active").siblings().removeClass("active"); // 내가 클릭한 버튼에 클래스를 추가하고 나머지 버튼은 삭제
        tabCont.eq(index).show().siblings().hide(); // 내가 클릭한 버튼의 콘텐츠를 보여주고 나머지 콘텐츠는 숨김
    });
    
});

// 이기적 버전

// 탭 메뉴에서 클릭한 항목만 활성화되고, 다른 항목의 활성화는 해제되는 코드

// $('.tabmenu>li>a').click(function(){
//     $(this).parent().addClass("active")
//            .siblings().removeClass("active");
//     return false;
// });
