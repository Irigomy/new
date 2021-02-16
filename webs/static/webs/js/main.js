"use strict";var elem=document.querySelector(".main-carousel"),BASE_URL="http://anugerahmebel.com/";if(elem)var flkty=new Flickity(elem,{prevNextButtons:!1});$(".flickity-page-dots").addClass("container"),document.URL!==BASE_URL&&document.URL!==BASE_URL+"about/"?$("header .menu-top + .menu-top").addClass("nv"):$("header .menu-top + .menu-top").removeClass("nv"),$("#openMenu").on("click",function(){screen.width>1024?($("header").removeClass("stick"),$(".min").css("transform","translateY(0)"),$("header .menu-top + .menu-top").addClass("nv")):($(".menu-mob").toggle(),$("header .menu-top + .menu-top").toggleClass("nv"))}),$("#closeMenu").on("click",function(){$("header").addClass("stick"),$(".min").removeAttr("style"),$("header .menu-top + .menu-top").removeClass("nv")}),$(window).scroll(function(){$(window).scrollTop()>=80?$("header").addClass("min"):$("header").removeClass("min")});var on=0;$(".sh").click(function(e){on++,e.preventDefault(),$(".filter").css("transform","translateX(0)"),on%2==1?$(this).addClass("active"):($(this).removeClass("active"),$(".filter").removeAttr("style"))}),$(".tab-header").click(function(e){e.preventDefault();var t=$(e.currentTarget).data("tab");$(".tab-header").removeClass("active"),$(e.currentTarget).addClass("active"),$(".tab").removeClass("active"),$(".tab[data-tab = "+t+"]").addClass("active")}),$(".show").click();

var product = document.querySelector('.carousel-product');
if(product) {
    var flktyProduct = new Flickity(product, {
        prevNextButtons: false,
        setGallerySize: false
    })
};
