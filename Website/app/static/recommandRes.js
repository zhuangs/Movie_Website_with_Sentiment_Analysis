$(document).ready(function(){
	$(".movieDetail").click(function(){
		var curDiv = $(this).find(".movieT").text();
		// alert("aaaaaaa");
		// alert(curDiv.text());
		// var movieName = curDiv.find("#movieT");

		window.location.href = "http://127.0.0.1:5000/movie?movieName="+curDiv;
		// alert(curDiv);
	});


	$("#socreBut").click(function(){
		//alert("aa");
		$("#score").show();
		$("#relevance").hide();
	});

	$("#releBut").click(function(){
		//alert("an");
		$("#score").hide();
		$("#relevance").show();
	});
});
