var textbuscar = document.getElementById("buscar");
textbuscar.onkeyup = function(){
    buscar(this);
}

function buscar(inputbuscar){
    var valorabuscar = (inputbuscar.value).toLowerCase().trim();
    var tabla_tr = document.getElementById("tabla").getElementsByTagName("tbody")[0].rows;
    for(var i=0; i<tabla_tr.length; i++){
        var tr = tabla_tr[i];
        var textotr = (tr.innerText).toLowerCase();
        tr.className = (textotr.indexOf(valorabuscar)>=0)?"":"ocultar";
    }
}

function eliminar(objetivo){
    var opcion = confirm("Estas seguro de eliminar el libro");
    if (opcion) {
        $.ajax({
            type:'POST',
            url:'/delete',
            data:'contactFrmSubmit=1&id_libro='+objetivo,
            complete: function(e){
                location.reload();
            }
        })
    }
}

function editar(objetivo){
    var id = objetivo[0];
    var titulo = objetivo[1];
    var autor = objetivo[2];
    var estatus = objetivo[3];
    
    $('#editor').modal('show');
    $('#titulo').val(titulo);
    $('#autor').val(autor);
    $('#estatus').val(estatus);
    $('#id_libro').val(id);
}

function updateData(id=0){
    var id_libro = $('#id_libro').val();
    var titulo = $('#titulo').val();
    var autor = $('#autor').val();
    var estatus = $('#estatus').val();
    if(titulo.trim() == '' ){
        $('#validate').html('<div class="alert alert-danger"> Por favor escribe el titulo </div>');
        $('#titulo').focus();
        return false;
    }else if(autor.trim() == '' ){
        $('#validate').html('<div class="alert alert-danger"> Por favor escribe el autor </div>');
        $('#autor').focus();
        return false;
    }else{
        $.ajax({
            type:'POST',
            url:'/update',
            data:'contactFrmSubmit=1&id_libro='+id_libro+'&titulo='+titulo+'&autor='+autor+'&estatus='+estatus,
            beforeSend: function () {
                $('#submit_btn').attr("disabled","disabled");
                $('.modal-body').css('opacity', '.5');
            },
            complete: function(data){
                location.reload()
            }
        });
    }
}

function addCsv() {
    var csv = $('#csv').val()
    $.ajax({
        type:'POST',
        url:'/newcsv',
        data:'contactFrmSubmit=1&csv='+csv,
        beforeSend: function () {
            $('#csv_submit_btn').attr("disabled","disabled");
            $('.modal-body').css('opacity', '.5');
        },
        complete: function(data){
            location.reload()
        }
    });
}
