/* Assignment for "Webfundamental-JavaScript-Foundation Concepts-For a Few Billion"*/
/*10-13-2017*/
var money=0.01;
var num=1;
while (true) {
    money=2*money;
    num+=1;
    if (num ==30 && money > 10000) {
        console.log("Money after "+num+" days is "+money+" , he can get more than 10,000 after 30 days, so how about 100000000?");

    }
    else if (num ==30 && money < 10000){
        console.log("Money after "+num+" days is "+money+" , he can NOT get more than 10,000 after 30 days. So how many days can he get more than 10,000?");
    }
    else if (money > 100000000){
        console.log("after "+num+" days, he gets 1 Billion");
        break;
    }

}
