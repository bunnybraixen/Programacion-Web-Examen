

$(function(){
    const precioOG1 = $('#precio').text()
    const precioOG2 = $('#precio2').text()
    const precioOG3 = $('#precio3').text()
    const precioOG4 = $('#precio4').text()
    const precioOG5 = $('#precio5').text()
    const precioOG6 = $('#precio6').text()


    $('.btnLimpiar').click(function() {
        $('.txtEmail, .txtClave').val('');

    })

    $('.btnDivisa').click(function() {
        $.getJSON('https://mindicador.cl/api', function(data) {
        var dailyIndicators = data;
        const dolar = dailyIndicators.dolar.valor
        console.log($('#precio2').text())
        $('#precio').text((Number($('#precio').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio2').text((Number($('#precio2').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio3').text((Number($('#precio3').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio4').text((Number($('#precio4').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio5').text((Number($('#precio5').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio6').text((Number($('#precio6').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))

        document.getElementById('btnDivisa').style.visibility = 'hidden';
        $("#btnDivisaCLP").show();
        $(".btnDivisaCLP").show();
        document.getElementById('btnDivisaCLP').style.visibility = 'visible';
        document.getElementById('btnDivisaCLP').style.visibility = 'block';
    }).fail(function() {
        console.log('Error al consumir la API!');
    });
    }
)

$('.btnDivisaCLP').click(function() {
    $.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;
    const dolar = dailyIndicators.dolar.valor
    console.log($('#precio2').text())
    $('#precio').text(precioOG1)
    $('#precio2').text(precioOG2)
    $('#precio3').text(precioOG3)
    $('#precio4').text(precioOG4)
    $('#precio5').text(precioOG5)
    $('#precio6').text(precioOG6)
    document.getElementById('btnDivisaCLP').style.visibility = 'hidden';
    document.getElementById('btnDivisa').style.visibility = 'visible';
    
}).fail(function() {
    console.log('Error al consumir la API!');
});
})

})