function setup() {
    createCanvas(499,499);
}
function draw(){
    background(200,160,230);
    point(249,249);
    point(0,0);
    point(499,499);
    point(0,499);
    point(499,0);
    triangle(0,0,499,0,249,499);
    triangle(0,499, 0, 19, 230, 499);
    
}