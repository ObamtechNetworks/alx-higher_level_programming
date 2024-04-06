$(document).ready(function() {
  function fetchTranslation() {
    // Retrieve the language code entered by the user
    const languageCode = $("#language_code").val();

    // Make an AJAX request to fetch the translation
    $.ajax({
	  url: "https://hellosalut.stefanbohacek.dev/?lang=ja",
      type: "GET",
      data: { lang: languageCode },
      success: function(response) {
        // Display the translation in the hello div
        $("#hello").text(response.hello);
      },
      error: function(xhr, status, error) {
        // Handle errors if any
        console.error("Error:", error);
      }
    });
  }
  // Triger translation when the translate button is clicked
  $('#btn_translate').click(function() {
    fetchTranslation();
  });
  $('#language_code').keypress(function(event) {
    // check if the key pressed is ENTER (key code 13)
	if (event.which === 13) {
	  fetchTranslation();
	}
  });
});
