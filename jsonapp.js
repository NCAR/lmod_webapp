//Thomas Johnson III
//jsonapp.js
//Reference: https://www.javatpoint.com/external-javascript-file

function jsonretrieval(tree_content)
{
    var treeJSON = tree_content; //receives the json tree content, saves it to the variable treeJSON
    var treeData = JSON.parse(treeJSON);//parses the JSON stored in treeJSON and saves data to treeData
    document.getElementById('displayjson').innerHTML = treeData;
}

var jsonTreeData = jsonretrieval(tree_content)

function jsonuse(jsonTreeData)
{

}
var headings =[]
var content =[]
function separate_headings_and_lists(treeData)
{
  var headings =treeData[0]
  treeData.shift()
  var content = treeData
}
