function generateSecondForm(event) {
    event.preventDefault(); // Prevenir el envío del formulario

    // Obtener los valores de las variables y restricciones
    const variables = document.getElementById('variables').value;
    const restricciones = document.getElementById('restricciones').value;

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

    // Ocultar el primer formulario y mostrar el segundo
    document.getElementById('firstForm').style.display = 'none';
    document.getElementById('tablasimplexform').style.display = 'block';
}
