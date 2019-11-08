var img = new Image();
img.src = 'perso.png';

var canvas = document.createElement('canvas');
canvas.width = document.body.clientWidth  //a changer
canvas.height = document.body.clientHeight//a changer

document.body.appendChild(canvas);
var ctx = canvas.getContext("2d");
var persoX = (canvas.width-img.width)/2;

var rightPressed = false;
var leftPressed = false;
var upPressed = false;


document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
    else if(e.keyCode == 38) {

        upPressed = true
    }
}
function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
    else if(e.keyCode == 38) {
        upPressed = false
  }
}



function draw_image(){
  ctx.clearRect(persoX,canvas.height-img.height,img.width,img.height)
  ctx.drawImage(img,persoX,canvas.height-img.height)
}

function jump(){

}

function draw() {
  draw_image()
  if(rightPressed && persoX < canvas.width-img.width) {
      persoX += 7;
  }
  else if(leftPressed && persoX > 0) {
      persoX -= 7;
  }
  else if(upPressed){
    jump() //a faire
  }
  console.log(persoX)
}

setInterval(draw, 10);
