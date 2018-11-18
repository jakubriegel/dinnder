$(document).ready(function(){
    $('.sidenav li a').click(function () {
        $('.sidenav').sidenav('close');
    })

    //Top Button functions
    $(window).scroll(function() {scrollFunction()});

    $('.topButton').click(function(){
        $('html, body').stop().animate({
            scrollTop: $('nav').offset().top
        }, 1000);
    });
});

function scrollFunction() {
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
        $(".topButton").css({'display':"block"});
    } else {
        $(".topButton").css({'display':"none"});
    }
}