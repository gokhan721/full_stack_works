var name = prompt("Enter First and Last Name")
var age = parseInt(prompt("Enter age"))
var height = parseInt(prompt("Enter height in cm"))
var pet_name = prompt("Enter pet name")

var name_array = name.split(' ')
var first_name = name_array[0]
var last_name = name_array[1]

if (
  first_name[0] === last_name[0] &&
  20 <= age <= 30 &&
  170 <= height &&
  pet_name[pet_name.length - 1] === "y"
){
  console.log("Spyyyyy!!!\n name:" + name + "\tage: " + age +
  "\theight: " + height + "\tpet_name" + pet_name)
  console.log("Welcome Comrade! You've passed the spy test!!!")
}else {
  console.log("Sorryy, nothing to see here!!!");
}
