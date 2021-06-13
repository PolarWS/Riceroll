var gaodu = document.documentElement.clientHeight;
var kuandu = gaodu/3*4;
var kuandu1 = kuandu*0.2
var kuandu2 = kuandu - kuandu1;
var kuandu3 = gaodu*0.119;
var yuanjiao1 = gaodu*0.01;
var gaodu1 = gaodu*0.079;
var gaodu2 = gaodu*0.049;
var gaodu3 = gaodu*0.005;
var gaodu4 = gaodu3*2;
document.getElementById("N1").style.height = gaodu + "px";
document.getElementById("N2").style.width = kuandu + "px";
document.getElementById("N1").style.width = kuandu1 + "px";
document.getElementById("N4").style.width = kuandu2 + "px";
document.getElementById("P1").style.width = kuandu3 + "px";
document.getElementById("P1").style.height = kuandu3 + "px";
document.getElementById("N5").style.height = gaodu1 + "px";
document.getElementById("N6").style.height = gaodu1 + "px";
// document.getElementById("T3").style.marginBottom = gaodu4 + "px";
var x1 = document.getElementsByClassName("Q1");
for(let i1 = 0; i1 < x1.length; i1++){
    x1[i1].style.height = gaodu2 + "px";
    x1[i1].style.marginTop = gaodu3 + "px";

}
document.getElementById("N3").style.borderRadius = yuanjiao1 + "px";

