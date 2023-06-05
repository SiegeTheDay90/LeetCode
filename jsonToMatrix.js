var jsonToMatrix = function(arr) {
    let headers = new Set();

    function headerize(obj, dir=""){

        if(!obj){
            return [dir]
        }

        let headers = new Set();

        for(const [key, val] of Object.entries(obj)){
            const pwd = dir.length>0 ? dir+"."+key : key;
            if(typeof(val) !== 'object'){
                headers.add(pwd)
            } else {
                headers = new Set([
                    ...headers,
                    ...headerize(val, pwd)
                ])
            }
        }
        return headers
    }

    for(const obj of arr){
        headers = new Set([
            ...headers,
            ...headerize(obj)
        ])
    }

    headers = Array.from(headers).sort((a, b) => a === b ? 0 : a < b ? -1 : 1)
    const matrix = [headers]
    
    for(const obj of arr){
        const row = []
        for(const header of headers){
            let pwd = obj
            const dir = header.split(".")
            let i = 0

            while(pwd !== null && pwd[dir[i]] !== undefined && typeof(pwd) !== 'string'){
                pwd = pwd[dir[i++]]
            }

            if(i<dir.length){
                row.push("")
            } else if(pwd === null){
                row.push(null)
            } else {
                row.push(typeof(pwd) === 'object' ? "" : pwd)
            }            
        }
        matrix.push(row)
    }

    return matrix
};

console.table(
    jsonToMatrix([{"tags":["et",true,"velit","velit","ullamco","qui","nostrud"]},{"tags":["et",true,"velit","velit",[1],{"x":true},{"x":true}]}])
)