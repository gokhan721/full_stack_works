var player_one_name = prompt("Player one enter name, you'll be blue")
var player_two_name = prompt("Player two enter name, you'll be red")
var player_play = player_one_name
var game_over = false
change_info_bar()


function change_info_bar() {
  let info_bar = $('h3');
  if (player_play === player_one_name){
    info_bar.text(player_play + ": it is your turn, please pick a cloumn to drop your blue chip.")
  } else {
    info_bar.text(player_play + ": it is your turn, please pick a cloumn to drop your red chip.")
  }

}

function connect_four_col(row, color) {
  let cl = "#col"
  let counter = 0
  for (let i = 1;
    (i < 5 && !game_over); i++) {
    let row_id = cl + i + row
    let color_row = $(row_id).attr('value')
    let counter = 1
    if (color_row !== "gray") {
      for (let j = i + 1; j < (i + 4); j++) {
        let row_next_id = cl + j + row
        let color_next_row = $(row_next_id).attr('value')
        if (color_next_row === color_row) {
          counter += 1;
        } else {
          break;
        }
      }
      if (counter === 4) {
        $('h2').text("")
        $('h3').text("")
        $('h1').text(player_play + " has won!Refresh your browser to play again!")
        game_over = true;
      }
    }
  }
}

function connect_four_row(col, color) {
  let cl = "#col"
  let counter = 0
  for (let i = 1;
    (i < 5 && !game_over); i++) {
    let row_id = cl + col + i
    let color_row = $(row_id).attr('value')
    let counter = 1
    if (color_row !== "gray") {
      for (let j = i + 1; j < (i + 4); j++) {
        let row_next_id = cl + col + j
        let color_next_row = $(row_next_id).attr('value')
        if (color_next_row === color_row) {
          counter += 1;
        } else {
          break;
        }
      }
      if (counter === 4) {
        $('h2').text("")
        $('h3').text("")
        $('h1').text(player_play + " has won!Refresh your browser to play again!")
        game_over = true;
      }
    }
  }
}


function check_game(row, col, color) {
  connect_four_col(row, color);
  connect_four_row(col, color);
  if (!game_over) {
    change_info_bar()
  }
}

function fill_circle(circle) {
  if (!game_over) {
    let id = circle.attr('id')
    let row = id[4]
    let col = id[3]
    let color = "gray"
    if (player_play === player_one_name) {
      player_play = player_two_name;
      color = "blue"
    } else {
      player_play = player_one_name;
      color = "red"
    }

    if (color !== "gray") {
      for (let j = 7; j > 0; j--) {
        let cl = "#col" + col + j
        let filled = $(cl).attr('value')
        if (filled === "gray") {
          $(cl).attr('value', color);
          $(cl).css('background', color);
          row = j;
          check_game(row, col, color);
          break;
        }
      }
    }
  }

}

$('.circle').on('click', function() {
  fill_circle($(this))
})
