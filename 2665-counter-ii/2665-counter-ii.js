/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let copy_of_init = init;
    return {
        increment: ()=> ++copy_of_init,
        decrement: ()=> --copy_of_init,
        reset: ()=> copy_of_init = init
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */