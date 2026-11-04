// JavaScript Document

jQuery(document).ready(function(){

  $('.navi>li').mouseover(function(){        
	  $(this).find('.submenu').stop().slideDown(500);
  }).mouseout(function(){
	  $(this).find('.submenu').stop().slideUp(500);
  });
  
  setInterval(function(){ 
  $('.slidelist').delay(2000);
  $('.slidelist').animate({marginLeft:-800});
  $('.slidelist').delay(2000);
  $('.slidelist').animate({marginLeft:-1600});
  $('.slidelist').delay(2000);
  $('.slidelist').animate({marginLeft:0});
  $('.slidelist').delay(2000);
  });
  
  $(".notice li:first").click(function(){
	$("#modal").addClass("active");
  });
  $(".btn").click(function(){
	$("#modal").removeClass("active");
  });  

});


