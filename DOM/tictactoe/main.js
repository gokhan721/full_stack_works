var restart = document.querySelector("#restart")


restart.addEventListener("click", function() {
  td_array.forEach(
    td => td.textContent = ""
  )
})

var td_array = document.querySelectorAll("td")

function css_td(td) {
  td.style.height = "150px";
  td.style.width = "150px";
  td.style.textAlign = "center";
  td.style.border = "5px solid black"
  td.style.fontSize = "100px"
  td.addEventListener("click", function() {
    let textContent = td.textContent;
    if (textContent === "") {
      td.textContent = "X";
    } else if (textContent === "X") {
      td.textContent = "O";
    } else {
      td.textContent = "";
    }
  })
}

td_array.forEach(td => css_td(td))
