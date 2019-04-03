'use strict'

var auth_token = 'authToken';

function SetAuthToken(token) {
    var bearer_token = 'Bearer ' + token; 
    sessionStorage.setItem(auth_token, bearer_token);
}

function GetAuthToken() {
    return sessionStorage.getItem(auth_token);
}

function ClearAuthToken() {
    sessionStorage.setItem(auth_token, '');
}

////Setting Input focus and cursor to the right
//
// $.fn.setCursorPosition = function(pos) {
//     this.each(function(index, elem) {
//         if (elem.setSelectionRange) {
//         elem.setSelectionRange(pos, pos);
//         } else if (elem.createTextRange) {
//         var range = elem.createTextRange();
//         range.collapse(true);
//         range.moveEnd('character', pos);
//         range.moveStart('character', pos);
//         range.select();
//         }
//     });
//     return this;
// };