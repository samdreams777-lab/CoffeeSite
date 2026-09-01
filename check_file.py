content = open('site/wp-content/themes/mugs/js/main.min.js', 'r', encoding='utf-8').read()
print(f'File size: {len(content)}')
has_bs2Fb = 'bs2Fb' in content
has_bs2Removed = '__bs2Removed' in content
print(f'Has bs2Fb: {has_bs2Fb}')
print(f'Has __bs2Removed: {has_bs2Removed}')
end = content[-200:]
print(f'Ends with: {repr(end)}')
