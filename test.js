function badComplexity(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                for (let k = 0; k < arr.length; k++) {
                    sum += arr[k];
                }
            }
        }
    }
    return sum;
}
