var lecture_id = window.location.hash.substr(1);

$(document).ready(function() {

	$.get("../../php/lecturer_getStatsHeadinfo.php?lecture=" + lecture_id, function (data){
		console.log(data);
		var dateAndTime = data.split("|");
		var date = dateAndTime[0];		
		var name = dateAndTime[1];
		var toReplace = ""; //probably unneeded step
		toReplace += date + " <i>" + name + "</i>";
		$("#lecture_name").html(toReplace);
	});

	
	$.get("../../php/lecturer_getStatistics.php?lecture=" + lecture_id, function (data) {
		
		if (data != "NO DATA") {
			//var statArray = data.split("|"); 
			createStatString(data); //if on data length?
		}
		else {
			console.log(data); //why?
		}

	});	
});

//check if parameter works

function createStatString(statArray) {
	toAppend="";
	var dataSets = statArray.split("]");
	dataSets.pop();
	console.log(dataSets);
	var currentSet;
	var name, numAnswers, percentage, spread;
	var keywords = [];
	
	//process data into relevant datasets
	for (var i = 0; i < dataSets.length; i++) { //for each [ ] block in stat array
		currentSet = dataSets[i].split(",");
		var name, numAnswers, percentage, spread;
		var keywords = [];

		for (var j = 0; j < currentSet.length; j++) { //for each comma-separeted element in currentSet
			
			switch(j) {
				case 0:
					name = currentSet[j];
					name = name.substr(1);
					break;
				case 1:
					numAnswers = currentSet[j];
					break;
				case 2:
					percentage = currentSet[j];
					break;
				case 3:
					spread = currentSet[j];
					break;
				default: //happens on j > 3, assumes correct data
					keywords.push(currentSet[j]);
			}
		}
		toAppend+=createDataSetString(name, numAnswers, percentage, spread, keywords);
	}
	$("#stats_content").append(toAppend);
}

//for later: Make arguments an array instad
function createDataSetString(name, numAnswers, percentage, spread, keywords) {
	var dataSetString = "";
	dataSetString += "<h3>" + name + "</h3>";
	dataSetString += "<ul>";
	dataSetString += "<li> Answers: " + numAnswers + "</li>";
	dataSetString += "<li> Average correctness percentage: " + percentage + "</li>";
	dataSetString +="<li>Spread: " + spread + "</li>";
	dataSetString +="<li> Keywords found in < 20% of answers: " + keywords + "</li>";
	dataSetString += "</ul>";
	return dataSetString;
}

