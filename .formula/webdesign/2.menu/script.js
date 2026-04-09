$(function(){

    $(".nav>ul>li").mouseover(function(){
        $(this).find(".submenu").stop().slideDown(); // 개별 서브메뉴 열때
        $('.nav>ul>li>ul').stop().slideDown();       // 단체 서브메뉴 열때
        //$("#header").addClass("on");                 // +가로메뉴 배경열기
        //$("#main").addClass("on");                   // +세로메뉴 배경열기
    });
    $(".nav>ul>li").mouseout(function(){
        $(this).find(".submenu").stop().slideUp();  // 개별 서브메뉴 닫을때
        $('.nav>ul>li>ul').stop().slideUp();        // 단체 서브메뉴 닫을때
        //$("#header").removeClass("on");             // +가로메뉴 배경닫기
        //$("#main").removeClass("on");               // +세로메뉴 배경닫기
    });

});

// 이기적 버전

// 서브메뉴가 내려가고, 마우스를 떼면 서브 메뉴가 올라가는 코드

// $('.navi>li').mouseover(function(){
//     $(this).find('.submenu').stop().slideDown();
// }).mouseout(function(){
//     $(this).find('.submenu').stop().slideUp();
// });

// 메뉴에 마우스를 올리면 서브메뉴와 배경이 내려가고, 마우스를 떼면 서브메뉴와 배경이 올라가는 코드

// $('.navi>li').mouseover(function(){
//     $('.submenu').stop().slideDown();
//     $('#menu_bg').stop().slideDown();
// }).mouseout(function(){
//     $('.submenu').stop().slideUp();
//     $('#menu_bg').stop().slideUp();
// });

