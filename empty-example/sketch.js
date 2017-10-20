function setup() {
createCanvas(925,333);
background(230,22,77)
}

function draw() {
if (mouseIsPressed) {
    fill(60,30,150);
} else{
    fill(150,50,99);
}
    ellipse(mouseX,mouseY,80,80);
}