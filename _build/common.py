# SubtractLab site — 和紙と墨 × φ (2026-11-07)
# 共通の頭・案内・帰属を1か所に持つ。gen.py が index.html / history.html / _layouts/default.html を書き出す。
import json, html as H

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Noto+Sans+JP:wght@400;500&display=swap" rel="stylesheet">')

PERSON = {"@context": "https://schema.org", "@type": "Person", "@id": "https://subtractlab.com/#koji-okuda",
          "name": "Koji Okuda", "alternateName": ["奥田剛司", "おくだ こうじ"], "url": "https://subtractlab.com/about.html",
          "jobTitle": "Independent builder / SubtractLab",
          "knowsAbout": ["AI-native systems", "semantic memory", "MeaningSpace", "3Gravity Architecture"],
          "sameAs": ["https://note.com/subtractlab", "https://x.com/subtractlabo", "https://www.youtube.com/@SUBTRACTLAB", "https://github.com/subtractlab"]}
ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": "https://subtractlab.com/#subtractlab",
       "name": "SubtractLab", "url": "https://subtractlab.com/", "founder": {"@id": "https://subtractlab.com/#koji-okuda"},
       "sameAs": ["https://github.com/subtractlab", "https://note.com/subtractlab", "https://x.com/subtractlabo", "https://www.youtube.com/@SUBTRACTLAB"]}
SITEJ = {"@context": "https://schema.org", "@type": "WebSite", "@id": "https://subtractlab.com/#website", "name": "SubtractLab",
         "url": "https://subtractlab.com/", "inLanguage": ["en", "ja"], "publisher": {"@id": "https://subtractlab.com/#subtractlab"},
         "author": {"@id": "https://subtractlab.com/#koji-okuda"}}


def ld(*objs):
    return "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False) for o in objs)


NAV = [("/#architectures", "Architectures"), ("/history.html", "Timeline"),
       ("/#writing", "Writing"), ("/about.html", "About")]


def header(cur=""):
    items = "".join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if u == cur else "", t) for u, t in NAV)
    return ('<header class="sl-head"><div class="wrap"><a class="sl-brand" href="/">SubtractLab</a>'
            '<nav class="sl-nav" aria-label="Site">%s</nav></div></header>' % items)


FOOT = ('<footer class="sl-foot"><div class="wrap">'
        '<div class="row"><a href="/meaningspace.html">MeaningSpace</a><a href="/3gravity.html">3Gravity</a><a href="/qis.html">QIS</a>'
        '<a href="/ARCHITECTURE.html">Architecture</a><a href="/products.html">Products</a><a href="/faq.html">FAQ</a>'
        '<a href="/history.html">Timeline</a><a href="/about.html">About</a></div>'
        '<div class="row"><a href="https://note.com/subtractlab">note</a><a href="https://x.com/subtractlabo">X</a>'
        '<a href="https://www.youtube.com/@SUBTRACTLAB">YouTube</a><a href="https://github.com/subtractlab">GitHub</a></div>'
        '<div>Developed by <a href="/about.html">Koji Okuda (奥田剛司)</a> · SubtractLab · © 2024–2026 Koji Okuda / SubtractLab.</div>'
        '</div></footer>')

JS = '<script src="/assets/js/sl-motion.js" defer></script>'


def head(title, desc, canon, extra=""):
    t, d = H.escape(title), H.escape(desc)
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{t}</title>\n<meta name="description" content="{d}">\n'
            '<meta name="author" content="Koji Okuda (奥田剛司)">\n'
            f'<link rel="canonical" href="{canon}">\n'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="SubtractLab">'
            f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{canon}">'
            '<meta name="twitter:card" content="summary"><meta name="twitter:site" content="@subtractlabo">\n'
            + FONTS + '\n<link rel="stylesheet" href="/assets/css/sl.css">\n' + extra + '\n</head>\n<body>\n')


def layout():
    return ("---\n---\n<!DOCTYPE html>\n<html lang=\"{{ page.lang | default: 'en' }}\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n{% seo %}\n"
            "<meta name=\"author\" content=\"Koji Okuda (奥田剛司)\">\n" + FONTS + "\n"
            "<link rel=\"stylesheet\" href=\"/assets/css/sl.css\">\n" + ld(PERSON, ORG) + "\n</head>\n<body>\n"
            + header() + "\n<main class=\"wrap\">\n"
            "<div class=\"crumb\"><a href=\"/\">SubtractLab</a> / {{ page.title | split: ' — ' | first | default: page.name }}</div>\n"
            "<article class=\"article\">\n{{ content }}\n</article>\n</main>\n" + FOOT + "\n" + JS + "\n</body>\n</html>\n")
