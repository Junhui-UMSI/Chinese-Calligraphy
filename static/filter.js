function seal(){
  var itemlist =document.getElementsByClassName("seal");
  for (i = 0; i < itemlist.length; i++) {
    if(document.getElementsByName("ckseal")[0].checked){
    itemlist[i].style.display = "block";
}
  else {
  itemlist[i].style.display = "none";
}
}
}

function clerical(){
  var itemlist =document.getElementsByClassName("clerical");
  for (i = 0; i < itemlist.length; i++) {
  if(document.getElementsByName("ckclerical")[0].checked){
      itemlist[i].style.display = "block";
}
  else {
  itemlist[i].style.display = "none";
}
}
}

function cursive(){
  var itemlist =document.getElementsByClassName("cursive");
  for (i = 0; i < itemlist.length; i++) {
  if(document.getElementsByName("ckcursive")[0].checked){
    itemlist[i].style.display = "block";
}
  else {
  itemlist[i].style.display = "none";
}
}
}

function regular(){
  var itemlist =document.getElementsByClassName("regular");
  for (i = 0; i < itemlist.length; i++) {
  if(document.getElementsByName("ckregular")[0].checked){
    itemlist[i].style.display = "block";
}
  else {
  itemlist[i].style.display = "none";
}
}
}

function semicursive(){
  var itemlist =document.getElementsByClassName("semicursive");
  for (i = 0; i < itemlist.length; i++) {
  if(document.getElementsByName("cksemicursive")[0].checked){
    itemlist[i].style.display = "block";
}
  else{
  itemlist[i].style.display = "none";
}
}
}
