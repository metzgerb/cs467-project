/* Program Name: dataTransferFunctions.js
 * Description: These are functions that use node.js to send and retrieve information
 * Author: Christopher Beall (beallch@oregonstate.edu)
 * Course: CS467 (Fall 2019)
 * Last Modified: 2019-10-21
 */

// Function to send starting link from website to Unix program
exports.sendStartingLink = function (req, res) {

    //TODO: work with Brian to directly call the crawler from here

    //temporary code for testing
    var spawn = require("child_process").spawn;

    var process = spawn('python', ["./DataTransfer/createJson.py",
        req.body.link]);
    console.log('before');
    process.stdout.on('data', function (data) {
        jsonArray = JSON.parse(data);
	console.log('beforeTree');
        var root = makeLinkTree(jsonArray);
        res.write(JSON.stringify(jsonArray));
	console.log('beforeRecursion');
        traverseAndWrite(root, res);
        res.end();
    })
}

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
    console.log(jsonArray);
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
    console.log(root);
    console.log(dict);
    return root;
}

//This will traverse the tree and print preorder.
function traverseAndWrite(node, res) {

    for (i = 0; i < node.childrenArray.length; i++) {
        traverseAndWrite(node.childrenArray[i], res);
    }
    res.write(node.link);
}
