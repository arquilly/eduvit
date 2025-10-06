function manyChecks(a) {  
  return (
    a > 10 ? 'a is bigger than 10' : 'a is less than or equal to 10 ' + (a === 5 ? 'an example of a special case' : '')) + (a === 15 ? 'but a is not 15' : '')+ (a > 5 ? 'and a is greater than 5' : 'and a is less than or equal to 5 ') + (a % 2 ? ' and a is odd' : ' and a is even ');
}

// if/else
function manyChecks_ifElse(a) {
  let msg = '';

  if (a > 10) {
    msg += 'a is bigger than 10';
  } else {
    msg += 'a is less than or equal to 10 ';
    if (a === 5) msg += 'an example of a special case';
  }

  if (a === 15) msg += 'but a is not 15';

  if (a > 5) {
    msg += 'and a is greater than 5';
  } else {
    msg += 'and a is less than or equal to 5 ';
  }

  if (a % 2) msg += ' and a is odd';
  else msg += ' and a is even ';

  return msg;
}

// switch
function manyChecks_switch(a) {
  let msg = '';

  switch (true) {
    case a > 10:
      msg += 'a is bigger than 10';
      break;
    default:
      msg += 'a is less than or equal to 10 ';
      if (a === 5) msg += 'an example of a special case';
  }

  switch (true) {
    case a === 15:
      msg += 'but a is not 15';
      break;
  }

  switch (true) {
    case a > 5:
      msg += 'and a is greater than 5';
      break;
    default:
      msg += 'and a is less than or equal to 5 ';
  }

  switch (a % 2) {
    case 0:
      msg += ' and a is even ';
      break;
    default:
      msg += ' and a is odd';
  }

  return msg;
}

let a = Math.floor(Math.random() * 20) + 1;
console.log(`a = ${a}`);

const r1 = manyChecks_ifElse(a);
console.log("if/else:", r1);

const r2 = manyChecks_switch(a);
console.log("switch:", r2);

const r3 = manyChecks(a);
console.log("tern:", r3);
