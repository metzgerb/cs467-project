module.exports = function () {
    var express = require('express');
    var router = express.Router();


    router.get('/', function (req, res) {

        history = {};
        history.result = [];

        if (req.session.search) {
            for (var i = 0; i < req.session.search.length; i++) {
                history.result[i] = {};
                history.result[i].date = req.session.search[i].date;
                history.result[i].link = req.session.search[i].link;
                history.result[i].search_type = req.session.search[i].search_type;
                history.result[i].keyword = req.session.search[i].keyword;
                history.result[i].max = req.session.search[i].max;
            }
        }
    
        res.render("history", history);

    });

    return router;

}();