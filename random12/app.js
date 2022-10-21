// const prg=document.getElementById("text")


// function js_style(){
//     prg.innerText='Soz deyishdi!'
//     prg.style.color='red'
//     prg.style.fontSize="14pt"
//     prg.style.fontFamily = "Arial"
//     prg.style.backgroundColor='blue'
// }

// const elmt=document.getElementById("tech")

// function getAttributes(){
//     console.log(elmt.getAttribute("id"))
//     console.log(elmt.getAttribute("type"))
//     console.log(elmt.getAttribute("hreflang"))
//     console.log(elmt.getAttribute("rel"))
//     console.log(elmt.getAttribute("target"))
//     console.log(elmt.getAttribute("href"))
// }


// const table=document.getElementById('sampleTable')

// function insert_Row(){
//     table.innerHTML+="<tr><td>Row cell</td> <td>Row cell</td></tr>"
// }


// const drpdwn=document.getElementById('colorSelect')

// function removecolor(){
//     drpdwn.lastChild.remove()
// }



// const table=document.getElementById('myTable')


  
// function createTable(){
//  for(var r=0;r<parseInt(document.getElementById('setir').value);r++)
//   {
//    var x=document.getElementById('myTable').insertRow(r);
//    for(var c=0;c<parseInt(document.getElementById('stun').value);c++)  
//     {
//      var y=  x.insertCell(c);
//      y.innerHTML="Row-"+r+" Column-"+c; 
//     }
//    }
// }

// var array=[
//    "http://farm4.staticflickr.com/3691/11268502654_f28f05966c_m.jpg",
//    "http://farm1.staticflickr.com/33/45336904_1aef569b30_n.jpg",
//    "http://farm6.staticflickr.com/5211/5384592886_80a512e2c9.jpg",
// ]
// function randomimg(){
//     index=Math.floor(Math.random( ) * array.length)
//     var image=array[index]
//     console.log(image)
//     document.getElementById("lst").innerHTML=`<img src="${image}" alt="" width="500px">`
// }