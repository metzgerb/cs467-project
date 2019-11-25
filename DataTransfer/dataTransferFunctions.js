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

    var process = spawn('python3', ["./crawl.py", req.body.link, req.body["search-type"], req.body.max]);

    r.tree = '';
    var data = '';
    process.stdout.on('data', function (chunk) {
        data += chunk;
    });
    process.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });
    process.on('exit', function() {
        try {
            console.log(data);
            jsonArray = JSON.parse(data);
        } catch (e) {
            console.error(e);
            r.error = e;
        }
        var root = makeLinkTree(jsonArray);
        if (root === undefined) {
            r.header = "<h2>No JSON data received. This could be due to a robots.txt file disallowing crawlers on that website. (For example, http://www.google.com will block crawlers.)</h2>";
        }
        else {
            let searchType;
            if (req.body["search-type"] === "dfs") {
                searchType = "Depth First Search";
            }
            else {
                searchType = "Breadth First Search";
            }
            r.header = "<h1> Results for your " + searchType + "</h1><h1> Your tree: </h1>";
            r.tree = "<script>" + "var treeData =" + JSON.stringify(root) + ";\nvar moreInfo = Object.keys(treeData)[0];\n passTree(treeData);\n </script >";
        }
        
        res.render("results", r);
    });

};

class Node {
    constructor(link) {
        this.name = link;
        this.children = [];
        this.parent = "";
    }
}



function makeLinkTree(jsonArray) {
    let dict = {};
    let root;

    /*
    for (i = 0; i < jsonArray.length; i++) {
        // Make a map with URL as key and URL object as item
        dict[jsonArray[i].URL] = jsonArray[i];
    }
    */
    jsonArray.forEach(function (urlObject) {
        let newNode;
        if (urlObject.URL in dict) {
            newNode = dict[urlObject.URL];
        }
        else {
            newNode = new Node(urlObject.URL);
            newNode.title = urlObject.Title;
            dict[urlObject.URL] = newNode;
        }
        if (urlObject.Parent === 'null') {
            root = newNode;
        }
        else {
            let parentNode;
            if (!(urlObject.Parent in dict)) {
                parentNode = new Node(urlObject.Parent);
                dict[urlObject.Parent] = parentNode; 
            }
            else {
                parentNode = dict[urlObject.Parent];  
            }
            
            parentNode.children.push(newNode);
            
        }

    });
    
    return root;
}

//the following functions are not currently being used within the crawler, but are saved here in case they will be needed again


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

//This will traverse the tree and print preorder.
function traverseAndWrite(node, r) {

    for (i = 0; i < node.childrenArray.length; i++) {
        r = traverseAndWrite(node.childrenArray[i], r);
    }
    r.tree += "<br>" + node.link;
    return r;
}
