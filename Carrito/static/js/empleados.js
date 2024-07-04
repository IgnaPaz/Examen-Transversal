// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://jsonplaceholder.typicode.com/users/';

    // Fetch para obtener los datos
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => mostrarData(data))
        .catch(error => console.error('Error fetching data:', error));

    // Función para mostrar los datos en la tabla
    const mostrarData = (data) => {
        let body = "";
        data.forEach(user => {
            body += `<tr><td>${user.id}</td><td>${user.name}</td><td>${user.email}</td></tr>`;
        });
        document.getElementById('data').innerHTML = body;
    };
});
