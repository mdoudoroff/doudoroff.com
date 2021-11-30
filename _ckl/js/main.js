
burgerOpen = false;

$( document ).ready(function(){

	$('#burger').click(function() {
		if (burgerOpen) {
			burgerOpen = false;
			$('#burger').css('transform','rotate(0deg)');
			$('#mainMenu').slideToggle(500);
		} else {
			burgerOpen = true;
			$('#burger').css('transform','rotate(90deg)');
			$('#mainMenu').slideToggle(500);
		}
	});

});
