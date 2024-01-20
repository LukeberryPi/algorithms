// https://leetcode.com/problems/remove-linked-list-elements/description/

let head = [1, 2, 6, 3, 4, 5, 6];
let val = 6;

function removeElements(head, val) {
  for (let i = head.length; i >= 0; i--) {
    if (head[i] === val) {
      head.splice(i, 1);
    }
  }

  return head;
}

console.log(removeElements(head, val));

