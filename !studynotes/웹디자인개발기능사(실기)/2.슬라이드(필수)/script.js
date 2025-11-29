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
