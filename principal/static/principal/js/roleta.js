var	selecionar	=	document.getElementById("selecionar");
var	letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
var i = 0;
var sorteio = Math.floor(Math.random()*25+26);

function mudar(){
    if (i < sorteio){
        console.log(document.getElementById("id_letra").value);
        document.getElementById("id_letra").value = letras[i%25];
        i++;
    }
}

selecionar.onclick	=	function() {
    var mudar_letra = window.setInterval(mudar,20);
    if (i > sorteio){
        window.clearInterval(mudar_letra);
    }
}