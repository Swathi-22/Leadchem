$(document).ready(function () {
    $('#whatsapp-form').hide()
});


$('#whatsapp-form').submit(function () {

    var phone = '919539438918';
    var Compname = $('#name').val()
    var quanity = $('#qty').val()
    var proTitle = $('#title1').val()
    const text = [
        'Product Name:' + proTitle,
        'Company Name: ' + Compname,
        'Quantity: ' + quanity
        

    ].join("\n") // change to what you want sep to be
    const action = "https://wa.me/" + phone + "?text=" + encodeURIComponent(text);
    window.location.href = action;

    return false
})


