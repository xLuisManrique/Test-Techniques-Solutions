function FirstFactorial(num){

    // code goes here
    let resultado = 1;

    for (let i = 1; i<=num; i++){
        resultado *= i;
    }
    
    return resultado;
}

// keep this function call here
console.log(FirstFactorial(4));
console.log(FirstFactorial(8));

