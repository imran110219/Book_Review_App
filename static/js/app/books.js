'use strict'

$(document).ready(function(){
    var owl = $('.owl-carousel');
    owl.owlCarousel({
        items:1,
        loop:true,        
        animateOut: 'zoomOut',
        animateIn: 'zoomIn',
        margin:10,
        autoplay:true,
        autoplayTimeout:3500,
        autoplayHoverPause:true,
        smartSpeed:450
    });
});

window.onresize = function(event) {
    BooksPageResponsive();
};

window.onload = function (event) {
    BooksPageResponsive();
};

function BooksPageResponsive(){
    var width = $(window).width();
    console.log(width + " >> " + $("#BookContentRoot").hasClass('card'));
    if(width < 976) {
        $("#BookContentRoot").removeClass('card');
        $("#BookContentFilter").removeClass('card').addClass('card');
        $("#BookContentBody").removeClass('card').addClass('card');
    }
    else {
        $("#BookContentFilter").removeClass('card');
        $("#BookContentBody").removeClass('card');
        $("#BookContentRoot").removeClass('card').addClass('card');
    }
}

function ChangeAuthor(e) {
    console.log($(e.target).val());
}

function ChangePublisher(e) {
    console.log($(e.target).val());
}

function ChangeRating(e) {
    console.log($(e.target).val());
}

function ChangeTags(e) {
    console.log($(e.target).val());
}

function LoadBookList(params) {
    
}

// function SwitchFilterState(e) {
//     if($(e.target).hasClass('fa-arrow-circle-up')){
//         $("#Filter").slideUp();
//         $(e.target).removeClass('fa-arrow-circle-up').addClass('fa-arrow-circle-down');
//     }
//     else{
//         $("#Filter").slideDown();
//         $(e.target).removeClass('fa-arrow-circle-down').addClass('fa-arrow-circle-up');
//     }
// }

function FilterGroupStateChange(e){
    var identifier = "#" + $(e.target).closest('a').data('target');
    var selected_element = $(identifier);
    if(selected_element.css('display') == 'none') {
        selected_element.slideDown();
        $(e.target).removeClass('fa-plus-square').addClass('fa-minus-square');
    }
    else {
        selected_element.slideUp();
        $(e.target).removeClass('fa-minus-square').addClass('fa-plus-square');
    }
}