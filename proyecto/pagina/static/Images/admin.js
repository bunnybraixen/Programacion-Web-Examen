$(function(){
    $('.btnLimpiar').click(function() {
        $('.txtEmail, .txtClave').val('');

    })

    $('.btnEnviar').click(function() {
       if( $('.txtNombre').val() == "")
       {
        alert('No especifico el nombre')
       }
       

       else if( $('.txtStock').val() == "")
       {
        alert('No especifico el stock')
       }

       else if( $('.txtStock').val() % 1 != 0)
        {
         alert('El stock ingresadoo no es valido')
        }
       else if( $('.txtDescripcion').val() == "")
       {
        alert('No especifico la descripcion')
       }

       else if( $('.txtConsola').val() == "")
       {
        alert('No especifico la consola')
       }

       else if( $('.txtPrecio').val() == "")
       {
        alert('No especifico el precio')
       }



       
       else if( $('.txtCategoria').val() == "Seleccione una categoria...")
       {
        alert('No especifico la categoria')
       }

else if(!(/^.{1,400}$/.test($('.txtNombre').val())))
{
alert('El usuario ingresado no es valido, debe ser mayor a 1 y menor a 400 caracteres')
}

else if(!(/^(?:[+\d].*\d|\d)$/.test($('.txtPrecio').val())))
{
alert('El precio ingresado no es valido, recuerde ingresarlo sin el $')
}
else if(!(/^.{4,8}$/.test($('.txtPrecio').val())))
{
alert('El precio ingresado no es valido, debe ser mayor a 4 y menor a 8 caracteres')
}

else if(!(/^(?:[+\d].*\d|\d)$/.test($('.txtStock').val())))
{
alert('El stock ingresado no es valido')
}





else if(!(/^.{50,1000}$/.test($('.txtDescripcion').val())))
{
alert('La descripcion ingresado no es valido, debe ser mayor a 50 y menor a 1000 caracteres')
}



else if( $('.txtImagen').val() == "")
    {
        if( $('.txtImagen2').val() == 'undefined') {
            
            alert('No se ingreso una imagen');
        }
        else {
            $(exampleModal).modal('show'); 
        }
    }

else {
    $(exampleModal).modal('show'); 

       }

    }

    

)
})