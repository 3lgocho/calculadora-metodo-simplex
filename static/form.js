function generateSecondForm(event) {
    event.preventDefault(); // Prevenir el envío del formulario

    // Obtener los valores de las variables y restricciones
    const variables = document.getElementById('variables').value;
    const restricciones = document.getElementById('restricciones').value;

    // Guardar los valores en localStorage
    localStorage.setItem('variables', variables);
    localStorage.setItem('restricciones', restricciones);

    // Redireccionar a la segunda página
    window.location.href = 'tablasimplexform.html';
}

window.onload = function() {
    // Verificar si estamos en la segunda página
    if (window.location.pathname.endsWith('tablasimplexform.html')) {
        // Obtener los valores de variables y restricciones de localStorage
        const variables = localStorage.getItem('variables');
        const restricciones = localStorage.getItem('restricciones');

        // Generar la función objetivo
        const funcionObjetivoDiv = document.getElementById('funcionObjetivo');
        funcionObjetivoDiv.innerHTML = '<label>Función Objetivo:</label>';
        for (let i = 1; i <= variables; i++) {
            const input = document.createElement('input');
            input.type = 'text';
            input.name = `variable${i}`;
            input.placeholder = `X${i}`;
            funcionObjetivoDiv.appendChild(input);
            if (i < variables) {
                funcionObjetivoDiv.appendChild(document.createTextNode(' + '));
            }
        }
        funcionObjetivoDiv.appendChild(document.createElement('br'));

        // Generar las restricciones
        const restriccionesDiv = document.getElementById('restriccionesContenedor');
        restriccionesDiv.innerHTML = '<label>Restricciones:</label>';
        for (let j = 1; j <= restricciones; j++) {
            const restriccionLabel = document.createElement('label');
            restriccionLabel.textContent = `Restricción ${j}:`;
            restriccionesDiv.appendChild(restriccionLabel);
            for (let k = 1; k <= variables; k++) {
                const input = document.createElement('input');
                input.type = 'text';
                input.name = `restriccion${j}_variable${k}`;
                input.placeholder = `X${k}`;
                restriccionesDiv.appendChild(input);
                if (k < variables) {
                    restriccionesDiv.appendChild(document.createTextNode(' + '));
                }
            }
            restriccionesDiv.appendChild(document.createElement('br'));
        }
    }
};
