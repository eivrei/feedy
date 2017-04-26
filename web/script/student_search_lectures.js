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
		$.get("../../php/student_getCourse.php?course=" + 
			course_code + "_" + parallel_id, function (data) {
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
			for (var n = 0; n < lectures.length; n+=3) { //possibly -1 on length comparison
				var lecture_id = lectures[n].replace(/(\r\n|\n|\r)/gm,"");
				var date = lectures[n+1].replace(/(\r\n|\n|\r)/gm,"");
				var name = lectures[n+2].replace(/(\r\n|\n|\r)/gm,"");
				toAppend += "<div class='lectureElement lecture row'><div class='lectureInfo col-md-6 col-xs-12'><p " + lecture_id +"'>" + date + "</p>"; //link course name to statistics page
				if (name !== "") { //lectures with names have quizzes already
					toAppend += " <i class='lectureName'>" + name + "</i></div>";
					toAppend += " <div class='innerLecture col-md-5 col-xs-12'> "; //create view button value = lecture_id
					toAppend += " " + createTakeQuizButtonString(lecture_id); //create view button value = lecture_id
				}
				toAppend += "</div></div><div class='line lecture'></div>";
			}
			$("#course_content").append(toAppend);
		});
	}
};
function createTakeQuizButtonString(lecture_id) {
	var buttonString = "<button class='takeQuiz btn btn-md-2 btn-primary' type='button'" ; //note: no end >
	buttonString += "value=" + lecture_id + " onclick = take_quiz(this)>Take quiz";
	buttonString +="</button>";
	return buttonString;
}
