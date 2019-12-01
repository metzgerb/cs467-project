const dataTransfer = require('./DataTransfer/dataTransferFunctions');

module.exports = function () {
    var express = require('express');
    var router = express.Router();

    router.get('/', function(req, res){
        results = {};
        results.jsscripts = ["static_search.js"];
        results.styles = ["search.css"];

        console.log(req.session.id);
        res.render("search", results);
    });


    router.post('/', function(req, res){
        
        r = {};
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); 
        var yyyy = today.getFullYear();
        today = mm + '/' + dd + '/' + yyyy;

        var link = req.body.link;
        var search_type = req.body.search_type;
        var max = req.body.max;
        var keyword = req.body.keyword;
        
        if(!link || !search_type || !max)
        {
            r.error = "Invalid search...please try again!";
            r.jsscripts = ["static_search.js"];
            r.styles = ["search.css"];
            res.render('search', r);
            return;
        }

        if (keyword){
            for(var i = 0; i < keyword.length; i++)
            {
                if((keyword[i] < 65 || keyword[i] > 122) || ( keyword[i] > 90 && keyword[i] < 97))
                {
                    r.error = "Invalid keyword...please try again!";
                    r.jsscripts = ["static_search.js"];
                    r.styles = ["search.css"];
                    res.render('search', r);
                    return;
                }
            }
        }
        
        
        if(!req.body.search_again){
            var search = req.session.search || [];
            search.push({"date": today, "link": link, "search_type": search_type, "max": max, "keyword": keyword});
            req.session.search = search;
        }
        

        dataTransfer.sendStartingLink(req, res, r);
        
        
    });



    return router;

}();