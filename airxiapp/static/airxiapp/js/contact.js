$(document).ready(function () {
  $(document).on("submit", ".contact-form", function (e) {
    e.preventDefault();

    $.ajax({
      type: "POST",
      url: "contact",
      data: {
        name: $("#name").val(),
        email: $("#email").val(),
        phone: $("#phone").val(),
        subject: $("#message").val(),
        message: $("#message").val(),
        csrfmiddlewaretoken: $("input[name = csrfmiddlewaretoken]").val(),
      },
      success: function (response) {
        alertify.success(response.status);
      },
    });
  });
});
