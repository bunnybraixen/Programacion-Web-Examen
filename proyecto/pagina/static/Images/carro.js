$(function(){
    const precioOG = []
    const precioOG1 = $('#precio').text()
    const precioOG2 = $('#precio2').text()
    const precioOG3 = $('#precio3').text()
    const precioOG4 = $('#precio4').text()
    
    function dinero(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    }
    for (let i = 0; i < 1000; i++) {
        precioOG[i] = $('#'+i).text()
    } 
    
    

    window.onload = function() {
        const precioOG1 = Number($('#precio').text().replace(/[.,\s]/g, ''))
        const precioOG2 = Number($('#precio2').text().replace(/[.,\s]/g, ''))
        const precioOG3 = Number($('#precio3').text().replace(/[.,\s]/g, ''))
        const precioOG4 = Number($('#precio4').text().replace(/[.,\s]/g, ''))
        var precioFinal = 0
        for (let i = 0; i < 1000; i++) {
            var precioFinal = precioFinal + Number($('#'+i).text().replace(/[.,\s]/g, ''))
        } 
        console.log(precioFinal)
        $('#precio5').text(dinero(precioFinal))
        globalThis.precioOG5 = $('#precio5').text()
        console.log($('#precio5').text())
        
      };
    



    $('.btnLimpiar').click(function() {
        $('.txtEmail, .txtClave').val('');

    })

    $('.btnDivisa').click(function() {
        $.getJSON('https://mindicador.cl/api', function(data) {
        var dailyIndicators = data;
        const dolar = dailyIndicators.dolar.valor
        $('#precio').text((Number($('#precio').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio2').text((Number($('#precio2').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio3').text((Number($('#precio3').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        $('#precio4').text((Number($('#precio4').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        for (let i = 0; i < 1000; i++) {
            $('#'+i).text((Number($('#'+i).text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        } 
        $('#precio5').text((Number($('#precio5').text().replace(/[.,\s]/g, '')) / dolar).toFixed(2))
        
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
    console.log(precioOG5)
    $('#precio').text(precioOG1)
    $('#precio2').text(precioOG2)
    $('#precio3').text(precioOG3)
    $('#precio4').text(precioOG4)
    $('#precio5').text(precioOG5)
    for (let i = 0; i < 1000; i++) {
        $('#'+i).text(precioOG[i])
    } 
    document.getElementById('btnDivisaCLP').style.visibility = 'hidden';
    document.getElementById('btnDivisa').style.visibility = 'visible';
    
}).fail(function() {
    console.log('Error al consumir la API!');
});
})

})