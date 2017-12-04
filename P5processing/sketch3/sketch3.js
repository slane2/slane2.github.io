function setup() {
    createCanvas(499,499);
}
function draw(){
    background(200,160,230);
    triangle(0, 0, 499, 0, 249, 499); //largest center
    fill(160, 200, 230);
    triangle(30, 30, 469, 30, 249, 469);
    fill(100, 15, 75);
    triangle(70, 60, 429, 60, 249, 429);
    fill(250, 180, 180);
    triangle(110, 90, 389, 90, 249, 389);
    fill(100, 250, 175);
    triangle(150, 120, 349, 120, 249, 349);
    fill(160, 20, 20);
    triangle(190, 150, 309, 150, 249, 309);
    fill(70, 100, 256);
    triangle(230, 180, 269, 180, 249, 269);//smallest center
    triangle(0, 499, 0, 19, 235, 499);//closest left
    fill(250,250,0);
    triangle(0, 499, 0, 59, 205, 499);
    fill(10,120,70);
    triangle(0, 499, 0, 89, 175, 499);
    fill(70,0,70);
    triangle(0, 499, 0, 119, 148, 499);
    fill(250,0,0);
    triangle(0, 499, 0, 153, 118, 499);
    fill(20,20,135);
    triangle(0, 499, 0, 190, 88, 499);
    fill(256,170,50);
    triangle(0, 499, 0, 232, 55, 499);
    fill(90,275,200);
    triangle(0, 499, 0, 265, 23, 499);
    triangle(0, 499, 0, 295, 10, 499);//furthest left
    fill(250, 100, 150);
    triangle(499, 499, 499, 24, 265, 499);//closest right
    fill(250,250,0);
    triangle(499, 499, 499, 60, 295, 499);
    fill(10,120,70);
    triangle(499, 499, 499, 95, 320, 499);
    fill(250,0,0)
    triangle(499, 499, 499, 125, 350, 499);
    fill(70,0,70);
    triangle(499, 499, 499, 157, 380, 499);
    fill(0, 230,230);
    triangle(0, 499, 0, 190, 88, 499);
    fill(50,250,95);
    triangle(499, 499, 499, 190, 413, 499);
    fill(256,170,50);
    triangle(499, 499, 499, 250, 450, 499);//furthest right
    
    
}