document.addEventListener('DOMContentLoaded', () => {
    fetch('/static/solucionDosFases')
        .then(response => response.text())
        .then(data => {
            const resultadosElement = document.getElementById('resultados');
            resultadosElement.textContent = data;
        })
        .catch(error => console.error('Error al cargar los resultados:', error));
});
