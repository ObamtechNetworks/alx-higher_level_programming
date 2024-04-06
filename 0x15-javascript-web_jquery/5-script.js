$(document).ready(function () {
  $('#add_item').click(function () {
    const newElement = $('<li>Item</li>');
    $('.my_list').append(newElement);
  });
});
