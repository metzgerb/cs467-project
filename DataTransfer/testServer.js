/* Program Name: testServer.js
 * Description: Used for testing the retrieval and sending of information between UNIX and website
 * Author: Christopher Beall (beallch@oregonstate.edu)
 * Course: CS467 (Fall 2019)
 * Last Modified: 2019-10-21
 */
process.on('uncaughtException', UncaughtExceptionHandler);

function UncaughtExceptionHandler(err) {
    console.log("Uncaught Exception Encountered!!");
    console.log("err: ", err);
    console.log("Stack trace: ", err.stack);
    setInterval(function () { }, 1000);
}

const dataTransfer = require('./dataTransferFunctions');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }))



app.listen(1337, function () {
    console.log('port 1337');
})



app.get('/', function (req, res) {
    res.sendFile(__dirname + '/public/test.html');
});

app.post('/', dataTransfer.sendStartingLink);

