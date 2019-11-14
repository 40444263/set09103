var img = new Image();
img.src = 'perso.png';
img.height = 100


var canvas = document.createElement('canvas');
canvas.width = document.body.clientWidth
canvas.height = document.body.clientHeight

document.body.appendChild(canvas);
var ctx = canvas.getContext("2d");
var persoX = (canvas.width-img.width)/2;
var persoY = canvas.height-img.height;

var rightPressed = false;
var leftPressed = false;
var upPressed = false;

var saut = false;
var gravite = 0;



document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
    if(e.keyCode == 38) {
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
    if(e.keyCode == 38) {
        upPressed = false
  }
}



function draw_image(){

  ctx.clearRect(persoX,persoY,img.width,img.height);
  ctx.drawImage(img,persoX,persoY);
}

function jump(){
  if (saut){
    ctx.clearRect(persoX,persoY,img.width,img.height)
    persoY = persoY-(20-gravite)
    ctx.drawImage(img,persoX,persoY)
    gravite+=0.65
    if (persoY > canvas.height-img.height){
        persoY = canvas.height-img.height;
        gravite=0
        saut = false
      }
      setTimeout(jump,5)
    }
}

function draw() {
  draw_image()
  if(rightPressed && persoX < canvas.width-img.width) {
      persoX += 7;
  }
  else if(leftPressed && persoX > 0) {
      persoX -= 7;
  }
  if(upPressed){
    if (saut == false){
      saut = true;
      jump() //a faire
      console.log(" DRAW Y",persoY)
    }
  }
  // console.log(persoX,persoY,img.height)
}

setInterval(draw, 10);
