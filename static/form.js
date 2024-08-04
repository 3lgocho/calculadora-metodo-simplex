function generateSecondForm(event) {
    event.preventDefault(); // Prevenir el envío del formulario

    // Obtener los valores de las variables y restricciones
    const variables = document.getElementById('variables').value;
    const restricciones = document.getElementById('cantidad_restricciones').value;

    const selectmodo = document.createElement('select');
    selectmodo.name = 'selectmodo';
    const optionmax = document.createElement('option');
    optionmax.value = 'max';
    optionmax.text = 'Maximizar';
    const optionmin = document.createElement('option');
    optionmin.value = 'min';
    optionmin.text = 'Minimizar'; 
    selectmodo.appendChild(optionmin);
    selectmodo.appendChild(optionmax);

    // Generar la función objetivo
    const funcionObjetivoDiv = document.getElementById('funcionObjetivo');
    funcionObjetivoDiv.appendChild(selectmodo);
    funcionObjetivoDiv.appendChild(document.createElement('br'))

    for (let i = 1; i <= variables; i++) {
        const input = document.createElement('input');
        input.type = 'number';
        input.name = `variable${i}`;
        input.required = true;

        funcionObjetivoDiv.appendChild(input);
        funcionObjetivoDiv.appendChild(document.createTextNode(` X${i} `));
        if (i < variables) {
            funcionObjetivoDiv.appendChild(document.createTextNode(' + '));
        }
    }
    funcionObjetivoDiv.appendChild(document.createElement('br'));

    // Generar las restricciones
    const restriccionesDiv = document.getElementById('restricciones');
    for (let j = 1; j <= restricciones; j++) {
        const restriccionLabel = document.createElement('label');
        restriccionLabel.textContent = `Restricción ${j}: `;
        restriccionesDiv.appendChild(restriccionLabel);
    
        for (let k = 1; k <= variables; k++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.name = `restriccion${j}_variable${k}`;
            input.pattern = "[-]?[0-9]+[/.]?[0-9]*";
            input.required = true;
            restriccionesDiv.appendChild(input);
            restriccionesDiv.appendChild(document.createTextNode(` X${k} `));
    
            if (k < variables) {
                restriccionesDiv.appendChild(document.createTextNode(' + '));
            }
        }
    
        // Crear y añadir el select con las opciones
        const select = document.createElement('select');
        select.name = `restriccion${j}_operador`; // Asegurar que el select tenga un nombre único
        const optionLess = document.createElement('option');
        optionLess.value = '<=';
        optionLess.text = '<= ';
    
        const optionEqual = document.createElement('option');
        optionEqual.value = '=';
        optionEqual.text = '= ';
    
        const optionGreater = document.createElement('option');
        optionGreater.value = '>=';
        optionGreater.text = '>= ';
    
        select.appendChild(optionLess);
        select.appendChild(optionEqual);
        select.appendChild(optionGreater);
        restriccionesDiv.appendChild(select);
        
        // Crear y añadir el input para la variable límite
        const inputL = document.createElement('input');
        inputL.type = 'number';
        inputL.name = `restriccion${j}_limite`;
        inputL.pattern = "[-]?[0-9]+[/.]?[0-9]*";
        inputL.required = true;
        restriccionesDiv.appendChild(inputL);   
        restriccionesDiv.appendChild(document.createElement('br'));
        restriccionesDiv.appendChild(document.createElement('br'));
    }
    
    // Ocultar el primer formulario y mostrar el segundo
    document.getElementById('firstForm').style.display = 'none';
    document.getElementById('tablasimplexform').style.display = 'block';
}
