// 10-13-2017 Assignment: Webfundamental-JavaScript-Fundamentals1-Fancy_array
function print(symbol,arr,sort){
    if (sort == "reverse") {
        for (var i = arr.length-1 ; i >= 0; i--) {
            console.log(i+ symbol + ""+arr[i]);
        }
    }
    else { for (var i = 0;i <  arr.length; i++){
        console.log(i+ symbol + ""+arr[i]);
        }
    }
}
var symbol="-->";
var arr=[1,2,3,5];
var sort= "reverse";
console.log(arr.length);
print("-->", [1,2,3],"reverse");
