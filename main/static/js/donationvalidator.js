var namevalid = false;
var emailvalid = false;
var phonevalid = false;
var cityvalid = false;
var amountvalid = false;
var dobvalid = false;
var addressvalid = false;
var pinvalid = false;
var panvalid = false;
var acceptvalid = false;


// Amount validator
$('[name = "amount"]').on('input', function () {
  if ("-".indexOf($('[name = "amount"]').val()) >=0 ) {
    amountvalid=false;
    $("#amounterror").removeAttr('hidden');
  }else{
    amountvalid=true;
    $("#amounterror").attr('hidden', 'hidden');
  }
});

//Name
$('[name = "name"]').on('input', function () {
  if (($('[name = "name"]').val().length) == 0 ) {
    namevalid=false;
    $("#namerror").removeAttr('hidden');
  }else{
    namevalid=true;
    $("#namerror").attr('hidden', 'hidden');
  }
});


//Address
$('[name = "address"]').on('input', function () {
  if (($('[name = "address"]').val().length) == 0 ) {
    addressvalid=false;
    $("#addresserror").removeAttr('hidden');
  }else{
    addressvalid=true;
    $("#addresserror").attr('hidden', 'hidden');
  }
});

//City
$('[name = "city"]').on('input', function () {
  if (($('[name = "city"]').val().length) == 0 ) {
    cityvalid=false;
    $("#cityerror").removeAttr('hidden');
  }else{
    cityvalid=true;
    $("#cityerror").attr('hidden', 'hidden');
  }
});

//pincode
$('[name = "pincode"]').on('input', function () {
  if (($('[name = "pincode"]').val().length) == 0 ) {
    pinvalid=false;
    $("#pincodeerror").removeAttr('hidden');
  }else{
    pinvalid=true;
    $("#pincodeerror").attr('hidden', 'hidden');
  }
});

//DOB
$('[name = "dob"]').on('input', function () {
  if (($('[name = "dob"]').val().length) == 0 ) {
    dobvalid=false;
    $("#doberror").removeAttr('hidden');
  }else{
    dobvalid=true;
    $("#doberror").attr('hidden', 'hidden');
  }
});

//PAN
$('[name = "pan"]').on('input', function () {
  if (($('[name = "pan"]').val().length) == 0 ) {
    panvalid=false;
    $("#panerror").removeAttr('hidden');
  }else{
    panvalid=true;
    $("#panerror").attr('hidden', 'hidden');
  }
});

//Phone
$('[name = "phone"]').on('input', function () {
  if (($('[name = "phone"]').val().length) == 0 ) {
    phonevalid=false;
    $("#phoneerror").removeAttr('hidden');
  }else{
    phonevalid=true;
    $("#phoneerror").attr('hidden', 'hidden');
  }
});

//Email
$('[name = "email"]').on('input', function () {
  if (($('[name = "email"]').val().length) == 0 ) {
    emailvalid=false;
    $("#emailerror").removeAttr('hidden');
  }else{
    emailvalid=true;
    $("#emailerror").attr('hidden', 'hidden');
  }
});


//Accept
$('[name = "accept"]').on('input', function () {
  if (($('[name = "accept"]').is(":checked")) == false ) {
    acceptvalid=false;
    $("#accepterror").removeAttr('hidden');
  }else{
    $("#accepterror").attr('hidden', 'hidden');
    acceptvalid=true;
  }
  
});


function submitform(){
  if(namevalid && panvalid && pinvalid && addressvalid && emailvalid && phonevalid && dobvalid && cityvalid && amountvalid){
    if(acceptvalid){
      $("#donateform").submit();
    }else{
      //$("#accepterror").removeAttr('hidden');
    }
  }else{
    alert("Please check the form values");
  }
}
