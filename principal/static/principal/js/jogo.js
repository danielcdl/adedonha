var tempo = 15

function trocaTempo() {
    document.getElementById("tempo").value = tempo;

    if (tempo == 0){
        clearInterval(temporizador);
        document.getElementById("tempo").value = "PERDEU";
    }

    tempo = tempo - 1;
}

temporizador = setInterval(trocaTempo,1000);



function inserir(valor) {
    if (document.getElementById("tempo").value != "PERDEU"){
        var	palavra = document.getElementById("id_palavra").value;
        document.getElementById("id_palavra").value = palavra+valor;
        tempo = 15;
    }
};
