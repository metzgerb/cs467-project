module.exports = function () {
    const express = require('express');
    const router = express.Router();
    const passport = require('passport');
    const fs = require('fs');

    // router.post('/', (req, res, next) => {
    //     // console.log('Inside POST /login callback') //1
    //     passport.authenticate('local', (err, user, info) => {
    //     //   console.log('Inside passport.authenticate() callback'); //4
    //     //   console.log(`req.session.passport: ${JSON.stringify(req.session.passport)}`) //5
    //     //   console.log(`req.user: ${JSON.stringify(req.user)}`) //6
    //       req.login(user, (err) => {
    //         if (err)
    //         {
    //           console.log("ERROR");
    //         //   console.log(err);
    //           return res.redirect('/');
    //         }
    //         // console.log('Inside req.login() callback') //8
    //         // console.log(`req.session.passport: ${JSON.stringify(req.session.passport)}`) //9
    //         // console.log(`req.user: ${JSON.stringify(req.user)}`) //10
    //         // return res.send('You were authenticated & logged in!\n');
    //         return res.redirect('/search');
    //       })
    //     })(req, res, next);
    //   });

    router.post('/', function (req, res, next) {

        var authenticated = false;
        username = req.body.username;
        password = req.body.password;

        let rawdata = fs.readFileSync('users.json');
        let users = JSON.parse(rawdata);
        for (var i = 0; i < users.users.length; i++) {

            if (username === users.users[i].username && password === users.users[i].password) {
                authenticated = true;
                if(!req.session.id)
                {
                    req.session.id = users.users[i].id;
                    req.session.name = [{"username": username}];
                }
                break;
                // res.redirect('/search');
            }
        }
        if (authenticated)
        {
            res.redirect('/search');
            
        }
        else{
            res.redirect('/');

        }
        
    });


    return router;

}();