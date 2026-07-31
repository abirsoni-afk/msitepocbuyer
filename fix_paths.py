import re
with open('browsing_files/browsing-DZFZGdyN.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace any `/assets/` or `/browsing_files/` with `./browsing_files/`
new_js = re.sub(r'\"/(assets|browsing_files)/([^\"]+)\"', r'"./browsing_files/\2"', js)
new_js = re.sub(r'\'/(assets|browsing_files)/([^\']+)\'', r'"./browsing_files/\2"', new_js)
new_js = re.sub(r'\`/(assets|browsing_files)/([^\`]+)\`', r'"./browsing_files/\2"', new_js)

if new_js != js:
    with open('browsing_files/browsing-DZFZGdyN.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("Updated browsing-DZFZGdyN.js image paths to use relative './browsing_files/'")
else:
    print("No paths matched in browsing-DZFZGdyN.js")

# Do the same for index-DCeeaYLK.js
with open('browsing_files/index-DCeeaYLK.js', 'r', encoding='utf-8') as f:
    js2 = f.read()

new_js2 = re.sub(r'\"/(assets|browsing_files)/([^\"]+)\"', r'"./browsing_files/\2"', js2)
new_js2 = re.sub(r'\'/(assets|browsing_files)/([^\']+)\'', r'"./browsing_files/\2"', new_js2)
new_js2 = re.sub(r'\`/(assets|browsing_files)/([^\`]+)\`', r'"./browsing_files/\2"', new_js2)

if new_js2 != js2:
    with open('browsing_files/index-DCeeaYLK.js', 'w', encoding='utf-8') as f:
        f.write(new_js2)
    print("Updated index-DCeeaYLK.js image paths to use relative './browsing_files/'")
else:
    print("No paths matched in index-DCeeaYLK.js")

# Now let's fix the HTML files.
import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    changed = False
    
    # Replace `<script type="module" crossorigin src="https://.../browsing-DZFZGdyN.js">`
    # Replace `<link rel="modulepreload" crossorigin href="https://.../browsing-DZFZGdyN.js">`
    # Actually just replace any URL matching lovable app with `./browsing_files/`
    
    new_html = re.sub(r'https://im-home[^\"]+\.lovable\.app[^\"]*(browsing-DZFZGdyN\.js|index-DCeeaYLK\.js)', r'./browsing_files/\1', html)
    # Also replace any other absolute JS paths from lovable app that we might have downloaded
    new_html = re.sub(r'https://im-home[^\"]+\.lovable\.app/assets/([^\"]+)', r'./browsing_files/\1', new_html)

    # Replace absolute `/browsing_files/` in html
    new_html = new_html.replace('"/browsing_files/', '"./browsing_files/')
    
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated HTML file: {file}")
