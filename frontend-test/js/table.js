$(document).ready(function() {
    $('#search_button').click(function(){
        var word = $('#search_field').val();
        $.ajax({
        url: `http://localhost:5000/companies/${word}`,
        type: "get",
        success: function(response) {
            clearTable();
            if(response.length)
                populateTable(response);
            else
                populateTableWithNotFound();
        },
        error: function(xhr) {
            clearTable();
            populateTableWithNotFound();
        }
        });
    });
});

function populateTable(data) {
    const len = data.length;
    for(let i = 0; i < len; i++) {
        const nome = data[i].nome;
        const categorias = data[i].categorias;
        const rua = data[i].rua;
        const numero = data[i].numero;
        const bairro = data[i].bairro;
        const cep = data[i].cep;
        const telefone = data[i].telefone;

        $('#table tbody').append("<tr><td>"+ nome +"</td><td>"+ rua +"</td><td>"+ numero +"</td><td>"+ bairro +"</td><td>"+ cep +"</td><td>"+ telefone +"</td><td>"+ categorias +"</td></tr>");
    }
}

function clearTable() {
    $('#table tbody').empty();
}

function populateTableWithNotFound() {
    $('#table tbody').append("<tr><td colspan='7' align='center'>Foi mal fera, não achei nenhuma empresa que coleta isso aí que tu quer</td></tr>");
}