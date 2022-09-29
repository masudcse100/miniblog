
function myFunction() {
  let txt;
  let r = confirm("Press a button!");
  if (r == true) {
    txt = "You pressed OK!";
  } else {
    txt = "You pressed Cancel!";
  }
  document.getElementById("demo").innerHTML = txt;
}
// var message_ele = document.getElementById("#msg");

// setTimeout(function(){ 
//    message_ele.style.display = "none"; 
// }, 3000);
// This file not working ....... so try later ....... 
// But use other delete confirmation >>> <input onclick="return confirm('Are you sure you want to delete this post?');" type="submit" class='btn btn-danger btn-sm my-3 font-weight-normal' value="Delete">

  var info_messages = document.getElementsByClassName('alert-dismissible');

    setTimeout(function(){
        for (var i = 0; i < info_messages.length; i ++) {
            // Set display attribute as !important, neccessary when using bootstrap
            info_messages[i].setAttribute('style', 'display:none !important');
        }
    }, 3000);