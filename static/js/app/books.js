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
    if(width < 976) {
        $("#BookContentRoot").removeClass('card').removeClass('responsive-filter');
        $("#BookContentFilter").removeClass('card').addClass('card').addClass('responsive-filter');
        $("#BookContentBody").removeClass('card').addClass('card');

        if($("#BookContentFilter").css('display') == 'block') {
            $('.filter-toggler').addClass('red darken-4');
            $('.filter-toggler i').removeClass('fa-chevron-right').addClass('fa-times');
        }
        else{            
            $('.filter-toggler').removeClass('red darken-4');
            $('.filter-toggler i').removeClass('fa-times').addClass('fa-chevron-right');
        }
        
        $('.filter-toggler').show();
    }
    else {
        $("#BookContentFilter").removeClass('card').removeClass('responsive-filter');
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
        $('.filter-toggler').removeClass('red darken-4');
        $('.filter-toggler i').removeClass('fa-times').addClass('fa-chevron-right');
    }
    else{
        $('.filter-toggler').addClass('red darken-4');
        $('.filter-toggler i').removeClass('fa-chevron-right').addClass('fa-times');
    }
    
    $("#BookContentFilter").toggle('slide', {direction: 'right'});
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

$(window).on('scroll', function() {
    var document_top = $(window).scrollTop() + 64;
    var element_top = $(".filter-toggler").offset().top;
    console.log($(".filter-toggler").hasClass('sticky-close'));
    if(document_top > element_top){
        if($(".filter-toggler").hasClass('sticky-close') == false)
            $(".filter-toggler").addClass('sticky-close');
    }
    else
        $(".filter-toggler").removeClass('sticky-close');
});