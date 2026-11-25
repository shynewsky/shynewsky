$(function(){

    $(".popup-btn").click(function(){
        $(".popup-view").show();
    });
    $(".popup-close").click(function(){
        $(".popup-view").hide();
    });

});

// 이기적 버전

// 클릭 이벤트로 클래스 토글

// $(".notice li:first").click(function(){
//     $("#popup").addClass("active");
// });
// $(".btn").click(function(){
//     $("#popup").removeClass("active");
// });
