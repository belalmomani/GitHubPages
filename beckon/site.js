(function(){
var d=document.documentElement,q=new URLSearchParams(location.search).get('lang'),s=null;
try{s=localStorage.getItem('lang')}catch(e){}
var l=(q==='en'||q==='ar')?q:(s||'ar');
function set(x){d.lang=x;d.dir=x==='ar'?'rtl':'ltr';try{localStorage.setItem('lang',x)}catch(e){}
var b=document.getElementById('lang');if(b)b.textContent=x==='ar'?'English':'العربية';}
set(l);
document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('lang');set(d.lang);
if(b)b.addEventListener('click',function(){set(d.lang==='ar'?'en':'ar')});});
})();