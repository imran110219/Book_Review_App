'use strict'

function Register(event) {
    $('#registerModal').modal('toggle');
}

function RegisterUser(e) {

}

function Login() {
    $.ajax({
        type: "POST",
        url: 'login/',
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
            else {
                $("#errorlogin").html("The User Name and Password do not match.");
            }
        }
    });
}