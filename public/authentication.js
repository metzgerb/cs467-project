$(document).ready(function(){
    $("#new").click(function(){
        $(".new-user").show();
        $(".returning-user").hide();
        console.log("new");


    });

    $("#returning").click(function(){
        console.log("returning");

        $(".returning-user").show();
        $(".new-user").hide();


    });

    // $("#signup").submit(function(event){
    //     event.preventDefault();
        
    //     if($(".password").val() == $(".confirm").val()){
    //         // $.ajax({
    //         //     url : '/signup',
    //         //     type : 'POST',
    //         //     data : {
    //         //         'username': $("#new-username").val(),
    //         //         'password': $("#new-password").val()
    //         //     },
    //         //     success : function(results) {              
    //         //         window.location.replace("/search");
    //         //     },
    //         //     error : function(request,error)
    //         //     {
    //         //         console.log(error, request);
    //         //     }
    //         // });
    //     }
    //     else{
    //         $(".pw-nonmatch").html("<p>Passwords do not match!</p>");
    //     }
    // });


    // $("#login").submit(function(event){
    //     event.preventDefault();
        
    //     console.log($("#username").val(), $("#password").val())
    //     if($(".password").val() == $(".confirm").val()){
    //         // $.ajax({
    //         //     url : '/login',
    //         //     type : 'POST',
    //         //     data : {
    //         //         'username': $("#username").val(),
    //         //         'password': $("#password").val()
    //         //     },
    //         //     success : function(results) {              
    //         //         window.location.replace("/search");
    //         //     },
    //         //     error : function(request,error)
    //         //     {
    //         //         console.log(error, request);
    //         //     }
    //         // });
    //     }
    //     else{
    //         alert("passwords do not match");
    //     }
    // });

});