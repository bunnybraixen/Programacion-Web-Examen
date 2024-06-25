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
        alert('No especifico el valido')
       }

       else if( $('.txtStock').val() != 0 && $('.txtStock').val() != 1 )
        {
         alert('El valido ingresado solo puede ser 0 o 1')
        }
     
else if(!(/^.{1,400}$/.test($('.txtNombre').val())))
{
alert('El usuario ingresado no es valido, debe ser mayor a 1 y menor a 400 caracteres')
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