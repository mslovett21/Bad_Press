
//name is id of bar, fin is when done loading
function move(name, fin) {
  var elem = document.getElementById(name);   
  var width = 0;
  var id = setInterval(frame, 2); //lower is faster
  function frame() {
    if (width >= fin) {
      clearInterval(id);
    } else {
      width++; 
      elem.style.width = width + '%'; 
      elem.innerHTML = width * 1  + '%';
    }
  }
}
