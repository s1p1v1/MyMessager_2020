window.onload = function () {
    /*
     добавляем ajax-обработчик для периодического автообновления
     списка сообщений пользователя
    */
    var url = form.attr("action");
    alert(url);
    let id = setInterval(function () {

        $.ajax({
            url: url,
            type: "POST",
            //dataType: "html",   //expect html to be returned
            success: function (data) {
                $('.messages_list').html(data.result);
            }

        });
    }, 10000);
}
window.unload(function(){ clearTimeout(id) })
