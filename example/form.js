
$(function()
{
    function after_form_submitted(data) 
    {
        $('form#reused_form').hide();
        $('#success_message').show();
        $('#error_message').hide();
        $('#result').html(data.result);
        
    }

	$('#reused_form').submit(function(e)
      {
        e.preventDefault();

        $form = $(this);
        //show some response on the button
        $('button[type="submit"]', $form).each(function()
        {
            $btn = $(this);
            $btn.prop('type','button' ); 
            $btn.prop('orig_label',$btn.text());
            $btn.text('Sending ...');
        });
        

            $.ajax({
                type: "POST",
                url: 'http://127.0.0.1:5000/',
                data: $form.serialize(),
                success: after_form_submitted,
                dataType: 'json' 
            });        
        
      });	
});
