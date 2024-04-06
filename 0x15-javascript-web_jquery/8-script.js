$(document).ready(function () {
  const listMovies = $('#list_movies'); // cache the dom element for reuse
  // Fetch data from the URL
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json').then(response => {
  // check if the response is successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // pares the respone to JSON format
    return response.json();
  }).then(data => {
  // Extract the character name from the data
    data.results.forEach(film => {
      // Append the title of the film to the list
      listMovies.append(`<li>${film.title}</li>`);
    });
  }).catch(error => {
  // handle any errors that occurs during fetch operation
    console.error('Error fetching data:', error);
  });
});
