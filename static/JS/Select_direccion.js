function loadProvincias() {
    var departamento_id = document.getElementById("id_departamento").value;

    fetch(`/get_provincias/${departamento_id}`)
    .then(response => response.json()) 
    .then(data => {
        var id_provincia = document.getElementById("id_provincia");
        id_provincia.innerHTML = '<option selected>--Seleccione su provincia--</option>';
        document.getElementById("id_distrito").innerHTML = '<option selected>--Seleccione su distrito--</option>';
        
        data.forEach(function(provincia) {
            var option = document.createElement("option");
            option.value = provincia[0];  
            option.text = provincia[1];   
            id_provincia.appendChild(option);
        });
    });
}

function loadDistritos() {
    var provincia_id = document.getElementById("id_provincia").value;

    fetch(`/get_distritos/${provincia_id}`)
    .then(response => response.json()) 
    .then(data => {
        var id_distrito = document.getElementById("id_distrito");
        id_distrito.innerHTML = '<option selected>--Seleccione su distrito--</option>';
        
        data.forEach(function(distrito) {
            var option = document.createElement("option");
            option.value = distrito[0]; 
            option.text = distrito[1];   
            id_distrito.appendChild(option);
        });
    });
}
