$(document).ready(function()
{
    var textBox = document.getElementById("textboxGpt2Small");
    var ResultTextBox = document.getElementById("ResultTextBox");
    $(".btn-widget").click(function()
    {
        $.ajax(
        {
            url: '',
            type: 'get',
            data: 
            {
                textbox_text: textBox.value
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