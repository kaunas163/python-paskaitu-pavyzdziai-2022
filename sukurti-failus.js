const fs = require('fs');

// let directory = './09-demo';
let examples_count = 30;

if (!fs.existsSync(directory)){
    fs.mkdirSync(directory);
}

for (let i = 1; i <= examples_count; i++) {
    let filename = `${directory}/${i}pvz.py`;
    fs.writeFile(filename, '', function (err) {
        if (err) throw err;
        console.log(filename, 'saved!');
    }); 
}
