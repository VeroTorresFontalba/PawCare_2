$( function() {
    $( "#datepicker" ).datepicker({
        beforeShowDay: $.datepicker.noWeekends,
        dateFormat: "dd-mm",
        
      });
  });