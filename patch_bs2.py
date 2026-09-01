content = open('site/wp-content/themes/mugs/js/main.min.js', 'r', encoding='utf-8').read()

safety = 'if(document.querySelector(".blackscreen2")){var bs2Fb=setInterval(function(){var el=document.querySelector(".blackscreen2");if(el&&el.parentNode&&(el.style.opacity==="0"||parseFloat(getComputedStyle(el).opacity)<0.1)){el.parentNode.removeChild(el);clearInterval(bs2Fb);window.__bs2Removed=!0}},200);setTimeout(function(){var el=document.querySelector(".blackscreen2");if(el&&el.parentNode){el.parentNode.removeChild(el);clearInterval(bs2Fb);window.__bs2Removed=!0}},5000)};'

# Add safety fallback at the end
content = content.rstrip().rstrip(';').rstrip() + ';' + safety

open('site/wp-content/themes/mugs/js/main.min.js', 'w', encoding='utf-8').write(content)
print(f"Safety fallback added. Final size: {len(content)} bytes")
