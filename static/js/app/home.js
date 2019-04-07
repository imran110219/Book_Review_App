'use strict'

$(document).ready(function(){
    $(".owl-carousel-trending-books").owlCarousel({
        loop:true,
        margin:50,
        autoplay:true,
        autoplayTimeout:1500,
        autoplayHoverPause:true,
        smartSpeed:600,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:4
            }
        }
    });
    $(".owl-carousel-quotes").owlCarousel({
        loop:true,
        margin:50,
        autoplay:true,
        autoplayTimeout:3500,
        items: 1,
        smartSpeed:800,
        navs: false
    });    
});