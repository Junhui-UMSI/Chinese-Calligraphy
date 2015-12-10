window.setInterval(function() {
  var gallery =document.getElementsByClassName("cn-images")[0];
  var imgArray= gallery.getElementsByTagName("img");
  var currenturl;
  for (i = 0; i < imgArray.length; i++) {
  if (imgArray[i].style.display=="inline"){
     currenturl=imgArray[i].src;
}
}
 document.getElementById("imageurl").value=currenturl;
 console.log(currenturl);
}, 1000)
