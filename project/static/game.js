var img = new Image();
img.src = 'perso.png';
img.height = 100


var canvas = document.createElement('canvas');
canvas.width = document.body.clientWidth
canvas.height = document.body.clientHeight

document.body.appendChild(canvas);
var ctx = canvas.getContext("2d");
var persoX = (canvas.width-img.width)/2;
var persoY = canvas.height-(canvas.height*0.3)-img.height;
var x_plat = canvas.width-(canvas.width*0.8)
var y_plat = canvas.height-(canvas.height*0.3)


var rightPressed = false;
var leftPressed = false;
var upPressed = false;

var saut = false;
var is_fall = false;
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

function draw_platform(){

  ctx.beginPath();
  ctx.fillStyle = "#FF0000";
  ctx.fillRect(x_plat, y_plat,canvas.width*0.6, 100);
  ctx.stroke();
}

function jump(){
  if (saut){
    ctx.clearRect(persoX,persoY,img.width,img.height)
    persoY = persoY-(20-gravite)
    ctx.drawImage(img,persoX,persoY)
    gravite+=0.65
    if ((persoY > canvas.height-(canvas.height*0.3)-img.height) && (persoX<canvas.width*0.8) && (persoX>(canvas.width*0.2-(img.width-5)))){
        persoY = canvas.height-(canvas.height*0.3)-img.height;
        gravite=0
        saut = false
      }
    else {
      setTimeout(jump,5);
      }
    }
}

function fall(){
  if (is_fall && !saut){
    ctx.clearRect(persoX,persoY,img.width,img.height)
    persoY = persoY+gravite
    ctx.drawImage(img,persoX,persoY)
    if ((persoX<canvas.width*0.8) && (persoX>(canvas.width*0.2-(img.width-5))) && persoY <canvas.height*0.7) {
     gravite=0
     is_fall = false
     console.log("fdoe")
   }
    else if (persoY > canvas.height){
      gravite=0
      is_fall = false
    }
    else{
      gravite+=0.3
      setTimeout(fall,10);
    }
  }
}

function draw() {
  draw_image()
  draw_platform()
  if(rightPressed && persoX < canvas.width-img.width) {
      persoX += 7;
      if (persoX>canvas.width*0.8 && !is_fall){
        is_fall = true
        fall()
      }
  }
  else if(leftPressed && persoX > 0) {
      persoX -= 7;
      if (persoX<(canvas.width*0.2-(img.width-5))&& !is_fall){
        is_fall = true
        fall()
      }
  }
  if(upPressed){
    if (saut == false){
      saut = true;
      gravite=0;
      is_fall = false;
      jump()
      console.log(" DRAW Y",persoY)
    }
  }
  // console.log(persoX,persoY,img.height)
}

setInterval(draw, 10);
