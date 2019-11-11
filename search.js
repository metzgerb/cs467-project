const dataTransfer = require('./DataTransfer/dataTransferFunctions');

module.exports = function () {
    var express = require('express');
    var router = express.Router();

    router.get('/', function(req, res){
        results = {};
        results.jsscripts = ["static_search.js"];
        results.styles = ["search.css"];

        res.render("search", results);
    });


    router.post('/', function(req, res){
        r = {};
        var link = req.body.link;
        var search_type = req.body.search_type;
        var max = req.body.max;
        var keyword = req.body.keyword;
        dataTransfer.sendStartingLink(req, res, r);
        
        
    });

    

    return router;

}();