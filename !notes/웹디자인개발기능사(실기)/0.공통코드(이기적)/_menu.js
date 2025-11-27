// 서브메뉴가 내려가고, 마우스를 떼면 서브 메뉴가 올라가는 코드

$('.navi>li').mouseover(function(){
    $(this).find('.submenu').stop().slideDown();
}).mouseout(function(){
    $(this).find('.submenu').stop().slideUp();
});

// 메뉴에 마우스를 올리면 서브메뉴와 배경이 내려가고, 마우스를 떼면 서브메뉴와 배경이 올라가는 코드

$('.navi>li').mouseover(function(){
    $('.submenu').stop().slideDown();
    $('#menu_bg').stop().slideDown();
}).mouseout(function(){
    $('.submenu').stop().slideUp();
    $('#menu_bg').stop().slideUp();
});
