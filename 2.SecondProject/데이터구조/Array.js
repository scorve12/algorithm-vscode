const { List } = require('immutable');

let list = List([1, 2, 3]);

list = list.push(4);

console.log(list);
