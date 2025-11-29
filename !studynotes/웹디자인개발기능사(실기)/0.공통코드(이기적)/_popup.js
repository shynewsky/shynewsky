// 클릭 이벤트로 클래스 토글

$(".notice li:first").click(function(){
    $("#popup").addClass("active");
});
$(".btn").click(function(){
    $("#popup").removeClass("active");
});
