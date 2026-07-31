import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for absolute image paths
    img_matches = re.findall(r'src="/browsing_files/[^"]+"', html)
    # Check for absolute js paths
    js_matches = re.findall(r'href="/browsing_files/[^"]+"', html)
    js_src_matches = re.findall(r'src="/browsing_files/[^"]+"', html)
    
    # Check for lovable domain references for JS files
    lovable_matches = re.findall(r'href="https://im-home[^"]+\.lovable\.app[^"]*browsing-DZFZGdyN\.js"', html)
    lovable_other_js = re.findall(r'href="https://im-home[^"]+\.lovable\.app[^\"]*\.js\"', html)
    
    if img_matches or js_matches or js_src_matches or lovable_other_js:
        print(f'File: {file}')
        if img_matches: print(f'  Absolute imgs: {len(img_matches)}')
        if js_matches: print(f'  Absolute js href: {len(js_matches)}')
        if js_src_matches: print(f'  Absolute js src: {len(js_src_matches)}')
        if lovable_other_js: print(f'  Lovable JS ref: {len(lovable_other_js)} -> {lovable_other_js}')
