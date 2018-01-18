function setup() {
    createCanvas(499,499);
 
}
function draw(){
    if (mouseIsPressed){
        background(0,175,0);
    } else {
        background(200,160,230)}
    

    triangle(0, 0, 499, 0, 249, 499); //largest center
        if (mouseIsPressed){
            fill(100,200,100);
        } else {
            fill(160, 200, 230,);}
    
    triangle(30, 30, 469, 30, 249, 469);
        if (mouseIsPressed){
            fill(10,250,70);
        } else {
    fill(100, 15, 75);}
    
    triangle(70, 60, 429, 60, 249, 429);
        if (mouseIsPressed){
            fill(20,130,20);
        } else {
    fill(250, 180, 180);}
    
    triangle(110, 90, 389, 90, 249, 389);
        if (mouseIsPressed){
            fill(0,90,0);
        } else {
    fill(100, 250, 175);}
    
    triangle(150, 120, 349, 120, 249, 349);
        if (mouseIsPressed){
            fill(40,150,70);
        }else{
    fill(160, 20, 20);}
    
    triangle(190, 150, 309, 150, 249, 309);
        if (mouseIsPressed){
            fill(10,80,10);
        }else{
    fill(70, 100, 256);}
    
    triangle(230, 180, 269, 180, 249, 269);//smallest center
        if (mouseIsPressed){
            fill (30,100,30);
        }else{
    fill(160, 60,110);}
    
    triangle(0, 499, 0, 19, 235, 499);//closest left
        if (mouseIsPressed){
            fill(80,250,150);
        }else{
    fill(250,250,0);}
    
    triangle(0, 499, 0, 59, 205, 499);
        if (mouseIsPressed){
            fill(0,250,0);
        }else{
    fill(10,120,70);}
    
    triangle(0, 499, 0, 89, 175, 499);
        if (mouseIsPressed){
            fill(180,180,60);
        }else{
    fill(70,0,70);}
    
    triangle(0, 499, 0, 119, 148, 499);
    if (mouseIsPressed){
        fill(100,250,100);
    } else {
    fill(250,0,0);}
    
    triangle(0, 499, 0, 153, 118, 499);
    fill(20,20,135);
    
    triangle(0, 499, 0, 190, 88, 499);
    fill(256,170,50);
    
    triangle(0, 499, 0, 232, 55, 499);
    fill(90,275,200);
    
    triangle(0, 499, 0, 265, 23, 499);
    fill(250,250,0);
    
    triangle(0, 499, 0, 295, 10, 499);
    if(mouseIsPressed){
        fill(60,178,60);
    }else{
    fill(160, 60,110);}
    
    triangle(499, 499, 499, 24, 265, 499);//closest right
    if (mouseIsPressed){
        fill(30,200,30);
    }else{
    fill(250,250,0);}
    
    triangle(499, 499, 499, 60, 295, 499);
    if (mouseIsPressed){
        fill(30,100,50);
    }else{
    fill(10,120,70);}
    
    triangle(499, 499, 499, 95, 320, 499);
    if (mouseIsPressed){
        fill(30,100,50);
    }else{
    fill(250,0,0)}
    
    triangle(499, 499, 499, 125, 350, 499);
    if (mouseIsPressed){
        fill(180,180,60);
    }else{
    fill(70,0,70);}
    
    triangle(499, 499, 499, 157, 380, 499);
    if (mouseIsPressed){
        fill(60,180,90);
    }else{
    fill(0, 230,230);}
    
    triangle(0, 499, 0, 190, 88, 499);
    if (mouseIsPressed){
        fill(30,200,50);
    }else{
    fill(50,250,95);}
    
    triangle(499, 499, 499, 190, 413, 499);
    if (mouseIsPressed){
        fill(60,250,115);
    }else{
    fill(256,170,50);}
    
    triangle(499, 499, 499, 250, 450, 499);//furthest right
    fill(250,250,0);
}