const LinkedList = require('linked-list');

let list = new LinkedList();

list.insertFirst(10);
list.insertLast(20);

console.log(list.getFirst());  // 10
console.log(list.getLast());   // 20