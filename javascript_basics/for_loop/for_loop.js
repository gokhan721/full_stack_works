/*

For- loops through a number of items
For/In - loops through a JS object
For/of - used with arrays

*/
var word = "ASDAASFFSAFSA"
var i = 0

for (let i = 0; i < word.length; ++i) {
  console.log(word[i])
}

while (i < 5) {
  console.log("hello\n");
  ++i
}

for (let i = 0; i < 5; ++i) {
  console.log("hello");
}

var j = 1

while(j < 25){
  if (j % 2 === 1){
    console.log("Odd: "+j);
  }
  j++
}

for(let j = 1; j <25; ++j){
  if (j % 2 === 1){
    console.log("Odd for: " + j);
  }
}

/*

// calling x after definition
var x = 5;
document.write(x, "\n");

// calling y after definition
let y = 10;
document.write(y, "\n");

// calling var z before definition will return undefined
document.write(z, "\n");
var z = 2;

// calling let a before definition will give error
document.write(a);
let a = 3;

// not logged due to above error
console.log("blablabla");

 */
