

$(function(){
    const precioOG1 = $('#precio').text()



    $('.btnDivisa').click(function() {
        $.getJSON('https://mindicador.cl/api', function(data) {
        var dailyIndicators = data;
        const dolar = dailyIndicators.dolar.valor
        console.log($('#precio').text().replace(/[.,\s]/g, ''))
        $('#precio').text((Number($('#precio').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))


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
    console.log($('#precio').text())
    $('#precio').text(precioOG1)
    document.getElementById('btnDivisaCLP').style.visibility = 'hidden';
    document.getElementById('btnDivisa').style.visibility = 'visible';
    
}).fail(function() {
    console.log('Error al consumir la API!');
});
})

})