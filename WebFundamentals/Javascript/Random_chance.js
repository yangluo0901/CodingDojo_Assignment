function lottery(quarter,round_1){
    if (quarter > 0) {
        var rewards = [];
        var round_2 = 1;
        var round;
        var string;
        var sum = 0;
        if (quarter >= round_1) {
            round = round_1;
            string = " After "+round + " rounds your rewards :"+sum;
        } else {
            round =  quarter;
            string = " Insufficient Gold, you can only play "+ round +" rounds and your rewards :"+sum;
        }
        while (round_2 <= round) {
            var nums = Math.random()*100;
            if (nums == 1) {
                rewards[round_2-1] = Math.random()*51+50;
                console.log("Win! You get "+rewards[round_2-1]);
            }
            else{
                rewards[round_2-1] = 0;
                console.log("Sorry, you are not lucky this time!");
            }
            sum+=rewards[round_2-1];
            round_2+=1;
        }
        sum = sum + quarter - round;

        console.log(string);
    }
}

quarter = 4;
round_1 = 5;
lottery(quarter,round_1);
