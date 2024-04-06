$(document).ready(function () {
  const hello = $('#hello'); // cache the dom element for reuse
  // Fetch data from the URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then(response => {
  // check if the response is successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // pares the respone to JSON format
    return response.json();
  }).then(data => {
  // Extract the character name from the data
    hello.text(data.hello);
  }).catch(error => {
  // handle any errors that occurs during fetch operation
    console.error('Error fetching data:', error);
  });
});
