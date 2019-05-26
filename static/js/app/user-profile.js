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

    //This is view switch function
    $('.user-action-menu ul li').on('click', function(e){
        $('.user-action-menu ul li').each(function (e) {
            $(this).removeClass('li-active');
        });
        
        SwitchProfileViews($(this).attr('rel'));
        $(this).addClass('li-active');
        $('html, body').animate({
            scrollTop: $("#user-tab-page-title").offset().top-80
        }, 700);
    });

    function SwitchProfileViews(view_id) {
        if(view_id === 'BasicInfo'){ 
            $('#Readings').hide(); $('#Mailbox').hide();
            $('#BasicInfo').fadeIn(200).show();
            // $('#user-tab-page-title').text('Profile');
        }
        else if(view_id === 'Readings'){
            LoadReadingsGrid();
            LoadWishlistGrid();
            $('#BasicInfo').hide(); $('#Mailbox').hide();
            $('#Readings').fadeIn(200).show(); 
            // $('#user-tab-page-title').text('Readings');
        }
        else{
            $('#BasicInfo').hide(); $('#Readings').hide();
            $('#Mailbox').fadeIn(200).show();
            // $('#user-tab-page-title').text('Mailbox');
        }
    }
});

function ToggleProfilePage(e){
    // $('.profile-body').removeClass();
}

function Submit(e, target_edit_class){
    $('.' + target_edit_class).show();
    $(e.target).closest('button').hide();
    toastr.success('Have fun storming the castle!', 'Miracle Max Says');
}

function LoadWishlistGrid(){
    $("#WishList").kendoGrid({
        dataSource: {
            type: "odata",
            transport: {
                read: "https://demos.telerik.com/kendo-ui/service/Northwind.svc/Orders"
            },
            schema: {
                model: {
                    fields: {
                        OrderID: { type: "number" },
                        Freight: { type: "number" },
                        ShipName: { type: "string" },
                        OrderDate: { type: "date" },
                        ShipCity: { type: "string" }
                    }
                }
            },
            pageSize: 10,
            serverPaging: true,
            serverFiltering: true,
            serverSorting: true
        },
        scrollable: true,
        height: 400,
        sortable: true,
        pageable: true,
        columns: [{
                field:"OrderID",
                filterable: false,
                width: 100
            },
            {
                field: "Freight",
                width: 150
            },
            {
                field: "OrderDate",
                title: "Order Date",
                format: "{0:MM/dd/yyyy}",
                width: 150
            }, {
                field: "ShipName",
                title: "Ship Name",
                width: 250
            }, {
                field: "ShipCity",
                title: "Ship City",
                width: 150
            }
        ]
    });
}

function LoadReadingsGrid(){
    $("#TotalReadings").kendoGrid({
        dataSource: {
            type: "odata",
            transport: {
                read: "https://demos.telerik.com/kendo-ui/service/Northwind.svc/Orders"
            },
            schema: {
                model: {
                    fields: {
                        OrderID: { type: "number" },
                        Freight: { type: "number" },
                        ShipName: { type: "string" },
                        OrderDate: { type: "date" },
                        ShipCity: { type: "string" }
                    }
                }
            },
            pageSize: 10,
            serverPaging: true,
            serverFiltering: true,
            serverSorting: true
        },
        scrollable: true,
        height: 400,
        sortable: true,
        pageable: true,
        columns: [{
                field:"OrderID",
                filterable: false,
                width: 100
            },
            {
                field: "Freight",
                width: 150
            },
            {
                field: "OrderDate",
                title: "Order Date",
                format: "{0:MM/dd/yyyy}",
                width: 150
            }, {
                field: "ShipName",
                title: "Ship Name",
                width: 250
            }, {
                field: "ShipCity",
                title: "Ship City",
                width: 150
            }
        ]
    });
}