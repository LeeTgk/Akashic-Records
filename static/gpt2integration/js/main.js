$(document).ready(function()
{
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    var basetextTextBox = document.getElementById("basetext");
    var resultTextBox = document.getElementById("result");
    var postTitle = document.getElementById("post-title");
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
            },
            error: function(xhr, textStatus, errorThrown )
             {
                if (textStatus == 'timeout') {
                    this.tryCount++;
                    if (this.tryCount <= this.retryLimit) {
                        //try again
                        $.ajax(this);
                        return;
                    }            
                    return;
                }
                if (xhr.status == 500) {
                    //handle error
                } else {
                    //handle error
                }
            }


        });

    });

    $('#openModal').click(function()
        {
            $('#popUpModal').modal('show');
    });

    $('.close').click(function()
    {
        $('#popUpModal').modal('hide');
    });


    $('#save').click(function()
    {
        var titletext = postTitle.value
        if(titletext != '')
        {
            $.ajax(
            {
                url: '',
                type: 'POST',
                cache: false,
                data: 
                {
                    title: titletext,
                    generatorText: basetextTextBox.value,
                    textContent: resultTextBox.value,
                    csrfmiddlewaretoken: csrf,
                },
                beforeSend: function() 
                {
                    //console.log(csrf)
                },
                success: function()
                {
                    resultTextBox.value = ''
                    basetextTextBox.value =''
                    postTitle.value =''
                    $('#popUpModal').modal('hide');
                }
        
            });
        }
        else{
            postTitle.style["border"] = "1.5px solid #d83e40";
            animateCSS('#titleInputBlock','bounce').then( ()=>
            {
                postTitle.style["border"] = "1px solid #222";
            });
        }

    });


    const animateCSS = (element, animation, prefix = 'animate__') =>
        // We create a Promise and return it
        new Promise((resolve, reject) => {
            const animationName = `${prefix}${animation}`;
            const node = document.querySelector(element);

            node.classList.add(`${prefix}animated`, animationName);

            // When the animation ends, we clean the classes and resolve the Promise
            function handleAnimationEnd(event) {
            event.stopPropagation();
            node.classList.remove(`${prefix}animated`, animationName);
            resolve('Animation ended');
            }

            node.addEventListener('animationend', handleAnimationEnd, {once: true});
    });
});

