'use strict'

var filter_sticky = false;
var categories = [], authors = [], publications = [];

function LoadBooks() {
    var filters = {
        from_year: $("#FromYear").val(),
        to_year: $("#ToYear").val(),
        categories: categories,
        authors: authors,
        publications: publications,
        sort_by: $("#SortBy").val(),
        sort_order: $("#SortOrder").val(),
        search_string: $("#SearchBook").val()
    };
    console.log(filters);
    //Here you'll call ajax to get book data as a list and then on success response
    //You'll iterate through those data to generate books html like below
    // $.ajax({
    //     type:'POST',
    //     url: '',
    //     //your_csrf_token,
    //     data:{ filters: filters},
    //     success: function(resp){

    //     },
    //     error: function(resp){
    //         console.log(resp);
    //     }
    // });
    //This is your ajax code
    //you'll process below code inside success block
    // Here books is a static images container

    var books = [
        { image_url: "/media/da-vinci-code.jpg" },
        { image_url: "/media/angels-n-demons.jpg" },
        { image_url: "/media/inferno.jpg" },
    ];
    var books_html = '';
    $.each(books, function(i, book){        
        var single_book = '<div class="grid-item" style="position: absolute; left: 0px; top: 0px;">';
        single_book+='<div class="single-book card hvrbox">';
        single_book+='<img src="'+ book.image_url +'" alt="" class="hvrbox-layer_bottom">';
        // single_book+='<img src="{{'+ book.image.url +'}}" alt="" class="hvrbox-layer_bottom">';
        single_book+='<div class="hvrbox-layer_top">';
        single_book+='<div class="star-rating center">';
        single_book+='<p class="">4.5 <i class="fas fa-star"></i></p>';
        single_book+='<button class="waves-effect waves-light btn-small fs-10 amaranth">View Deails';
        single_book+='</button></div></div></div></div>';

        books_html += single_book;
    });

    $('.grid').empty().append(books_html);

}

function CategoryFilterChecked(e, value){
    if($(e.target).is(":checked"))
        categories.push(value);
    else
        categories.splice(categories.indexOf(value), 1);

    LoadBooks();
}

function AuthorFilterChecked(e, value){
    if($(e.target).is(":checked"))
        authors.push(value);
    else
        authors.splice(authors.indexOf(value), 1);

    LoadBooks();
}

function PublicationFilterChecked(e, value){
    if($(e.target).is(":checked"))
        publications.push(value);
    else
        publications.splice(publications.indexOf(value), 1);

    LoadBooks();
}

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

    GenerateYearFilter();
    LoadBooks();

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

$(function () {

    $('#SearchBook').keyup(function () {
        $.ajax({
            type: "POST",
            url: "/books/search/",
            data: {
                'search_text': $('#SearchBook').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR) {
    $('#search-results').html(data);
}

function BookFilter(id, value) {
    alert(id, value);
}

function GenerateYearFilter(){
    var date = new Date();
    var current_year = date.getFullYear();
    var options = '';

    for(var i=current_year; i>= 1900; i--){
        options += '<option value="' + i +'">'+ i + '</option>';
    }
    options += '<option value="1899">Earlier 1900</option>';

    $("#FromYear").empty().append(options).trigger('contentChanged');
    $("#ToYear").empty().append(options).trigger('contentChanged');

}

$('#FromYear').on('contentChanged', function() {
    $(this).formSelect();
});

$('#ToYear').on('contentChanged', function() {
    $(this).formSelect();
});