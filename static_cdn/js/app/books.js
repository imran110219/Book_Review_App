'use strict'

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