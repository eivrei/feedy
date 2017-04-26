//globals only exist because the code was updated when there was no time to rewrite for proper objects and local variables
//CODE CHECKERS - the line above is a justification, not a "real" comment. Consider removing
var lecture_id = window.location.hash.substr(1);
var progress = 0;
var chosenTopics = [];
var numAnswered = 0;
var presentKeywordIds = [];

$(document).ready(function() {
	$.get("../../php/student_getQuiz.php?id=" + lecture_id, function (data) {
		if (data != "NO DATA") {
			var allTopics = make_allTopics(data);
			chosenTopics = take_random(allTopics,4); //last number is how many random questions each student answers
			get_bind_keywords(get_bind_callback); //chosenTopics is currently global, if not an argument is needed (and function update)
			document.getElementById("topic-text").append(chosenTopics[0].topicText); //move one up for load speed
			//set initial progress bar state
			set_progress();
		}
		else {
		console.log("NO DATA");
		}
	});
});

//returns array in format chosen[i]={text:" ", id:x};
function take_random(allTopics, numToChoose) {
	//take 5 random
	var pickedNumbers = []; //avoid redeclaring in loop
	var randomNum;
	var wasFound;
	var i = 0;
	while (i < numToChoose) {
		randomNum = getRandomInt(0, allTopics.length);
		//appearantly faster than indexOf
		for (var j = 0; j < pickedNumbers.length; j++) {
			if (randomNum == pickedNumbers[j]) {
				wasFound = true;
			}
		}
		if (!wasFound) {
			i++;
			pickedNumbers.push(randomNum);
		}
		wasFound = false;
	}
	var chosenTopics = [];
	for (var j = 0; j < numToChoose; j++) {
		chosenTopics.push(allTopics[pickedNumbers[j]]);
	}
	return chosenTopics;
}

//onclick for send button (quiz.php)
function topic_answered() {
	//do stuff like check validity and sending answer to db
	if (document.getElementById("answer-input").value.replace(/^\s+|\s+$/g,"") === ""){
		alert("Missing some text here");
	}else{
		check_correctness();
		change_topic();
	}
}

//checks per topic (on clicking "send"
function check_correctness() {
	var answerText = document.getElementById("answer-input").value;
	var answerSplit = answerText.split(" ");
	var weightTotal = 0; //sums weight of matching user input matching keywords
	var keywords = [];
	var toCheck;
	//brute force, but should be okay with the low amount of keywords we expect
	for (var i = 0; i < answerSplit.length; i++) {
		for (var j = 0; j < chosenTopics[numAnswered].keywords.length; j++) {
			keywords.push(chosenTopics[numAnswered].keywords[j].keyword);
		}
		toCheck = $.inArray(answerSplit[i], keywords);
		if (toCheck != -1) {
			weightTotal += parseInt(chosenTopics[numAnswered].keywords[toCheck].weight);
			presentKeywordIds.push(chosenTopics[numAnswered].keywords[toCheck].id);
		}
	}
	chosenTopics[numAnswered].answerWeightSum = weightTotal;
}

//needs to handle what to do when all topics are answered
function change_topic() {
	if (numAnswered < chosenTopics.length -1) {
		//update progress bar
		numAnswered++; //global
		set_progress();
		//reset input in text area
		document.getElementById("answer-input").value="";
		//change topic in header
		document.getElementById("topic-text").innerHTML = chosenTopics[numAnswered].topicText;
		if (numAnswered == chosenTopics.length -1){
			document.getElementById("send-button").innerHTML = "Finish";
		}
	}
	else {
		send_final();
	}
}

function make_allTopics(data) {
	var datasplit = data.split("|"); 
	datasplit.pop(); //removes final "|" 
	var allTopics = [];
	for (var i = 0; i < datasplit.length; i+=2) {
		allTopics.push({
			topicText: datasplit[i],
			id: datasplit[i+1],
			keywords:[],
			answerWeightSum: 0
		});
	}
	return allTopics;
}

//courtesy of Mozilla Developers Network
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

function get_bind_keywords(callback) {
	var idArray = [];
	for (var i = 0; i < chosenTopics.length; i++) {
		idArray.push(chosenTopics[i].id);
	}
	//callback is get_bind_callback, shortened for convenience
	$.ajax({
       type: "POST",
       url: "../../php/student_getKeywords.php",
       datatype: 'JSON',
       data: {idArray: JSON.stringify(idArray)},
       success: function(data){
		   //bind keywords
		   data = data.split("|");
		   data.pop();
		   callback(data, idArray);
        },
       failure: function(errMsg) {																					
            console.error("error:",errMsg);
       }
    });
	return chosenTopics;
}
//necessary for async ajax
function get_bind_callback(data,idArray) {
    var crntId;
	for (var i = 0; i < chosenTopics.length; i++) {
		crntId = idArray[i];
		for (var j = 0; j < data.length; j+=4) {
			if (crntId == data[j]) {
			chosenTopics[i].keywords.push({
			keyword: data[j+1],
			id: data[j+2],
			weight: data[j+3],
			answered: true
			});
		}
	   }
	}
}

function set_progress() {
	var percentageDone = Math.floor(((numAnswered+1)/chosenTopics.length) * 100);
	var styleString = "width:" + percentageDone.toString() + "%";
	document.getElementById("quiz-progress").setAttribute("aria-valuenow", percentageDone);
	document.getElementById("quiz-progress").setAttribute("style", styleString);
	document.getElementById("progress-text").innerHTML = (numAnswered+1) + "/" + chosenTopics.length ;
}

//prep data and send
function send_final() {
	var weightMax;
	var correctPercent;
	var quizResult = {
					topics: [],
					keywords: []
					};
	//probably not the best way to do this
	for (var i = 0; i < chosenTopics.length; i++) {
		weightMax = 0;
		for (var j = 0; j < chosenTopics[i].keywords.length;j++) {
			weightMax += parseInt(chosenTopics[i].keywords[j].weight);
		}
		correctPercent = Math.round( (chosenTopics[i].answerWeightSum/weightMax)*100);
		quizResult.topics.push({
			id: chosenTopics[i].id, 
			correctPercent: correctPercent
		});
	}
	quizResult.keywords = presentKeywordIds; //id's are unique, no need to connect with topics
	//send data to db
	$.ajax({
       type: "POST",
       url: "../../php/student_sendQuiz.php",
       datatype: 'JSON',
       data: {quizResult: JSON.stringify(quizResult)},
       success: function(data){
		   var alertText = "Your results:\n";
		   for(var k = 0; k < chosenTopics.length; k++) {
			   alertText += chosenTopics[k].topicText + ": " + quizResult.topics[k].correctPercent +"%\n";
		   }
		   alert(alertText);
		   history.back();
        },
       failure: function(errMsg) {																					
            console.error("error:",errMsg);
       }
  	});
}