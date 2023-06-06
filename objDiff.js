function deepEquals(obj1, obj2){
    if(obj1.__proto__.constructor !== obj2.__proto__.constructor){
        return false
    } else if(typeof(obj1) !== 'object' && typeof(obj2) !== 'object'){
        return obj1 === obj2
    } else if (Object.keys(obj1).length !== Object.keys(obj2).length){
        return false
    }

    for(const key of Object.keys(obj1)){
        if(obj2[key] === undefined){
            return false
        }
        if(!deepEquals(obj1[key], obj2[key])){
            return false
        }
    }
    return true
}

let a = {b: 2, a: 1, c: {d: [1,2,3]}}

let b = {a: 1, b: 2, c: {d: [1,2,3]}}

console.log(deepEquals({}, {}))
// console.log(deepEquals([1,2,3], {0: 1, 1: 2, 2: 3}))