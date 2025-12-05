$(function(){

    // M-2
    $('.nav > ul > li').mouseover(()=>{
        $('.nav > ul > li > ul').stop().slideDown(200);
    })
    $('.nav>ul>li').mouseout(()=>{
        $('.nav > ul > li > ul').stop().slideUp(200);
    })

    // S-3
    let currentIndex=0;
    $('.sliderWrap').append($('.slider').first().clone(true));
    setInterval(() => {
        currentIndex++;
        $('.sliderWrap').animate({marginTop: -currentIndex * 350 + 'px'}, 600);
        if(currentIndex==3){
            setTimeout(() => {
                $('.sliderWrap').animate({marginTop: 0}, 0);
                currentIndex = 0;
            }, 700);
        }        
    }, 3000);

})