var hash = window.location.hash.substr(1);
hash = hash.split("_");
var topic_id = hash[0];
var lecture_id = hash[1];
var course_code = hash[2];
var parallel_id = hash[3];

$(document).ready(function() {
    $.get("../../php/lecturer_getTopicKeywords.php?topic=" + topic_id, function (data) {
        if (data !== "NO DATA|NO DATA") {
            data = data.split("|");
            createTopicPreview(data);
        }
        else{
            console.log("No data");
        }
    });
    document.getElementById("edit_form").addEventListener('submit', function(e) {
        submitForm();
        e.preventDefault();
    }, false);
});

function createTopicPreview(data){
    var appendString = "";
    var topic_id = data.splice(0, 1);
    var topic = data.splice(0, 1);

    // Add topic on the top of the page
    appendString += '<div class="row">';
    appendString += '<div class="textInput col-md-3 col-xs-8">';
    appendString += '<input type="text" name="' + topic_id + '" value="' + topic + '" style="font-size: 24px; font-weight: bold" required pattern="[a-zA-Z0-9\- ]+">';
    appendString += '</div></div>';

    for(var i = 0; i < data.length; i+= 3) {
        var keyword_id = data[i];
        var keyword = data[i+1];
        var weight = data[i+2];

        //TODO: mobile phone compatability
        // Add all keywords with weights and a checkbox for each keyword
        appendString += '<div class="row">';
        appendString += '<div class="textInput col-md-2 col-xs-2"><input type="text" name="' + keyword_id + '" value="' + keyword + '" required pattern="[a-zA-ZæøåÆØÅ0-9\-]+"></div>';
        appendString += '<div class="textInput col-md-1 col-xs-2"><input type="text" name="' + keyword_id + '" value="' + weight + '" required pattern="^[0-9]|[0-2][0-9]|3[0]$" style="width: 30px; text-align: center"></div>';
        appendString += '<div class="checkBox col-md-9 col-xs-4"><input type="checkbox" name="' + keyword_id + '">Delete<br></div>';
        appendString += "</div>";
    }
    appendString += "<input id='submitButton' class='btn btn-success' type='submit' value='Submit changes'>";
    appendString += "<input class='btn btn-default' type='reset' value='Reset'>";
    $("#edit_form").append(appendString);
}

function submitForm() {
    var form_data = [];
    var form = document.getElementById("edit_form");
    var num_to_delete = 0;
    for(var i = 0; i < form.length - 1; i++){
        switch(form[i].type){
            case "text":
                if(form_data.indexOf(form[i].name) === -1){
                    form_data.push(form[i].name);
                }
                form_data.push(form[i].value);
                break;

            case "checkbox":
                form_data.push(form[i].checked);
                if(form[i].checked === true){
                    num_to_delete ++;
                }
                break;
        }
    }

    // Must have at least 3 keywords for the quiz to work properly
    if(form_data.length - (num_to_delete * 4) < 14){
        alert("Cannot delete more keywords.\nConsider using the 'delete topic'-button instead");
    }else{
        $.get("../../php/lecturer_editTopic.php?array=" + JSON.stringify(form_data), function (data) {
            console.log(data);
            window.location = "quiz_preview.php#" + lecture_id + "_" + course_code + "_" + parallel_id;
        });
    }
}