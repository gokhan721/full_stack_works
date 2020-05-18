var hover = document.querySelector("#one")
var click = document.querySelector("#two")
var double_click = document.querySelector("#three")


hover.addEventListener("mouseover", function() {
  hover.textContent = "Mouse Currently Ovver";
  hover.style.color = "red";
})


hover.addEventListener("mouseout", function() {
  hover.textContent = "HOVER OVER ME";
  hover.style.color = "black";
})


click.addEventListener("click", function() {
  click.textContent = 'CLICKED ON';
  click.style.color = 'blue';
})


double_click.addEventListener("dblclick", function() {
  double_click.textContent = "DB CLICKED";
  double_click.style.color = "orange"
})
