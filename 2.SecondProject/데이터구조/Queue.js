const Queue = require('queue');

let queue = new Queue();

queue.push(1);
queue.push(2);
queue.push(3);

console.log(queue.shift());
console.log(queue.peek());