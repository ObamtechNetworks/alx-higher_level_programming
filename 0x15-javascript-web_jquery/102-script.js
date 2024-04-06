$(document).ready(function() {
  $("#btn_translate").click(function() {
    // Retrieve the language code entered by the user
    var languageCode = $("#language_code").val();

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
  });
});
