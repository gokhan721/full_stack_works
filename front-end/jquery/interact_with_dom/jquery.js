// $('h1').click(function() {
//   $(this).text('changed')
// })

// Key press
$('input').eq(0).keypress(function(event) {
  // console.log(event);
  if (event.which === 13) {
    $('h3').toggleClass('turnBlue')
  }
})

//on
$('h1').on('dblclick',function () {
    $(this).toggleClass('turnBlue');
})

$('p').on('mouseenter',function () {
  $(this).toggleClass('turnRed');
})

$('input').eq(1).on('click', ()=>{
  $('.container').fadeOut(3000);
})
