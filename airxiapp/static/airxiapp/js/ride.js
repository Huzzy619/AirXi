$(document).ready(function () {
  $('input[type=radio][name="taxi"]').change(function (e) {
    e.preventDefault();
    console.log($(this).val());

    $.ajax({
      type: "GET",
      url: "/model",
      data: {
        Type: $(this).val(),
      },
      success: function (response) {
        console.log(response);
        $("#model_form").html(response)

        
      },
    });
  });
});

// model = document.querySelector('#model')
