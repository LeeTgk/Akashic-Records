$(document).ready(function()
{

    var basetextTextBox = document.getElementById("basetext");
    var resultTextBox = document.getElementById("result");
    $('#compute').click(function()
    {
        $.ajax(
        {
            url: '',
            type: 'GET',
            cache: false,
            data: 
            {
                textbox_text: basetextTextBox.value,
                model: "SmallPortuguese",
            },
            beforeSend: function() 
            {
                resultTextBox.value = 'Carregando'
            },
            success: function(response)
            {
                resultTextBox.value = response.generated_text
            }


        });

    });

});