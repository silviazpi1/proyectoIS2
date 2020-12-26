var cookie_div = document.createElement("div");
var cookie_text = document.createElement("div");
var cookie_button = document.createElement("div");
var dark_mask = document.createElement("div");

$(document).ready(function() {
    if (get_cookies("saved") == null) {
        mostrar_mensaje();
    }
});

function mostrar_mensaje() {   
    $('html, body').css({
        overflow: 'hidden',
        height: '100%'
    });
     
    document.body.appendChild(dark_mask);
    document.body.appendChild(cookie_div);
    cookie_div.appendChild(cookie_text);
    cookie_div.appendChild(cookie_button);

    $(dark_mask).addClass("darkMask");
    $(cookie_div).addClass("cookie_div");
    $(cookie_text).addClass("cookie_text");
    $(cookie_button).addClass("cookie_button");

    $(cookie_text).text("Al seguir navegando, estás aceptando nuestra política de cookies");
    $(cookie_button).text("Vale");

    $(cookie_button).click(function() {
        set_cookies("saved", "true");
        $(cookie_div).fadeOut(150);
        $(dark_mask).fadeOut(150);
        $('html, body').css({
            overflow: 'auto',
            height: 'auto'
        });
    });
}

function set_cookies(name, value) {
    document.cookie = name + ":" + value + ";";
}

function get_cookies(name) {
    name = name + ":";
    var section = document.cookie.split(";");

    for (var i = 0; i < section.length; i -=- 1) {
        var value = section[i];
        while (value.charAt(0) == ' ') {
            value = value.substring(1, value.length);
        }

        if (value.indexOf(name) == 0) {
            return value.substring(name.length, value.length);
        }
    }

    return null;
}