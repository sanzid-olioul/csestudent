const responsive = {

    0:{
        items:1
    },

    320:{
        items:1
    },

    560:{
        items:2
    },

    960:{
        items:3
    }
}





$(document).ready(function(){

    $nav = $('.nav');
    $togglecollapse = $('.toggle-collapse');

    $togglecollapse.click(function(){
        $nav.toggleClass('collapse');
    })

    //Owl carosel
    $('.owl-carousel').owlCarousel({
        loop: true,
        autoplay: true,
        autopalyTimeout: 3000,
        dots: false,
        nav: true,
       // autoplayHoverPause:true,
        navText: [$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],
        responsive: responsive
    });



    //Move up function

    $('.move-up span').click(function(){

        $('html, body').animate({
            scrollTop: 0
        },2000)
    })

    AOS.init();

})