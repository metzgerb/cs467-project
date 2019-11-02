/* Program Name: testServer.js
 * Description: Used for testing the retrieval and sending of information between UNIX and website
 * Author: Christopher Beall (beallch@oregonstate.edu)
 * Course: CS467 (Fall 2019)
 * Last Modified: 2019-10-21
 */

var port = process.env.PORT || 8080

const dataTransfer = require('./DataTransfer/dataTransferFunctions');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }))



app.listen(port, function () {
    console.log('Starting up server');
})



app.get('/', function (req, res) {
    res.sendFile(__dirname + '/public/test.html');
});

app.post('/', dataTransfer.sendStartingLink);

