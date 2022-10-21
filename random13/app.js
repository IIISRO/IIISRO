// // #1

//     var l= document.querySelectorAll("li")


//     l.forEach((e)=>{
//         e.addEventListener('click', (event)=>{
//             if(event.target===e && e.className!=='selected'){
//                 if(event.ctrlKey==false){
//                 l.forEach((e)=>{
//                     if(e.className==='selected'){
//                         e.classList.remove('selected')
//                     }
//                 })
//             }
//                 e.classList.add('selected');
//             }
//             else{
//                 e.classList.remove('selected');
//             }
//         })
//     })


// // #2

// const elements=document.querySelectorAll('[data-tooltip]')
// const tip=document.getElementById("tip")
// elements.forEach((e)=>{

// e.onmouseover = function (event) {
//     var w=event.clientX + 'px'
//     var h= event.clientY+ 'px'
//     tip.style.display="block"
//     tip.style.left=w
//     tip.style.top=h
//     tip.innerText=event.target.dataset.tooltip;
// };
  
//   e.onmouseout = function (event) {
//     tip.style.display='none'
//   };
// })


// // #3

// const div= document.getElementById('scrl')

// var i=0

// while (i<6){
//     div.innerHTML+=`<p>${new Date()}</p>`
//     i++
// }

// div.addEventListener('scroll', ()=>{
//     div.innerHTML+=`<p>${new Date()}</p>`
// })


// // #4

// const pr=document.getElementById('pr')
// const btn=document.getElementById('btn')

// pr.addEventListener("scroll",()=>{
//     console.log(pageYOffset)
//    if(pageYOffset <  document.documentElement.clientHeight) {
//        btn.style.display='block'
//    }
// })
// btn.addEventListener('click',()=>{
//     pr.scrollTo(pageYOffset, 0)
// })


// // #5

// let form = document.forms.calculator;
// form.money.oninput = calculate;
// form.months.onchange = calculate;
// form.interest.oninput = calculate;
// function calculate() {
//   let initial = +form.money.value;
//   if (!initial) return;
//   let interest = form.interest.value * 0.01;
//   if (!interest) return;
//   let years = form.months.value / 12;
//   if (!years) return;
//   let result = Math.round(initial * (1 + interest) ** years);
//   let height = result / form.money.value * 100 + 'px';
//   document.getElementById('height-after').style.height = height;
//   document.getElementById('money-before').innerHTML = form.money.value;
//   document.getElementById('money-after').innerHTML = result;
// }
// calculate();