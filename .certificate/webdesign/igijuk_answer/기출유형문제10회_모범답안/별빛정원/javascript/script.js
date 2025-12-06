// JavaScript Document

jQuery(document).ready(function(){

  $('.navi>li').mouseover(function(){        
	  $(this).find('.submenu').stop().slideDown(500);
  }).mouseout(function(){        
	  $(this).find('.submenu').stop().slideUp(500);
  });

  $(".notice li:first").click(function () {
    $("#modal").addClass("active");
  });
  $(".btn").click(function () {
    $("#modal").removeClass("active");
  });

  setInterval(function(){ 
    $('.slidelist').delay(1000);
    $('.slidelist').animate({marginLeft: 0});
    $('.slidelist').delay(2000);
    $('.slidelist').animate({marginLeft: '-100%'});
    $('.slidelist').delay(2000);
    $('.slidelist').animate({marginLeft: '-200%'});
    $('.slidelist').delay(2000);
  });

});
	

