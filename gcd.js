function greatestCommonDivisor(num1,num2) {
    if (num1%num2 == 0){
        console.log(num2);
    }
    else {
        return greatestCommonDivisor(num2,num1%num2)
    }
    }
greatestCommonDivisor(4,16);
