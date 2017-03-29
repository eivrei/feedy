function handle_login(data, username){
	console.log("data:" + data + " username: " + username);
	if (data != "WRONG") {
				setCookie("Username", username);
				window.location.href = "lecturer/courses.html"; 
				console.log(document.cookie);
	}	
	else if (data == "WRONG"){
		document.getElementById("errorfield").innerHTML = "Whoa there, something went wrong. Are you sure you typed username and password correctly :-)?";
	}
}


$(document).ready(function(){
			
	$("#loginSubmit").click(function(){
		var username = $("#inputUsername").val(); //could not pass jquery-object for some reason
		$.post("../php/login.php" , "username=" + $("#inputUsername").val() + "&password=" + $("#inputPassword").val(), function(data, status){
		handle_login(data, username);
		});
	});
	$('#password').keypress(function(e){
		if(e.which == 13){
			$('#loginSubmit').click();
		}
	});
});


function setCookie(c_name, value/*, exdays*/)  
{  
    //var exdate = new Date();  
    //exdate.setDate( exdate.getDate() + exdays );  
    var c_value = escape( value);  
    document.cookie = c_name + "=" + c_value + "; path=/";  
} 

function delete_cookie(name) {
	document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

function handle_logout() { //should be moved
	delete_cookie("Username");
	window.location.href = "index.html";
}

	
