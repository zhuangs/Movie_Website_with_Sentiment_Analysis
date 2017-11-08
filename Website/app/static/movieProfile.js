$(document).ready(function(){
	$(".re").click(function(){
		var movieName = $(this).children().eq(1).text().trim();
		window.location.href = "http://127.0.0.1:5000/movie?movieName="+movieName;
	})
});