var Q1 = document.documentElement.clientHeight;
function f(){
    if(document.documentElement.clientHeight != Q1){
        if(document.documentElement.clientHeight > 700){
            Q1 = document.documentElement.clientHeight;
            location.reload();
        }
    }
}  
window.setInterval("f()",500);