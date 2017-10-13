var daysUntilMyBirthday = 60;
for (i= daysUntilMyBirthday; i>=0; i--){
    if (i >= 30){
        console.log(i+" days left, can't wait!");
    }
    else if(i >=5){
        console.log(i+" days left, it's coming!");
    }
    else if (i !=0){
        console.log(i+" days left, SCREAM!");
    }
    else{
        console.log(" Happy birthday!");
    }
}
