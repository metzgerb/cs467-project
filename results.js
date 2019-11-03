module.exports = function(){
    var express = require('express');
    var router = express.Router();

    router.get('/', function(req, res){
        r = {};
        r.search_type = '';
        
        res.render('results', r);

    });



    return router;

}();