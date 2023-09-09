/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let res_arr = [];
    for(let i = 0; i < arr.length; i++) {
        res_arr[i] = fn(arr[i], i);
    }
    return res_arr;
};