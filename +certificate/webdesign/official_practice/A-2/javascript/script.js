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

})
