/* Program Name: dataTransferFunctions.js
 * Description: These are functions that use node.js to send and retrieve information
 * Author: Christopher Beall (beallch@oregonstate.edu)
 * Course: CS467 (Fall 2019)
 * Last Modified: 2019-10-21
 */

// Function to send starting link from website to Unix program
exports.sendStartingLink = function (req, res, r) {

    //TODO: work with Brian to directly call the crawler from here

    //temporary code for testing
    var spawn = require("child_process").spawn;

    var process = spawn('python', ["./crawl.py", req.body.link, req.body.search_type, req.body.max]);
    r.tree = '';
    process.stdout.on('data', function (data) {
        jsonArray = JSON.parse(data);

        var root = makeLinkTree(jsonArray);
        r = traverseAndWrite(root, r);
    });
    process.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
    process.on('exit', function () {
        res.render("results", r);
    });
    console.log(r.tree);

};

class Node {
    constructor(link) {
        this.link = link;
        this.childrenArray = [];
        this.parent = null;
    }
}

class Tree {
    constructor(link) {
        var nodeRoot = new Node(link);
        this.root = nodeRoot;
    }

    traverse(node, stack) {
        for (i = 0; i < node.children.length; i++) {
            traverse(node.children[i], stack);
        }
        stack.push(node.link);
    }
}

//Json should be formatted as {"link": "www.ex.com", "children": [{"link": www.ex2.com", "children" : []}]}
function convertJsonToTree(jsonCrawlerString) {
    var jsonCrawler = JSON.parse(jsonString);

    var root = new Node(jsonCrawler.link);
    makeTreeRecursively(root, jsonCrawler);
}

function makeTreeRecursively(node, jsonObj) {

    for (i = 0; i < jsonObj.children.length; i++) {
        var child = new Node(jsonObj.children[i].link);
        node.childrenArray.push(child);
        makeTreeRecursively(child, jsonObj.children[i]);
    }
}

function makeLinkTree(jsonArray) {
    var dict = {};
    var root;

    /*
    for (i = 0; i < jsonArray.length; i++) {
        // Make a map with URL as key and URL object as item
        dict[jsonArray[i].URL] = jsonArray[i];
    }
    */
    jsonArray.forEach(function (urlObject) {
        var newNode;
        if (urlObject.URL in dict) {
            newNode = dict[urlObject.URL];
        }
        else {
            newNode = new Node(urlObject.URL);
            dict[urlObject.URL] = newNode;
        }
        if (urlObject.Parent === 'null') {
            root = newNode;
        }
        else {
            var parentNode;
            if (!(urlObject.Parent in dict)) {
                parentNode = new Node();
                dict[urlObject.Parent] = parentNode;
            }
            else {
                parentNode = dict[urlObject.Parent];
            }
            parentNode.childrenArray.push(newNode);
            newNode.parent = parentNode;
        }

    });
    return root;
}

//This will traverse the tree and print preorder.
function traverseAndWrite(node, r) {

    for (i = 0; i < node.childrenArray.length; i++) {
        r = traverseAndWrite(node.childrenArray[i], r);
    }
    r.tree += "<br />" + node.link;
    return r;
}
