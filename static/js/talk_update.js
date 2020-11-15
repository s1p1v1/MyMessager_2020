//window.onload = function () {
    /*
     добавляем ajax-обработчик для периодического автообновления
     контактов пользователя
    */
    setInterval(function () {
        $.ajax({
            url: "/talk/",
            type: "POST",
            //dataType: "html",   //expect html to be returned
            success: function (data) {
                $('.messages_list').html(data.result);
            }
        });
    }, 10000);
    
//}
