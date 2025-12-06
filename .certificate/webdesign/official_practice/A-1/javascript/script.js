$(function(){

    // M-2
    $('.nav > ul > li').mouseover(function(){
        $('.nav > ul > li > ul').stop().slideDown(200);
    })
    $('.nav>ul>li').mouseout(function(){
        $('.nav > ul > li > ul').stop().slideUp(200);
    })

    // S-3
    let currentIndex=0;
    $('.sliderWrap').append($('.slide').first().clone(true));
    setInterval(function(){
        currentIndex++;
        $('.sliderWrap').animate({marginTop: -currentIndex * 350 + 'px'}, 600);
        if(currentIndex==3){
            setTimeout(function(){
                $('.sliderWrap').animate({marginTop: 0}, 0);
                currentIndex = 0;
            }, 700);
        }
    }, 3000);

    // T-1
    let tabBtn = $('.tab-btn > ul > li');
    let tabCont = $('.tab-cont > div');
    tabCont.hide().eq(0).show();
    tabBtn.click(function(){
        const index = $(this).index();
        $(this).addClass('active').siblings().removeClass('active');
        tabCont.eq(index).show().siblings().hide();
    });

    // P-1
    $(".popup-btn").click(function(){
        $(".popup-view").show();
    });
    $(".popup-close").click(function(){
        $(".popup-view").hide();
    });

});