let a = Math.floor(Math.random() * 100);
console.log("a =", a);

// if else
let r1;
if ((a > 10 ? a : a * 2) > 5) {
  r1 = 2 * a + 1;
} else if ((a < 3 ? 1 : 2 * (a - 2)) > 4) {
  r1 = 5;
} else if (a % 2 === 0) {
  r1 = 6;
} else {
  r1 = 7;
}
console.log(r1);

// switch
let r2;
switch (true) {
  case ((a > 10 ? a : a * 2) > 5):
    r2 = 2 * a + 1;
    break;
  case ((a < 3 ? 1 : 2 * (a - 2)) > 4):
    r2 = 5;
    break;
  case (a % 2 === 0):
    r2 = 6;
    break;
  default:
    r2 = 7;
}
console.log(r2);

let r3 = (a > 10 ? a : a * 2) > 5 ? (2 * a) + 1 : (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7);
console.log(r3);
