// // #1

// document.getElementById('b').placeholder = 'Ededi daxil edin!';
// document.getElementById('c').addEventListener('click', ()=>{
// var x=document.getElementById('b').value
// function prtst(eded){
//     if (eded==2||eded==1){
//         document.getElementById('o').innerText='Prime!'
//     }
//     else{
//         for(var i=2;i<eded;i++){
//             if (eded % i == 0){    
//                 document.getElementById('o').innerText='Not prime!'          
//                 break;
//             }else{
//                 document.getElementById('o').innerText='Prime!'
//             };
//         };
//     };
// };

// prtst(x)

// })


// // #2

// document.getElementById('b').placeholder = '"CUMLENI DAXIL EDIN","HERFI DAXIL EDIN"';
// document.getElementById('c').addEventListener('click', ()=>{
// var word=document.getElementById('b').value.split(',')


// function cnt(wrd){
//     var count=0
//     var p=wrd[0]
//     var x=wrd[1]
//     for(i=0;i<p.length;i++){
//        if(p[i]==x){
//           count+=1          
//        };
//     };

//     return document.getElementById('o').innerText=`${count}`;
// };

// cnt(word)

// })


// // #3

// document.getElementById('b').placeholder = 'Cumlenin uzunlugun daxil edin!';
// var word="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
// document.getElementById('c').addEventListener('click', ()=>{
// var len=parseInt(document.getElementById('b').value)
// function rndm(wrd){
//     var mxd=''
//     for(var i=0;i<len;i++){
//         let random=Math.floor(Math.random() * word.length);
//         mxd+=word[random];
//     }

//     return document.getElementById('o').innerText=`${mxd}`;
// };

// rndm(word)

// })


// // #4

// document.getElementById('b').placeholder = 'Olke adlarin daxil edin , ile';
// document.getElementById('c').addEventListener('click', ()=>{
// var word=document.getElementById('b').value.split(',')


// function mnwrd(wrd){
//     var max=wrd[0].length
//     var maxwrd=wrd[0]
//     for(i=0;i<wrd.length;i++){
//         if(max<wrd[i].length){ 
//             max=wrd[i].length
//             maxwrd=wrd[i]
//         };
//     };


//     return document.getElementById('o').innerText=`${maxwrd}`;
// };

// mnwrd(word)

// })


// // #5

// document.getElementById('b').placeholder = 'Eded daxil edin!';
// document.getElementById('c').addEventListener('click', ()=>{
// var aot=parseInt(document.getElementById('b').value)
// var coin=[25, 10, 5, 2, 1]
// function amountTocoins(amount, coins) {
//     if (amount === 0) {
//         return [];
//     } else {
//         if (amount >= coins[0]) {
//             left = (amount - coins[0]);
//             return [coins[0]].concat(amountTocoins(left, coins));
//         } else {
//             coins.shift();
//             return amountTocoins(amount, coins);
//         }
//     }
// }
// document.getElementById('o').innerText=`${amountTocoins(aot, coin)}`;
// })


// // #6

// document.getElementById('b').placeholder = 'Cumleni yazin!';
// document.getElementById('c').addEventListener('click', ()=>{
// var word=document.getElementById('b').value.split(' ')
// function mnwrd(wrd){
//     var max=wrd[0].length
//     var maxwrd=wrd[0]
//     for(i=0;i<wrd.length;i++){
//         if(max<wrd[i].length){ 
//             max=wrd[i].length
//             maxwrd=wrd[i]
//         };
//     };


//     return document.getElementById('o').innerText=`${maxwrd}`;
// };

// mnwrd(word)

// })

