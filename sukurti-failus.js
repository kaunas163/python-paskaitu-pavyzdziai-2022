const fs = require('fs');

let directory = './13-darbas-su-failais';
let examples_start = 1;
let examples_count = 50;

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
