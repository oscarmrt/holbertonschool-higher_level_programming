$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
      const titles = data.results;
      for (const titleName in titles) {
        $('#list_movies').append(`<li>${titles[titleName].title}</li>`);
      }
    }
  });
});
