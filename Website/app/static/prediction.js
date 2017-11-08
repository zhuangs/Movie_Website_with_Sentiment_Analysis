$(document).ready(function(){
	$(".entry").click(function(){
		var movieName = $(this).children().eq(0).children().eq(1).text();
		alert(movieName);
		window.location.href = "http://127.0.0.1:5000/movie?movieName = "+movieName;
	})
});