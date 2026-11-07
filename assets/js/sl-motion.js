(function(){var els=document.querySelectorAll('[data-motion]');if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('is-in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target)}})},{threshold:.25});
els.forEach(function(e){io.observe(e)});
document.querySelectorAll('.draw').forEach(function(p){try{var l=Math.ceil(p.getTotalLength());p.style.setProperty('--len',l)}catch(_){}})})();
