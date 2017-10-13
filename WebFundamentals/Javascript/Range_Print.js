function range_Print(point1,point2,skip){
    var num = [];
    if (skip === undefined) {
        skip = 1;
    }
    if (point2 ===undefined) {
        point2 = point1;
        point1 = 0;
    }
    for (var i = point1; i < point2; i+=skip) {
        num.push(i)
    }

    console.log(num);
}

range_Print(4,10,4);
