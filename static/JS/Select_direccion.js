// Función para cargar las provincias cuando seleccionas un departamento
function loadProvincias() {
    var departamento_id = document.getElementById("id_departamento").value;

    // Hacer una petición al servidor para obtener las provincias
    fetch(`/get_provincias/${departamento_id}`)
    .then(response => response.json()) // Convertir la respuesta a JSON
    .then(data => {
        // Limpiar el select de provincias y distritos
        var id_provincia = document.getElementById("id_provincia");
        id_provincia.innerHTML = '<option selected>--Seleccione su provincia--</option>';
        document.getElementById("id_distrito").innerHTML = '<option selected>--Seleccione su distrito--</option>';
        
        // Llenar el select de provincias con los datos obtenidos
        data.forEach(function(provincia) {
            var option = document.createElement("option");
            option.value = provincia[0];  // ID de la provincia
            option.text = provincia[1];   // Nombre de la provincia
            id_provincia.appendChild(option);
        });
    });
}

// Función para cargar los distritos cuando seleccionas una provincia
function loadDistritos() {
    var provincia_id = document.getElementById("id_provincia").value;

    // Hacer una petición al servidor para obtener los distritos
    fetch(`/get_distritos/${provincia_id}`)
    .then(response => response.json()) // Convertir la respuesta a JSON
    .then(data => {
        // Limpiar el select de distritos
        var id_distrito = document.getElementById("id_distrito");
        id_distrito.innerHTML = '<option selected>--Seleccione su distrito--</option>';
        
        // Llenar el select de distritos con los datos obtenidos
        data.forEach(function(distrito) {
            var option = document.createElement("option");
            option.value = distrito[0];  // ID del distrito
            option.text = distrito[1];   // Nombre del distrito
            id_distrito.appendChild(option);
        });
    });
}
