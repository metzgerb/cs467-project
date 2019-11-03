module.exports = function(){
    var express = require('express');
    var router = express.Router();


    router.post('/', function(req, res){
        r = {};
        var username = req.body.username;
        var pw = req.body.password;
        console.log(username, pw);
        
        res.redirect('/search');
    });

    

    return router;

}();