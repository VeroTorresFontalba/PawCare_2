
function abrir_modal_ratings(url) {
    console.log("HOLAAA")
    console.log(url)
    $.ajax({        
        url: url,
        success: function (data) {
          $("#div_modal_rating").html(data);
          $('#myModalRatings').modal('show');
          console.log(data)
          console.log("dentro del success")
        },
        error: function (error) {
          console.log("Abrir modal error ")
 
        }
    });
}