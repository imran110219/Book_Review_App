'use strict'

var filter_sticky = false;

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

    $('.grid').isotope({
        itemSelector: '.grid-item',
        layoutMode: 'fitRows'
    });
});

window.onresize = function(event) {
    BooksPageResponsive();
};

window.onload = function (event) {
    BooksPageResponsive();
    StickyFilterToggle();
};

function BooksPageResponsive(){
    var width = $(window).width();
    if(width < 976) {
        $("#BookContentRoot").removeClass('card');
        $("#BookContentFilter").removeClass('card').addClass('card');
        $("#BookContentBody").removeClass('card').addClass('card');

        if($("#BookContentFilter").css('display') == 'block') {
            $('.filter-toggler').addClass('red');
            $('.filter-toggler i').removeClass('fa-chevron-right').addClass('fa-times');
        }
        else{            
            $('.filter-toggler').removeClass('red');
            $('.filter-toggler i').removeClass('fa-times').addClass('fa-chevron-right');
        }
        
        $('.filter-toggler').show();
    }
    else {
        $("#BookContentFilter").removeClass('card');
        $("#BookContentBody").removeClass('card');
        $("#BookContentRoot").removeClass('card').addClass('card');
        $('.filter-toggler').hide();
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

function ToggleFilter(e){
    if($(e.target).closest('a').hasClass('red')){
        $('.filter-toggler').removeClass('red');
        $('.filter-toggler i').removeClass('fa-times').addClass('fa-chevron-down');
    }
    else{
        $('.filter-toggler').addClass('red');
        $('.filter-toggler i').removeClass('fa-chevron-down').addClass('fa-times');
    }

    $('html, body').animate({
        scrollTop: $("#BookContentFilter").offset().top-64
    }, 1000);

    $(".filter-section").toggle('slide', {direction: 'up'});
}

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

function IsTotallyOutsideViewport(element){
	var document_top = $(window).scrollTop();

	var element_top = $(element).offset().top;
	var element_bottom = element_top + $(element).height();
	
	return (document_top >= element_bottom);
}

$(document).on('scroll', function() {
    StickyFilterToggle();
});

function StickyFilterToggle(){
    if($(".books").get(0) !== undefined){
        var document_top = $(window).scrollTop() + 64;
        var element_top = $(".filter-header").offset().top;
        var element_bottom = element_top + $("#BookContentFilter").height();
        if(document_top > element_top && document_top <= element_bottom - 50){
            if(filter_sticky == false){
                $(".filter-toggler").addClass('sticky-close');
                filter_sticky = true;
            }

            console.log(document_top + " >> " + (element_bottom - 50));
        }
        else if(document_top > element_bottom - 50 && filter_sticky){
            $(".filter-toggler").removeClass('sticky-close');
            filter_sticky = false;
        }
        else {
            $(".filter-toggler").removeClass('sticky-close');
            filter_sticky = false;
        }
    }
}