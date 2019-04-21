'use strict'

function Register(event) {
    $('#registerModal').modal('toggle');
}

function RegisterUser() {
    $.ajax({
        type: "POST",
        url: window.location.origin + '/register/',
        data: {
            'register_user_name': $('#register_user_name').val(),
            'register_email_address': $('#register_email_address').val(),
            'register_password': $('#register_password').val(),
            'register_confirm_password': $('#register_confirm_password').val(),
            'first_name': $('#first_name').val(),
            'last_name': $('#last_name').val(),
            'occupation': $('#occupation').val(),
            'mobile_number': $('#mobile_number').val()
            // 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function (data) {
            console.log(data);
            if (data['message'] == "duplicate") {
                $("#errorlogin").html("This User already exists.");
            }
            else {
                window.location.href = window.location.origin + '/'
            }
        }
    });
}

$('#register_password, #register_confirm_password').on('keyup', function () {
  if ($('#register_password').val() == $('#register_confirm_password').val()) {
    $('#message').html('Matching').css('color', 'green');
  } else
    $('#message').html('Not Matching').css('color', 'red');
});

function Login() {

    $.ajax({
        type: "POST",
        url: window.location.origin + '/login/',
        data: {
            'username': $('#username').val(),
            'password': $('#password').val()
            // 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function (data) {
            console.log(data);
            if (data['message'] == "inactive") {
                $("#errorlogin").html("Please verify this User Name.");
            }
            else if (data['message'] == "invalid") {
                $("#errorlogin").html("The User Name and Password do not match.");
            }
            else {
                window.location.href = window.location.origin + '/'
            }
        }
    });
}