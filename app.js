//express for routing
var express = require('express');
var app = express();
var port = process.env.PORT || 8080;


var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:true}));

//handlebars for html manipulation
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
app.engine('handlebars', handlebars.engine);

//get static files from public folder
app.use('/static', express.static('public'));
app.set('view engine', 'handlebars');
app.use('/', express.static('public'));


app.use('/login', require('./login.js'));
app.use('/signup', require('./signup'));
app.use('/search', require('./search.js'));
app.use('/history', require('./history.js'));
app.use('/results', require('./results.js'));

//listen on local port 3001
app.listen(port, function () {
    console.log('Express started on http://localhost:8080');
});
