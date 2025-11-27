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
