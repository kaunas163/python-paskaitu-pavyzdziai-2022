const fs = require('fs');

let directory = './15-demo';
let examples_start = 1;
let examples_count = 30;

if (!fs.existsSync(directory)){
    fs.mkdirSync(directory);
}

for (let i = examples_start; i < examples_start + examples_count; i++) {
    let filename = `${directory}/${i}pvz.py`;
    fs.writeFile(filename, '', function (err) {
        if (err) throw err;
        console.log(filename, 'saved!');
    }); 
}
