$(document).ready(function () {
    

    $('#whatsapp-form').hide()
});


$('#whatsapp-form').submit(function () {

    var phone = '917594939666';
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
// $('.Show').click(function() {
//     $('#target').show(500);
//     $('.Show').hide(0);
//     $('.Hide').show(0);
// });
// $('.Hide').click(function() {
//     $('#target').hide(500);
//     $('.Show').show(0);
//     $('.Hide').hide(0);
// });
$('.toggle').click(function() {
    
    $('#target').fadeToggle();
});
