
// https://www.w3schools.com/jsref/prop_nav_geolocation.asp
// var latID = document.getElementById("lat");
// var lngID = document.getElementById("lng");

function initializeGeoLocation() {
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            $('#lat').val(pos['lat']);
            $('#lng').val(pos['lng']);
            $('#msg').html("Ready, detected location " + "lat: "+ pos['lat'] + " lng: " + pos['lng'] );

          }, function() {
            $('#msg').html("looks like your browser does not support location ")
          });
        }
}


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
         $('#msg').html("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    $('#latFM').val(position.coords.latitude);
    $('#lngFM').val(position.coords.longitude);
    $('#latID').html(position.coords.latitude);
    $('#lngID').html(position.coords.longitude);
}
 

function submitForm() {
      // alert('hi')
      $("#formId").submit();
}

function setup() {
    // initializeGeoLocation()
    console.log( "ready!" );
    $("#submit").click(submitForm);
}

$(document).ready(setup);


/*
$( document ).ready(function() {
    console.log( "ready!" );
    getLocation();
});
*/

