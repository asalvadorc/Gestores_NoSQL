import os, sys, re, time
import concurrent.futures
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='ca', target='es')

def translate_safe(text):
    if not text.strip(): return text
    
    # Split text into chunks if it exceeds deep-translator limit (approx 5000 chars)
    # Using 4000 to be safe
    MAX_CHUNK = 4000
    if len(text) > MAX_CHUNK:
        chunks = [text[i:i+MAX_CHUNK] for i in range(0, len(text), MAX_CHUNK)]
        translated_chunks = [translate_safe(c) for c in chunks]
        return "".join(translated_chunks)

    try:
        # Avoid rate limits and short network errors
        for _ in range(3):
            try:
                # deep-translator might not respect whitespace, so strip and add back
                leading = text[:len(text)-len(text.lstrip())]
                trailing = text[len(text.rstrip()):]
                res = translator.translate(text.strip())
                return leading + str(res) + trailing
            except Exception as e:
                print(f"Retrying translation due to: {e}")
                time.sleep(2)
        return text
    except:
        return text

def process_markdown_file(filepath):
    print(f"Translating: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by code blocks
    parts = re.split(r'(```.*?```)', content, flags=re.DOTALL)

    translated_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Code block, keep as is
            translated_parts.append(part)
        else:
            # Text part. Translate paragraph by paragraph
            paragraphs = part.split('\n\n')
            translated_paragraphs = []
            for p in paragraphs:
                if not p.strip():
                    translated_paragraphs.append(p)
                    continue

                # Protect URLs and images: ![alt](url) -> replace with placeholders
                url_pattern = re.compile(r'(!?\[)(.*?)(\]\([^\)]+\))')
                
                links = []
                def link_replacer(match):
                    links.append(match.group(0))
                    return f"__LINK_{len(links)-1}__"
                    
                p_no_links = url_pattern.sub(link_replacer, p)
                
                # Protect inline codes
                inline_codes = []
                def code_replacer(match):
                    inline_codes.append(match.group(0))
                    return f"__CODE_{len(inline_codes)-1}__"
                    
                code_pattern = re.compile(r'(`[^`\n]+`)')
                p_no_code = code_pattern.sub(code_replacer, p_no_links)
                
                # Protect HTML tags <br> etc
                html_tags = []
                def html_tags_replacer(match):
                    html_tags.append(match.group(0))
                    return f"__HTML_{len(html_tags)-1}__"
                    
                html_pattern = re.compile(r'(<[^>]+>)')
                p_clean = html_pattern.sub(html_tags_replacer, p_no_code)

                # Now translate
                trans_p = translate_safe(p_clean)

                # Restore HTML
                for j, tag in enumerate(html_tags):
                    trans_p = trans_p.replace(f"__HTML_{j}__", tag)

                # Restore inline codes
                for j, code in enumerate(inline_codes):
                    trans_p = trans_p.replace(f"__CODE_{j}__", code)
                    
                # Restore and translate links
                for j, link in enumerate(links):
                    m = url_pattern.match(link)
                    if m:
                        pref, ltxt, suff = m.groups()
                        if ltxt.strip():
                            trans_ltxt = translate_safe(ltxt)
                        else:
                            trans_ltxt = ltxt
                        restored_link = pref + trans_ltxt + suff
                        trans_p = trans_p.replace(f"__LINK_{j}__", restored_link)
                    else:
                        trans_p = trans_p.replace(f"__LINK_{j}__", link)
                
                translated_paragraphs.append(trans_p)
                
            translated_parts.append('\n\n'.join(translated_paragraphs))

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(''.join(translated_parts))

def process_dir(directory):
    files_to_process = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                files_to_process.append(os.path.join(root, file))
                
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_markdown_file, files_to_process)

if __name__ == "__main__":
    process_dir('C:/Antigravity/Gestores_NoSQL/docs')
    print("Done translating!")
