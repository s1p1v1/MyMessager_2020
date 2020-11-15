window.onload = function () {
    /*
     добавляем ajax-обработчик для периодического автообновления
     контактов пользователя

    alert(window.location.href);
    alert(this.location.pathname.indexOf('/send/') + 1);
    */
    if (this.location.pathname == '/contacts/') {
        let id = setInterval(function() {
            $.ajax({
                url: "/contacts/",
                //type: "POST",
                //dataType: "html",   //expect html to be returned
                success: function (data) {
                    $('.contacts_list').html(data.result);
                }
            });
        }, 10000);
    }
    else if (this.location.pathname.indexOf('/send/') + 1) {

        //var url = form.attr("action");
        var url = this.location.pathname
        //alert(url);
        let id1 = setInterval(function () {
            $.ajax({
                url: url,
                //type: "POST",
                //dataType: "html",   //expect html to be returned
                success: function (data) {
                    $('.messages_list').html(data.result);
                }

            });
        }, 10000);

    }
};
window.onunload(function(){ clearTimeout(id); clearTimeout(id1)})

