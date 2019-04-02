'use strict'

function ResizeHome(){
    $(".background-fixed img").css('width', $(document).width());
}

// $("#SiteNavigation li").on('click', function(e) {
//     $("#SiteNavigation li").each(function(e){
//         $(this).removeClass('active');
//     });
//     $(this).addClass('active');
//     $("#responsive-menu li").each(function(e){
//         $(this).removeClass('active');
//     });
//     var location = $(this).find('a').data('location');
//     $('html, body').animate({
//         scrollTop: $("#" + location).offset().top - 50
//     }, 1000);
// });

function SwitchActiveClass(){
    var title = $(document).attr('title').split('|')[1].toLowerCase().trim();
    $("#SiteNavigation li a").each(function(e){
        $(this).closest('li').removeClass('active');
        if($(this).data('location') == title){
            $(this).closest('li').addClass('active');
        }
    });

    $("#responsive-menu li a").each(function(e){
        $(this).closest('li').removeClass('active');
        if($(this).data('location') == title){
            $(this).closest('li').addClass('active');
        }
    });
}

function ScrollTop(e){
    $('html, body').animate({
        scrollTop: $("#NavigationBar").offset().top-50
    }, 1000);
}

function FooterPlacement(){
    if($('body').height() <= $(window).height()){
        $('footer').addClass('sticky-footer');
    }
    else{
        $('footer').removeClass('sticky-footer');
    }
}

window.onresize = function(event) {
    ResizeHome();
};

$(window).on('scroll', function() {
    var scrollPosition = $(this).scrollTop();
    if (scrollPosition >= 100)
        $(".scroll-top").fadeIn(500);
    else
        $(".scroll-top").fadeOut(500);

    if (scrollPosition >= 200)
        $('.site-nav').css('height', '60');
    else
        $('.site-nav').css('height', '100');

    // if($(window).scrollTop() > $('#home').offset().top - 50){
    //     console.log("Out");
    // }
    // else
    //     console.log("Inn");
});

$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();
    $('.tabs').tabs();
    SwitchActiveClass();
    ResizeHome();
    FooterPlacement();
    /** Review incomplete task **/
    
    // $("#review-edit-btn").click(function () {
    //     var revid = $(this).data('revid');
    //     $("#review_" + revid).load("review_edit.html");
    // });

    // $(document).on('click', '.edit', function () {
    //     $id = $(this).attr('name');
    //     window.location = "reviews/" + $id + "/edit/";
    // });

    // var id = $(this).attr('revid');
    // alert(id);
    // $("#review-delete-btn").click(function () {
    //     $id = $(this).attr('revid');
    //     alert($id);
    //     $.ajax({
    //         url: '/books/reviews/' + $id + '/delete/',
    //         type: 'POST',
    //         data: {
    //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         success: function (data) {
    //             $(".review").html(data);
    //             $(".review").hide();
    //             alert("Deleted!");
    //         }
    //     });
    // });

    // $("#review-delete-btn").on('click', function (event) {
    //     event.preventDefault();

    //     // for referencing this later in this function
    //     var _button = $(this);
    //     var revid = $(this).data('revid');

    //     alert(revid);

    //     bootbox.confirm({
    //         title: "Destroy planet?",
    //         message: "Do you want to delete? This cannot be undone.",
    //         buttons: {
    //             cancel: {
    //                 label: '<i class="fa fa-times"></i> Cancel'
    //             },
    //             confirm: {
    //                 label: '<i class="fa fa-check"></i> Confirm'
    //             }
    //         },
    //         callback: function (result) {
    //             // result will be a Boolean value
    //             if (result) {
    //                 // this encodes the form data
    //                 var data = _button.closest('form').serialize();

    //                 $.post('{% url "delete" pk=revid %}', data).done(function (response, status, jqxhr) {
    //                     // status code 200 response
    //                 })
    //                     .fail(function (jqxhr, status, errorThrown) {
    //                         // any other status code, including 30x (redirects)
    //                     });
    //             }
    //         }
    //     });
    // });
});

