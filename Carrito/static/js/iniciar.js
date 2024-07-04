const form = document.querySelector('#iniciar');
const correo = document.querySelector('#id_correo');  
const contraseña = document.querySelector('#id_password');  

form.addEventListener('submit', function(event) {
  event.preventDefault();

  // Validar el formato del correo electrónico
  const correoValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo.value);
  if (!correoValido) {
    alert('Por favor ingrese un correo electrónico válido.');
    return;
  }

  // Mostrar mensajes de error específicos
  if (correo.value.trim() === '') {
    alert('Por favor ingrese su correo electrónico.');
    return;
  }

  if (contraseña.value.trim() === '') {
    alert('Por favor ingrese su contraseña.');
    return;
  }

  // Confirmación de envío del formulario
  if (confirm('¿Está seguro de enviar sus credenciales?')) {
    form.submit();
  } else {
    // El usuario canceló el envío del formulario
    return;
  }
});


