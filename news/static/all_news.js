var nbOptions = 3;
// var angleStart = -360;
var angleStart = -360;
// jquery rotate animation
function rotate(li, d) {
    $({ d: angleStart }).animate({ d: d }, {
        step: function (now) {
            $(li)
                .css({ transform: 'rotate(' + now + 'deg)' })
                .find('label')
                .css({ transform: 'rotate(' + (-now) + 'deg)' });
        }, duration: 0
    });
}
// show / hide the options
function toggleOptions(s) {
    $(s).toggleClass('open');
    var li = $(s).find('li');
    var deg = $(s).hasClass('half') ? 180 / (li.length - 1) : 360 / li.length;
    for (var i = 0; i < li.length; i++) {
        var d = $(s).hasClass('half') ? (i * deg) - 90 : i * deg;
        $(s).hasClass('open') ? rotate(li[i], d) : rotate(li[i], angleStart);
    }
}

$('.selectors button').click(function (e) {
    toggleOptions($(this).parent());
});

// setTimeout(function() { toggleOptions('.selector'); }, 100);//@ sourceURL=pen.js



    $(document).ready(function(){
    $(".owl-carousel").owlCarousel();
});

$('.owl-one').owlCarousel({
    loop:true,
    responsiveClass:true,
    responsive:{
    0:{
        items:1,
        nav:true
    },
    600:{
        items:1,
        nav:false
    },
    1000:{
        items:4,
        nav:true,
        loop:true,
        pagination:false,
        autoplay:true,
        autoplayTimeout:4000,
navText : ['<i class="fa fa-2x fa-inverse fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-2x fa-inverse fa-angle-right" aria-hidden="true"></i>']
    }
    }
})

$('.owl-two').owlCarousel({
    loop:true,
    margin:0,
    responsiveClass:true,
    responsive:{
    0:{
        items:1,
        nav:true
    },
    600:{
        items:1,
        nav:false
    },
    1000:{
        items:1,
        nav:true,
        loop:true,
        pagination:false,
        autoplay:false,
autoplayTimeout:4000,
navText : ['<i class="fa fa-2x fa-inverse fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-2x fa-inverse fa-angle-right" aria-hidden="true"></i>']
    }
    }
})
