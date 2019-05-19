'use strict'

$(document).ready(function () {
    $('.user-profile-picture img, .hover-profile-image').on('mouseover', function () { 
        $('.hover-profile-image').css('opacity', 1);
    });
    
    $('.user-profile-picture img, .hover-profile-image').on('mouseout', function(e){        
        $('.hover-profile-image').css('opacity', 0);
    });

    $('#ChangeProfilePicture').on('click', function () {
        $('#ProfilePictureUrl').trigger('click');
    });

    $('.edit-basic-info').on('click', function(e){
        $(this).hide();
        $('.submit-basic-info').show();
    });
    
    $('.edit-contact-info').on('click', function(e){
        $(this).hide();
        $('.submit-contact-info').show();
    });
});

function Submit(e, target_edit_class){
    $('.' + target_edit_class).show();
    $(e.target).closest('button').hide();
    toastr.success('Have fun storming the castle!', 'Miracle Max Says');
}