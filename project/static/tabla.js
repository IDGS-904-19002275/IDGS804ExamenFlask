function update(id,nombre,precio,img,marca,deporte) {
    document.getElementsByName('accion')[0].value = 'update';
    document.getElementsByName('id')[0].value = id;
    document.getElementsByName('nombre')[0].value = nombre;
    document.getElementsByName('precio')[0].value = precio;
    document.getElementsByName('img')[0].value = img;
    document.getElementsByName('marca')[0].value = marca;
    document.getElementsByName('deporte')[0].value = deporte;
}
function cancel() {
    document.getElementById('form').reset();
    document.getElementsByName('accion')[0].value = 'add';
    document.getElementsByName('id')[0].value = '';
}