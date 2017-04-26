//filter through array made in client
//doesnt need to connect to db
window.onload = function(){
	$('input[type="text"]').keypress(function (e) {
		var code = e.keyCode || e.which;
		if ( code === 13 ){
			$("#searchButton").click();
		}
	});

	document.getElementById("searchButton").onclick = function(){
		search();
	};

	function search(){
		$.get("../../php/lecturer_course.php?course=" + 
			course_code + "_" + parallel_id, function (data) {
			$("#course_name").html(course_code);
			var lectures = data.split("|"); //remember to check if pop is needed
			var toAppend = "";
			var query = document.getElementById("searchQuery").value;

			var arrayLength = lectures.length;
			var match = false;
			var ctr = 1;

			for ( var i=0; i<arrayLength; i++){
			//case insensitive
				if ( lectures[i].toUpperCase().includes(query.toUpperCase()) ){
					match = true;
				}
			//when counter reaches 4, we have iterated through
			//a course and its corresponding values
				if ( (ctr % 3) === 0 && i !== 0){
					//if match is true, keep the array, set match to false
					if (match){
						match = false;
					//else set the element and prev 3 to null (entire course)
					} else{
						lectures[i] = null;
						lectures[i-1] = null;
						lectures[i-2] = null;
					}
				}
				ctr += 1;
			}
			//console.log(lectures);

			//create new array with remaining/queried elements (gets rid of null)
			var newArray = [];
				for (var x = 0; x < lectures.length-1; x+=3) {
					if (lectures[x]) {
				    	newArray.push(lectures[x]);
				    	newArray.push(lectures[x+1]);
				    	newArray.push(lectures[x+2]);
				    }
				}
				lectures = newArray;
			//remove current array from html
			$('.lecture').remove();

			for (var n = 0; n < lectures.length; n+=3) { //each iteration makes one complete lecture display with buttons/functionality
				var lecture_id = lectures[n].replace(/(\r\n|\n|\r)/gm,"");
				var date = lectures[n+1].replace(/(\r\n|\n|\r)/gm,"");
				var name = lectures[n+2].replace(/(\r\n|\n|\r)/gm,"");
				toAppend+= "<div class='lectureElement lecture row'>"; //link course name to statistics page
				if (name !== "") { //lectures with names have quizzes already
					toAppend += "<div class='col-md-7 col-xs-12'><p class='lectureInfo' " + lecture_id +"'>" + date + "</p>";
					toAppend += " <i class='lectureName'>" + name + "</i></div>";
					toAppend += " <div class='innerLecture col-md-5 col-xs-12'> " + createButtonString("view",lecture_id); //create view button value = lecture_id
					toAppend += " " + createButtonString("stats",lecture_id);
					toAppend += " " + createButtonString("delete",lecture_id); //create delete button value = lecture_id
				}
				else { //lecture does not have quiz
					toAppend += "<div class='lectureInfo col-md-6 col-xs-8'><p class='dateTime' " + lecture_id +"'>" + date + "</p> </div>";
					toAppend+= " " + createButtonString("upload", lecture_id); //only make var date if this case applies?
					//create upload button value = lecture_id + lecture.date (?)
				}
				toAppend+="</div></div><div class='line lecture'></div>"; //each lecture has its own, nameless div to linebreak break between lectures
			}
				//console.log(toAppend);
				$("#course_content").append(toAppend);
		});
	}
};

function createButtonString(type, lecture_id) { //remember functions are bound to buttons here 
	var buttonString = "";
	//"<button id='" + lecture_id + "' class='btn btn-md btn-primary' type='button'" ; //note: no end >
	switch(type) {
		case "view":
			buttonString += "<button class='viewQuiz btn btn-md-2 btn-default' type='button' id='viewQuiz'" ; //note: no end >
			buttonString += "value=" + lecture_id + " onclick = view_quiz(this)>View quiz</button>";
			console.log("create view", buttonString);
			break;
		case "delete":
			buttonString += "<button class='deleteQuiz btn btn-md-2 btn-default' type='button' id='deleteQuiz'" ; //note: no end >
			buttonString += "value=" +lecture_id + " onclick = delete_quiz(this)>Delete quiz</button>";
			break;
		case "stats":
			buttonString += "<button class='statsQuiz btn btn-md-2 btn-default' type='button' id='statsQuiz'" ; //note: no end >
			buttonString += "value=" +lecture_id + " onclick = \"window.location = 'statistics.php#" + lecture_id +"'\">View statistics</button>";
			break;
		case "upload":
			buttonString += "<form class='' action='../../php/upload.php' method='post' enctype='multipart/form-data' accept-charset='UTF-8'>" + 
								"<div class='col-md-6 col-xs-8'>" +
									"<input type='file' class='uploadField btn btn-default form-control' name='fileToUpload'>" + 
								"</div>" +
								"<div class='col-md-6 col-xs-4 button'>" +
									"<input type='submit' value='Upload' class='deleteFile uploadButton btn btn-md-2 btn-primary submitFile' name='submit' id='submitFile'>" +
									"<input type='hidden' name='lecture_id' value='" +lecture_id + "'>" +//gives php access to lecture id
								"</div></form>"; 
			break;
		default:
			console.log("something went wrong");
	}
	buttonString +=" ";
	return buttonString;
}
