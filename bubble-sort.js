const bubbleSort = (arr) => {
    let sortUntil = arr.length - 1; 
    let sorted = false; 
    while(!sorted){
        sorted = true;
        for(let i=0; i < sortUntil; i++){
            if(arr[i] > arr[i + 1]){
                sorted = false;
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            }
        }
        sortUntil--; 
    }
    return arr;
};


const arr = [5, 4, 3, 2, 1]; 
console.log(bubbleSort(arr));