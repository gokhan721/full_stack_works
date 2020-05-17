var roster = []

function callback(a, b){
  alert(a * b)
}

function main_call(callback) {
  callback(arguments[1], arguments[2])
}

function add() {
  let name = prompt("Enter added name:").trim()
  roster.push(name)
}

function display() {
  console.log(roster)
}

function remove() {
  let name = prompt("Enter removed name:").trim()
  let index_name = roster.indexOf(name)
  if (index_name > -1)
    roster.splice(index_name, 1)
}



while (1) {
  let action = prompt("Select perform: add,remove,display,quit").trim().toLowerCase()
  if (action === "add") {
    add()
  } else if (action === "display") {
    display()
  } else if (action === "remove") {
    remove()
  } else if (action === "quit") {
    alert("Thanks for all")
    break
  } else {
    continue
  }
}
