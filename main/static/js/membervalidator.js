var namevalid = false;
var emailvalid = false;
var phonevalid = false;
var cityvalid = false;
var votervalid = false;
var dobvalid = false;
var addressvalid = false;
var pinvalid = false;
var contribvalid = false;
var acceptvalid = false;
var passvalid = false;

//Name
$('[name = "vname"]').on('input', function () {
    if (($('[name = "vname"]').val().length) == 0) {
        namevalid = false;
        $("#nameerror").removeAttr('hidden');
    } else {
        namevalid = true;
        $("#nameerror").attr('hidden', 'hidden');
    }
});

//email
$('[name = "vemail"]').on('input', function () {
    if (($('[name = "vemail"]').val().length) == 0) {
        emailvalid = false;
        $("#emailerror").removeAttr('hidden');
    } else {
        emailvalid = true;
        $("#emailerror").attr('hidden', 'hidden');
    }
});

$(document).ready(function () {
    $("[name = 'vemail']").change(function () {
        if ($('[name = "vemail"]').val().indexOf("@") < 0) {
            emailvalid = false;
            $("#emailerror").removeAttr('hidden');
        } else {
            emailvalid = true;
            $("#emailerror").attr('hidden', 'hidden');
        }
    });
});

//Phone
$(document).ready(function () {
    $("[name = 'vphone']").change(function () {
        if (($('[name = "vphone"]').val().length) < 10 || ($('[name = "vphone"]').val().length) > 10) {
            phonevalid = false;
            $("#phoneerror").removeAttr('hidden');
        } else {
            phonevalid = true;
            $("#phoneerror").attr('hidden', 'hidden');
        }
    });
});


//DOB
$('[name = "vdob"]').on('input', function () {
    if (($('[name = "vdob"]').val().length) == 0) {
        dobvalid = false;
        $("#doberror").removeAttr('hidden');
    } else {
        dobvalid = true;
        $("#doberror").attr('hidden', 'hidden');
    }
});

//Address
$('[name = "vaddress"]').on('input', function () {
    if (($('[name = "vaddress"]').val().length) == 0) {
        addressvalid = false;
        $("#addresserror").removeAttr('hidden');
    } else {
        addressvalid = true;
        $("#addresserror").attr('hidden', 'hidden');
    }
});

//pincode
$('[name = "vpin"]').on('input', function () {
    if (($('[name = "vpin"]').val().length) == 0) {
        pinvalid = false;
        $("#pinerror").removeAttr('hidden');
    } else {
        pinvalid = true;
        $("#pinerror").attr('hidden', 'hidden');
    }
});

//Voter ID
$('[name = "vvoter"]').on('input', function () {
    if (($('[name = "vvoter"]').val().length) == 0) {
        votervalid = false;
        $("#votererror").removeAttr('hidden');
    } else {
        votervalid = true;
        $("#votererror").attr('hidden', 'hidden');
    }
});

//City
$('[name = "vcity"]').on('input', function () {
    if (($('[name = "vcity"]').val().length) == 0) {
        cityvalid = false;
        $("#cityerror").removeAttr('hidden');
    } else {
        cityvalid = true;
        $("#cityerror").attr('hidden', 'hidden');
    }
});

//Password
$('[name = "vpassword"]').on('input', function () {
    if (($('[name = "vpassword"]').val().length) <= 6) {
        passvalid = false;
        $("#passerror").removeAttr('hidden');
    } else {
        passvalid = true;
        $("#passerror").attr('hidden', 'hidden');
    }
});

//Accept
$('[name = "vaccept"]').on('input', function () {
    if (($('[name = "vaccept"]').is(":checked")) == false) {
        acceptvalid = false;
        $("#accepterror").removeAttr('hidden');
    } else {
        $("#accepterror").attr('hidden', 'hidden');
        acceptvalid = true;
    }
});

var itcheck = 0;
var contentcheck = 0;
var partycheck = 0;
var digitalcheck = 0;
var othercheck = 0;

function itsp(e) {
    if (itcheck == 0) {
        itcheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        itcheck = 0;
    }
}

function party() {
    if (partycheck == 0) {
        partycheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        partycheck = 0;
    }
}

function content() {
    if (contentcheck == 0) {
        contentcheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        contentcheck = 0;
    }
}

function digital() {
    if (digitalcheck == 0) {
        digitalcheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        digitalcheck = 0;
    }
}

function other() {
    if (othercheck == 0) {
        othercheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        othercheck = 0;
    }
}

var acceptcheck = 0;

function acceptterms() {
    if (acceptcheck == 0) {
        acceptcheck = 1;
        $("#contriberror").attr('hidden', 'hidden');
    } else {
        acceptcheck = 0;
    }
}


function submitmemberform() {
    var summation = itcheck + othercheck + contentcheck + digitalcheck + partycheck;
    var formtype = $('#vtype').val();
    if (acceptcheck == 1) {
        if (formtype == 1) {
            if (summation == 0) {
                contribvalid = false;
                $("#contriberror").removeAttr('hidden');
            } else {
                if (phonevalid && emailvalid && namevalid && addressvalid && pinvalid 
                    && dobvalid && cityvalid && votervalid) {
                    $("#volunteerform").submit();
                } else {
                    alert("Please fill all fields");
                }
            }
        } if (formtype == 2) {
            if (phonevalid && emailvalid && namevalid && addressvalid && pinvalid && dobvalid && cityvalid && votervalid) {
                $("#volunteerform").submit();
            } else {
                alert("Please fill all fields");
            }
        }
    } else {
        $("#accepterror").removeAttr('hidden');
    }
}