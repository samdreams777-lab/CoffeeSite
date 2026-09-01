import sys

content = open('site/wp-content/themes/mugs/js/main.min.js', 'r', encoding='utf-8').read()

# The original broken code:
old = 'TweenMax.to(".blackscreen2",1,{opacity:0,ease:Power1.easeOut,delay:.3,onComplete:s,onCompleteParams:[".blackscreen2"],delay:.5})'

# The fixed code:
new_code = 'TweenMax.to(".blackscreen2",1,{opacity:0,ease:Power1.easeOut,delay:.3,onComplete:function(){var el=document.querySelector(".blackscreen2");if(el&&el.parentNode){el.parentNode.removeChild(el);window.__bs2Removed=!0}}})'

if old in content:
    new_content = content.replace(old, new_code, 1)
    open('site/wp-content/themes/mugs/js/main.min.js', 'w', encoding='utf-8').write(new_content)
    print("PATCH 1: Applied - onComplete callback fixed")
    print(f"Original len: {len(content)}, New len: {len(new_content)}")
else:
    print("ERROR: Target string not found!")
    idx = content.find('blackscreen2')
    if idx >= 0:
        print(f"Context: {repr(content[idx-50:idx+200])}")
    sys.exit(1)

# Now add safety fallback at end of file
safety_fallback = '''if(document.querySelector(".blackscreen2")){var bs2Fb=setInterval(function(){var el=document.querySelector(".blackscreen2");if(el&&el.parentNode&&(el.style.opacity==="0"||parseFloat(getComputedStyle(el).opacity)<0.1)){el.parentNode.removeChild(el);clearInterval(bs2Fb);window.__bs2Removed=!0}},200);setTimeout(function(){var el=document.querySelector(".blackscreen2");if(el&&el.parentNode){el.parentNode.removeChild(el);clearInterval(bs2Fb);window.__bs2Removed=!0}},5000)};'''

content2 = open('site/wp-content/themes/mugs/js/main.min.js', 'r', encoding='utf-8').read()

# Remove trailing semicolon + whitespace, then add ; + fallback
content2_stripped = content2.rstrip().rstrip(';').rstrip()
if not content2_stripped.endswith('}'):
    content2_stripped = content2.rstrip()

new_content2 = content2_stripped + ';' + safety_fallback
open('site/wp-content/themes/mugs/js/main.min.js', 'w', encoding='utf-8').write(new_content2)
print("PATCH 2: Applied - safety fallback added")
print(f"Final len: {len(new_content2)}")
