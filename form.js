document.getElementById('simplexForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const variables = document.getElementById('variables').value;
    const restricciones = document.getElementById('restricciones').value;

    if (variables > 0 && restricciones > 0) {
        // Aquí puedes manejar el envío del formulario
        console.log('Cantidad de Variables:', variables);
        console.log('Cantidad de Restricciones:', restricciones);

        // Redirigir a otra página o mostrar un formulario adicional
        // Ejemplo: window.location.href = 'siguiente_pagina.html';
    } else {
        alert('Por favor, ingrese valores válidos.');
    }
});
