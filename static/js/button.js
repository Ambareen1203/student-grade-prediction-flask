var count = 0;
var btn = document.getElementById("btn");
var disp = document.getElementById("display");

btn.onClick = function countClicks() {
    count++;
    console.log(count);
    disp.innerHTML = count;
}




        