const menu=document.getElementById('menu-button');
const nav=document.getElementById('nav');
menu.addEventListener('click',()=>{
  const opened=nav.classList.toggle('open');
  menu.setAttribute('aria-expanded',String(opened));
});
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'){
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded','false');
  }
});
document.getElementById('year').textContent=String(new Date().getFullYear());
