var namevalid = false;
var emailvalid = false;
var phonevalid = false;
var cityvalid = false;
var resumevalid = false;
var tentvalid = false;
var collegevalid = false;
var programvalid = false;
var interestvalid = false;
var acceptvalid = false;
var passvalid = false;
var agevalid = false;


//Name
$('[name = "iname"]').on('input', function () {
    if (($('[name = "iname"]').val().length) == 0) {
        namevalid = false;
        $("#inameerror").removeAttr('hidden');
    } else {
        namevalid = true;
        $("#inameerror").attr('hidden', 'hidden');
    }
});

//email
$('[name = "iemail"]').on('input', function () {
    if (($('[name = "iemail"]').val().length) == 0) {
        emailvalid = false;
        $("#iemailerror").removeAttr('hidden');
    } else {
        emailvalid = true;
        $("#iemailerror").attr('hidden', 'hidden');
    }
});

$(document).ready(function () {
    $("[name = 'iemail']").change(function () {
        if ($('[name = "iemail"]').val().indexOf("@") < 0) {
            emailvalid = false;
            $("#iemailerror").removeAttr('hidden');
        } else {
            emailvalid = true;
            $("#iemailerror").attr('hidden', 'hidden');
        }
    });
});

//Phone
$(document).ready(function () {
    $("[name = 'iphone']").change(function () {
        if (($('[name = "iphone"]').val().length) < 10 || ($('[name = "iphone"]').val().length) > 10) {
            phonevalid = false;
            $("#iphoneerror").removeAttr('hidden');
        } else {
            phonevalid = true;
            $("#iphoneerror").attr('hidden', 'hidden');
        }
    });
});


//Tentative
$('[name = "itsd"]').on('input', function () {
    if (($('[name = "itsd"]').val().length) == 0) {
        tentvalid = false;
        $("#itenterror").removeAttr('hidden');
    } else {
        tentvalid = true;
        $("#itenterror").attr('hidden', 'hidden');
    }
});


//City
$('[name = "icity"]').on('input', function () {
    if (($('[name = "icity"]').val().length) == 0) {
        cityvalid = false;
        $("#icityerror").removeAttr('hidden');
    } else {
        cityvalid = true;
        $("#icityerror").attr('hidden', 'hidden');
    }
});

//Password
$('[name = "ipassword"]').on('input', function () {
    if (($('[name = "ipassword"]').val().length) <= 6) {
        passvalid = false;
        $("#ipasserror").removeAttr('hidden');
    } else {
        passvalid = true;
        $("#ipasserror").attr('hidden', 'hidden');
    }
});

//Accept
$('[name = "iaccept"]').on('input', function () {
    if (($('[name = "iaccept"]').is(":checked")) == false) {
        acceptvalid = false;
        $("#iaccepterror").removeAttr('hidden');
    } else {
        $("#iaccepterror").attr('hidden', 'hidden');
        acceptvalid = true;
    }
});

//Program
$('[name = "icourse"]').on('input', function () {
    if (($('[name = "icourse"]').val().length) == 0) {
        programvalid = false;
        $("#icourseerror").removeAttr('hidden');
    } else {
        $("#icourseerror").attr('hidden', 'hidden');
        programvalid = true;
    }
});

//College
$('[name = "icollege"]').on('input', function () {
    if (($('[name = "icollege"]').val().length) == 0) {
        collegevalid = false;
        $("#icollegeerror").removeAttr('hidden');
    } else {
        $("#icollegeerror").attr('hidden', 'hidden');
        collegevalid = true;
    }
});

//Age
$('[name = "iage"]').on('input', function () {
    if (($('[name = "iage"]').val()) == 0) {
        agevalid = false;
        $("#iageerror").removeAttr('hidden');
    } else {
        $("#iageerror").attr('hidden', 'hidden');
        agevalid = true;
    }
});

//Interest
function checkinterest(){
    interestvalid=true;
    $("#iinteresterror").attr('hidden', 'hidden');
}

function selectingfile(){
    $("#iresumeerror").attr('hidden', 'hidden');
}


function submitintern() {
    var filename = $("#idoc").val();
    if(filename.length > 0){
        if(acceptvalid){
            if(interestvalid){
                if(phonevalid && emailvalid && cityvalid && collegevalid && programvalid
                && agevalid && tentvalid){
                    $('#internform').submit();
                }else{
                    alert("Please fill all the fields")
                }
            }else{
                $("#iinteresterror").removeAttr('hidden');  
            }
        }else{
            $("#iaccepterror").removeAttr('hidden');    
        }
    }else{
        $("#iresumeerror").removeAttr('hidden');
    }
}