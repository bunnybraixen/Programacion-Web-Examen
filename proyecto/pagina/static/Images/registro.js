$(function(){
    $('.btnLimpiar').click(function() {
        $('.txtEmail, .txtClave').val('');

    })

    $('.btnLogin').click(function() {
        if( $('.loginEmail').val() == "")
        {
         alert('No especifico el correo')
        }
        
 
        else if( $('.loginClave').val() == "")
        {
         alert('No especifico la clave')
        }
        else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('.loginEmail').val())))
        {
        alert('El correo ingresado no es valido')
        }

        else {

            $(exampleModal1).modal('show'); 

       }
    })

    $('.btnEnviar').click(function() {
       if( $('.txtEmail').val() == "")
       {
        alert('No especifico el correo')
       }
       

       else if( $('.txtClave').val() == "")
       {
        alert('No especifico la clave')
       }
       else if( $('.txtClaveVer').val() == "")
       {
        alert('No especifico la clave')
       }

       else if( $('.txtUsuario').val() == "")
       {
        alert('No especifico el usuario')
       }

       else if( $('.txtTelefono').val() == "")
       {
        alert('No especifico el telefono')
       }

       else if( $('.txtFechaNacimiento').val() == "")
       {
        alert('No especifico la Fecha de Nacimiento')
       }
       else if( $('.txtDireccion').val() == "")
       {
        alert('No especifico la direccion')
       }

       else if( $('.txtRut').val() == "")
       {
        alert('No especifico el rut')
       }
       
       else if( $('.txtRegion').val() == "Seleccione una region...")
       {
        alert('No especifico la region')
       }

       else if(!( $('.txtClave').val() == $('.txtClaveVer').val()))
       {
        alert('Las claves no coinciden')
       }
       else if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('.txtEmail').val())))
{
alert('El correo ingresado no es valido')
}

else if(!(/^(?:[+\d].*\d|\d)$/.test($('.txtTelefono').val())))
{
alert('El numero de telefono ingresado no es valido')
}

else if(!(/^(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])$/.test($('.txtRut').val())))
{
alert('El rut ingresado no es valido, recuerde usar puntos y guion')
}

else if(!(/^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}$/.test($('.txtFechaNacimiento').val())))
{
alert('La fecha ingresada no es valido')
}


else if(!(/^.{4,20}$/.test($('.txtUsuario').val())))
{
alert('El usuario ingresado no es valido, debe ser maayor a 4 y menor a 20 caracteres')
}

else if (!($("input[class=checkbox]").is(":checked"))) {
    alert("Debe aceptar los terminos y cndiciones");
} 
  

else if (!(/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.* ).{8,50}$/.test($('.txtClave').val())))
{
    alert('La clave ingresada no es valida, debe tener una letra miniscula, una mayuscula, un digito, un caracter especial, no espacios y minimo 8 caracteres')
   }
   
else {
    $(exampleModal).modal('show'); 

       }

    }

    

)
})