
  $(function() {
    $('button').click(function() {
      var value = this.value;
        $.ajax({
            url : '/control',
            data : { 
              'light' : value 
              },
            type : 'POST',
            success : function(response) {
                console.log(response);
            },
            error : function(error) {
                console.log(error);
            }
        });
    });
});
