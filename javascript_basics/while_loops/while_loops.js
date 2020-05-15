var counter = 1
var age = 0

while(1){
  age = parseInt(prompt("Enter age"))
  console.log(age);
  if (Number.isInteger(age) && 0 < age < 130){
    alert("Greate age is integer!!")
    break
  }else{
    if (counter < 3){
      alert("Try again to enter Integer!!!")
    }else{
      alert("Sorry dude!!!")
      break
    }
  }
  ++counter
}
