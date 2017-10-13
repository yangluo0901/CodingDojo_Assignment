var hour = 7;
var minute = 31;
var period = "PM"

if(minute <30){
    if(period == "AM"){
    console.log("It's just after "+hour+"i n the morning")
    }
    else{
        console.log("It's just after "+hour+" in the evening")
    }
}
else{
    if(period == "AM"){
    console.log("It's almost "+hour+" in the morning")
    }
    else{
        console.log("It's almost "+hour+" in the evening")
    }
}
