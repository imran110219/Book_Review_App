'use strict'

function ResizeHome(){
    $(".background-fixed img").css('width', $(document).width());
}

$("#SiteNavigation li").on('click', function(e) {
    $("#SiteNavigation li").each(function(e){
        $(this).removeClass('active');
    });
    $(this).addClass('active');
    $("#responsive-menu li").each(function(e){
        $(this).removeClass('active');
    });
    var location = $(this).find('a').data('location');
    $('html, body').animate({
        scrollTop: $("#" + location).offset().top - 50
    }, 1000);
});

function ScrollTop(e){
    $('html, body').animate({
        scrollTop: $("#NavigationBar").offset().top-50
    }, 1000);
}

window.onload = function (event) {
    ResizeHome();
};

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
});

