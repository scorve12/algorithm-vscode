const HashTable = require('hash-table');

let table = new HashTable();

table.set('name', 'Alice');
table.set('age', 25);

console.log(table.get('name'));
console.log(table.get('age'));