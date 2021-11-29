$(document).ready(function()
{


    var textBox = document.getElementById("textboxGpt2Small");
    var ResultTextBox = document.getElementById("ResultTextBox");
    $('#ComputeButton').click(function()
    {
        $.ajax(
        {
            url: '',
            type: 'GET',
            cache: false,
            data: 
            {
                textbox_text: textBox.value,
                model: "SmallPortuguese",
            },
            beforeSend: function() 
            {
                $(this).text('Loading...');
            },
            success: function(response)
            {
                $('#ResultBox').removeClass("hide")
                ResultTextBox.value = response.generated_text
            }


        });

    });

});