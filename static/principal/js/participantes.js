function adicionar() {
    var participante = document.getElementById("participante").value;
    var lista = document.getElementById("lista").innerHTML;
    var link = document.getElementById("continuar").href
    if (participante != ""){
        lista = lista+ "<li>" + participante + "</li>";
        document.getElementById("lista").innerHTML = lista;
        document.getElementById("participante").value = ""
    }
}
