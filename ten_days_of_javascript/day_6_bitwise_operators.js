//link to challenge: https://www.hackerrank.com/challenges/js10-bitwise/problem


// this approach only solves 3/6 test cases
function getMaxLessThanK(n,k){
    
    // create array with values from 1 to n
    let S = Array.from({length: n}, (_, i) => i + 1);
    
    // create all possible combinations of bitwise AND of elements inside S
    var bitwise_and_results = S.flatMap(
    (v, i) => S.slice(i+1).map( w => v & w ));
    
    let max_elem = 0;
    
    // iterate through bitwise_and_results and only append if element higher than current max_elem but smaller than k
    bitwise_and_results.forEach((result) => {
        if ((result > max_elem) && (result < k)){
            max_elem = result;
        }
    }) 
    
    return max_elem;
    
}