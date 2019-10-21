/* Program Name: testServer.js
 * Description: Used for testing the retrieval and sending of information between UNIX and website
 * Author: Christopher Beall (beallch@oregonstate.edu)
 * Course: CS467 (Fall 2019)
 * Last Modified: 2019-10-21
 */


const dataTransfer = require('./dataTransferFunctions');
var express = require('express');
var app = express();

app.listen(1337, function () {
    console.log('port 1337');
})

app.get('/link', dataTransfer.sendStartingLink);

