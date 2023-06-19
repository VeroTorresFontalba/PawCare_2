function abrir_modal3(url){
    console.log("Modal 3 abierto")

        $.ajax({
            url:url ,
            success:function(data){
                $("#reservar").html(data);
                $('#MyModalReserva').modal('show');
                console.log(data)
            },
            error:function(){
            alert("No carga Modal")
            }
        });
}

function click(url){
    console.log(url)
}