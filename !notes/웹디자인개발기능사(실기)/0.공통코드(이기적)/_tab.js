// 탭 메뉴에서 클릭한 항목만 활성화되고, 다른 항목의 활성화는 해제되는 코드

$('.tabmenu>li>a').click(function(){
    $(this).parent().addClass("active")
           .siblings().removeClass("active");
    return false;
});
