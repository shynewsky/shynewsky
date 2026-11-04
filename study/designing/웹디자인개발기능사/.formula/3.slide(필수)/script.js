// FadeIn, FadeOut

$(function(){

    let currentIndex = 0;
    setInterval(function(){
        let nextIndex = (currentIndex + 1) % 3;
        $(".slide").eq(currentIndex).fadeOut(1200);
        $(".slide").eq(nextIndex).fadeIn(1200);        
        currentIndex = nextIndex;
    }, 3000);
    
});

// 좌로 이동
// 위로 이동

$(function(){

    let currentIndex = 0;
    $(".sliderWrap").append($(".slide").first().clone(true));

    setInterval(function(){
        currentIndex++;
        $(".sliderWrap").animate({marginLeft: -currentIndex * 100 + "%"}, 600);    // 좌로 이동
        // $(".sliderWrap").animate({marginTop: -currentIndex * 350 + "px"}, 600); // 위로 이동
        // $(".sliderWrap").animate({marginTop: -currentIndex * 100 + "vh"}, 600); // 위로 이동(반응형)

        if(currentIndex == 3){
            setTimeout(function(){  
                $(".sliderWrap").animate({marginLeft: 0}, 0);    // 좌로 이동
                // $(".sliderWrap").animate({marginTop: 0}, 0); // 위로 이동
                currentIndex = 0;
            }, 700);
        }
    }, 3000);
    
});

// 이기적 버전

// 첫 번째 이미지를 제외한 나머지는 숨기고 순서대로 페이드 인·아웃하며 이미지를 순환하는 코드

// $('.imgslide a:gt(0)').hide();
// setInterval(function(){
//     $('.imgslide a:first-child').fadeOut()
//        .next('a').fadeIn()
//        .end().appendTo('.imgslide');
// });

// 리스트가 일정 간격으로 위로 이동하다가 마지막에 다시 처음 위치로 돌아가는 세로 슬라이드 애니메이션 코드

// setInterval(function(){ 
//     $('.slidelist').delay();
//     $('.slidelist').animate({marginTop:}); 
//     $('.slidelist').delay();
//     $('.slidelist').animate({marginTop:}); 
//     $('.slidelist').delay();
//     $('.slidelist').animate({marginTop:0}); 
// });
