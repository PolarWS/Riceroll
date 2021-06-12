var gaodu = document.documentElement.clientHeight;
var kuandu = gaodu/3*4;
var kuandu1 = kuandu*0.2
var kuandu2 = kuandu - kuandu1;
document.getElementById("N1").style.height = gaodu + "px";
document.getElementById("N2").style.width = kuandu + "px";
document.getElementById("N1").style.width = kuandu1 + "px";
document.getElementById("N4").style.width = kuandu2 + "px";
