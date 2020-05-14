$(() => {
  $('#red_header').click(() => {
    $('header').toogleClass('red', 'green');
  });
});
