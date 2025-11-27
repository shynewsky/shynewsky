// 첫 번째 이미지를 제외한 나머지는 숨기고 순서대로 페이드 인·아웃하며 이미지를 순환하는 코드

$('.imgslide a:gt(0)').hide();
setInterval(function(){
    $('.imgslide a:first-child').fadeOut()
       .next('a').fadeIn()
       .end().appendTo('.imgslide');
});

// 리스트가 일정 간격으로 위로 이동하다가 마지막에 다시 처음 위치로 돌아가는 세로 슬라이드 애니메이션 코드

setInterval(function(){ 
    $('.slidelist').delay();
    $('.slidelist').animate({marginTop:}); 
    $('.slidelist').delay();
    $('.slidelist').animate({marginTop:}); 
    $('.slidelist').delay();
    $('.slidelist').animate({marginTop:0}); 
});
