var get_row_count = prompt("Enter total row number")
var get_col_count = prompt("Enter total col number")
var player1 = prompt("Player One: Enter your name, you will be Blue")
var player1_color = 'rgb(86, 151, 255)'; // jquery return it

var player2 = prompt("Player One: Enter your name, you will be Blue")
var player2_color = 'rgb(237, 45, 73)'

var default_color = 'rgb(128, 128, 128)'

var game_on = true;
var table = $('.board') // getting rows

var ROW_COUNT = get_row_count
var COL_COUNT = get_col_count
var WIN_SEQ_NUM = 4


function create_board() {
  for (let row = 0; row < get_row_count; row++) {
    table.append('<tr></tr>');
    for (let col = 0; col < get_col_count; col++) {
      let tr = table.find('tr').eq(row)
      tr.append('<td><button type="button"></button></td>')
    }
  }
}


function reportWin(rowNum, colNum) {
  console.log("You won starting at this row, col");
  console.log(rowNum);
  console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
  return table.find('tr').eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex) {
  return table.find('tr').eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}


function checkBottom(colIndex) {
  console.log(ROW_COUNT);
  var colorReport = returnColor(ROW_COUNT - 1, colIndex);
  for (let row = ROW_COUNT - 1; row > -1; row--) {
    colorReport = returnColor(row, colIndex);
    console.log(colorReport);
    if (colorReport === default_color) {
      return row
    }
  }
}

function colorMatchCheck(one, two, three, four) {
  return (one === two && one === three && one === four && one !== default_color && one !== undefined);
}

function horizontalWincheck() {
  for (let row = 0; row < ROW_COUNT; row++) {
    for (let col = 0; col < (COL_COUNT - WIN_SEQ_NUM) + 1; col++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row, col + 1), returnColor(row, col + 2),
          returnColor(row, col + 3))) {
        console.log('horiz');
        reportWin(row, col);
        return true;
      } else {
        continue;
      }
    }
  }
}

function verticalWincheck() {
  for (let col = 0; col < COL_COUNT; col++) {
    for (let row = 0; row < (ROW_COUNT - WIN_SEQ_NUM) + 1; row++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col), returnColor(row + 2, col),
          returnColor(row + 3, col))) {
        console.log('horiz');
        reportWin(row, col);
        return true;
      } else {
        continue;
      }
    }
  }
}

function diagonalWinCheck() {
  for (var row = 0; row < ROW_COUNT; row++) {
    for (var col = 0; col < COL_COUNT; col++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col + 1), returnColor(row + 2, col + 2), returnColor(row + 3, col + 3))) {
        console.log('diag');
        reportWin(row, col);
        return true;
      } else if (colorMatchCheck(returnColor(row, col), returnColor(row - 1, col + 1), returnColor(row - 2, col + 2), returnColor(row - 3, col + 3))) {
        console.log('diag');
        reportWin(row, col);
        return true;
      } else {
        continue;
      }
    }
  }
}

var current_player = 1;
var current_name = player1;
var current_color = player1_color;


create_board()
$('h3').text(player1 + ": it's your turn, pick a column to drop in");

$('.board button').on('click', function() {
  if(game_on){
    var col = $(this).closest('td').index();

    var bottom_avail = checkBottom(col);

    changeColor(bottom_avail, col, current_color);

    if (horizontalWincheck() || verticalWincheck() || diagonalWinCheck()){
      $('h1').text(current_name + " You have won!");
      $('h3').fadeOut('fast');
      $('h2').fadeOut('fast');
      game_on = false;
    }

    current_player = current_player * -1;

    if (current_player === 1) {
      current_name = player1;
      $('h3').text(current_name+ ": it's yoru turn");
      current_color = player1_color;
    }else{
      current_name = player2;
      $('h3').text(current_name+ ": it's yoru turn");
      current_color = player2_color;
    }
  }
})
