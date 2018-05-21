$(document).ready(function () {
    $('#comment-form').submit(function (e) {
        e.preventDefault();
        $('#comment-box').prop("required", true);
    })

    $('#subscribe').click(function () {
        $('.modal').show()
        $('#close-modal').click(function () {
            $('.modal').show()
        })
    })

    $('#submit-s').attr('disabled', true)

    function validateEmail($email) {
        var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        return emailReg.test($email);
    }

    email = $('#email-s').val()

    if (email != '' || email != null) {
        $('#submit-s').attr('disabled', false)
    } else if (validateEmail(email)) {
        $('#submit-s').attr('disabled', false)
    } else {
        $('#submit-s').attr('disabled', true)
    }

})