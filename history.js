module.exports = function(){
    var express = require('express');
    var router = express.Router();

    router.get('/', function(req, res){
        history = {};
        var date = '1/2/19';
        var starting_page = 'www.oregonstate.edu';
        var type = 'depth';
        history.result = [];
        history.result[0] = {};
        history.result[0].date = date;
        history.result[0].starting_page = starting_page;
        history.result[0].type = type;

        history.result[1] = {};
        history.result[1].date = date;
        history.result[1].starting_page = starting_page;
        history.result[1].type = type;


        history.result[2] = {};
        history.result[2].date = date;
        history.result[2].starting_page = starting_page;
        history.result[2].type = type;
        
        res.render("history", history);

    });

    return router;

}();