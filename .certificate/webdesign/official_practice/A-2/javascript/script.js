$(function(){

    //M-3
    $('.nav > ul > li').mouseover(function(){
        $('.nav > ul > li > ul').stop().slideDown(900);
        $('#header').addClass('on');
    });
    $('.nav > ul > li').mouseout(function(){
        $('.nav > ul > li > ul').stop().slideUp(900);
        $('#header').removeClass('on');
    });

    // S-2
    let currentIndex = 0;
    $(".sliderWrap").append($(".slide").first().clone(true));
    setInterval(function(){
        currentIndex++;
        $(".sliderWrap").animate({marginLeft: -currentIndex * 100 + "%"}, 600);    // 좌로 이동

        if(currentIndex == 3){
            setTimeout(function(){  
                $(".sliderWrap").animate({marginLeft: 0}, 0);    // 좌로 이동
                currentIndex = 0;
            }, 700);
        }
    }, 3000);

    // P-1
    $(".popup-btn").click(function(){
        $(".popup-bg").show();
        $(".popup-view").show();
    });
    $(".popup-close").click(function(){
        $(".popup-bg").hide();
        $(".popup-view").hide();
    });
    
});
