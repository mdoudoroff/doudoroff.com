burgerOpen=!1,$(document).ready((function(){$("#burger").click((function(){burgerOpen?(burgerOpen=!1,$("#burger").css("transform","rotate(0deg)"),$("#mainMenu").slideToggle(300)):(burgerOpen=!0,$("#burger").css("transform","rotate(90deg)"),$("#mainMenu").slideToggle(300))}))}));