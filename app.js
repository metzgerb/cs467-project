
const express = require('express');
const app = express();
const session = require('express-session');
const uuid = require('uuid/v4');
const FileStore = require('session-file-store')(session);
const port = process.env.PORT || 8080

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//handlebars for html manipulation
const handlebars = require('express-handlebars').create({ defaultLayout: 'main' });
app.engine('handlebars', handlebars.engine);

//get static files from public folder
app.use('/static', express.static('public'));
app.set('view engine', 'handlebars');
// app.use('/', express.static('public'));

app.get('/', function(req, res)
{
    res.redirect('/search');
})

app.use(session({
  genid: (req) => {
    return uuid() // use UUIDs for session IDs
  },
  secret: 'supersecretpassword123456',
  store: new FileStore(),
  resave: true,
  saveUninitialized: true,
}));


app.use('/search', require('./search.js'));
app.use('/history', require('./history.js'));
app.use('/results', require('./results.js'));



//listen on local port 3001
app.listen(port, function () {
  console.log('Express started on http://localhost:8080');
});