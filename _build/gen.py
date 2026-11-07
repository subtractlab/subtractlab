# SubtractLab site generator — washi-and-sumi on a golden-ratio grid (2026-11-07, English)
# python _build/gen.py writes index.html / history.html / _layouts/default.html
import os, json, html as H
from common import head, header, FOOT, JS, ld, PERSON, ORG, SITEJ, layout

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(SITE, "_build")


def w(name, s):
    with open(os.path.join(SITE, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def log_lines():
    out = []
    for i in range(10):
        y = 112 + i * 42
        x2 = [292, 250, 280, 236, 296, 262, 288, 244, 274, 258][i]
        out.append(f'<text class="svgs pop" x="60" y="{y+5}" font-size="16" style="--dl:{i*0.08:.2f}s">{i+1}</text>'
                   f'<path class="ln draw" d="M84 {y} H{x2}" style="--dl:{i*0.08:.2f}s"/>')
    return "".join(out)


HERO_SVG = ('<svg viewBox="0 0 1000 618" role="img" aria-labelledby="hs-t hs-d" data-motion>'
            '<title id="hs-t">How MeaningSpace works</title>'
            '<desc id="hs-d">Conversation logs are kept whole. A meaning layer of crystals sits on top; every section carries its outcome and the address of the lines it came from. Only skills close to the task light up, and a map of files keeps the reason for every change.</desc>'
            '<text class="svgs" x="60" y="66" font-size="20">Conversation logs (kept whole)</text>'
            '<text class="svgs" x="400" y="66" font-size="20">Crystals (meaning)</text>'
            '<text class="svgs" x="740" y="66" font-size="20">Skills and map</text>'
            + log_lines() +
            '<path class="ln draw" d="M400 150 H600 V468 H400 Z" style="--dl:.9s"/>'
            '<path class="ln2 draw" d="M400 256 H600 M400 362 H600" style="--dl:1.3s"/>'
            '<text class="svgt pop" x="424" y="210" font-size="24" style="--dl:1.5s">decided</text>'
            '<text class="svgt pop" x="424" y="316" font-size="24" style="--dl:1.7s">overturned</text>'
            '<text class="svgt pop" x="424" y="422" font-size="24" style="--dl:1.9s">open</text>'
            '<text class="svgs pop" x="424" y="236" font-size="16" style="--dl:1.6s">address L2</text>'
            '<text class="svgs pop" x="424" y="342" font-size="16" style="--dl:1.8s">address L5</text>'
            '<text class="svgs pop" x="424" y="448" font-size="16" style="--dl:2.0s">address L8</text>'
            '<path class="dash draw" d="M400 203 C350 203 330 154 300 154" style="--dl:2.2s"/>'
            '<path class="dash draw" d="M400 309 C350 309 330 280 302 280" style="--dl:2.35s"/>'
            '<path class="dash draw" d="M400 415 C350 415 330 406 280 406" style="--dl:2.5s"/>'
            '<path class="ln draw" d="M600 230 L782 196" style="--dl:2.7s"/>'
            '<circle class="lamp" cx="820" cy="190" r="34" stroke-width="1.2" style="--dl:3.0s"/>'
            '<text class="svgt pop" x="820" y="262" font-size="21" text-anchor="middle" style="--dl:3.1s">only close skills light up</text>'
            '<text class="svgs pop" x="868" y="160" font-size="16" style="--dl:3.1s">≥ 0.80</text>'
            '<path class="ln draw" d="M600 400 L752 404" style="--dl:2.8s"/>'
            '<path class="ln2 draw" d="M760 404 L860 384 L812 474 L760 404 M860 384 L904 462 L812 474" style="--dl:3.2s"/>'
            '<circle class="ln pop" cx="760" cy="404" r="7" fill="#faf9f6" style="--dl:3.3s"/>'
            '<circle class="ln pop" cx="860" cy="384" r="7" fill="#faf9f6" style="--dl:3.4s"/>'
            '<circle class="ln pop" cx="812" cy="474" r="7" fill="#faf9f6" style="--dl:3.5s"/>'
            '<circle class="ln pop" cx="904" cy="462" r="7" fill="#faf9f6" style="--dl:3.6s"/>'
            '<text class="svgt pop" x="832" y="530" font-size="21" text-anchor="middle" style="--dl:3.7s">a map, with reasons</text>'
            '<text class="svgs pop" x="500" y="596" font-size="20" text-anchor="middle" style="--dl:3.9s">Keep every word. Carry only the meaning.</text>'
            '</svg>')


def mini(kind):
    v = 'viewBox="0 0 324 200" role="img" data-motion'
    if kind == "ground":
        rows = "".join(f'<text class="svgs pop" x="28" y="{40+i*26}" font-size="10" style="--dl:{i*.1:.1f}s">{i+1}</text>'
                       f'<path class="ln draw" d="M48 {36+i*26} H{[260,220,250,200,270,230][i]}" style="--dl:{i*.1:.1f}s"/>' for i in range(6))
        return f'<svg {v} aria-label="Line-numbered conversation logs">{rows}</svg>'
    if kind == "crystal":
        return (f'<svg {v} aria-label="Each section carries an outcome and an address"><path class="ln draw" d="M60 28 H264 V172 H60 Z"/>'
                '<path class="ln2 draw" d="M60 76 H264 M60 124 H264" style="--dl:.4s"/>'
                '<text class="svgt pop" x="78" y="58" font-size="13" style="--dl:.6s">decided</text><text class="svgs pop" x="200" y="58" font-size="10" style="--dl:.7s">L12–40</text>'
                '<text class="svgt pop" x="78" y="106" font-size="13" style="--dl:.8s">overturned</text><text class="svgs pop" x="200" y="106" font-size="10" style="--dl:.9s">L41–77</text>'
                '<text class="svgt pop" x="78" y="154" font-size="13" style="--dl:1.0s">open</text><text class="svgs pop" x="200" y="154" font-size="10" style="--dl:1.1s">L78–96</text></svg>')
    if kind == "skill":
        dots = "".join(f'<circle class="ln2 pop" cx="{x}" cy="{y}" r="11" style="--dl:{i*.08:.2f}s"/>' for i, (x, y) in enumerate([(70,70),(120,130),(170,60),(230,120),(270,64),(90,150)]))
        return (f'<svg {v} aria-label="Only skills above the threshold light up">{dots}<path class="dash draw" d="M40 100 H290" style="--dl:.5s"/>'
                '<text class="svgs pop" x="292" y="96" font-size="10" text-anchor="end" style="--dl:.6s">0.80</text>'
                '<circle class="lamp" cx="170" cy="60" r="11" stroke-width="1.2" style="--dl:1.0s"/>'
                '<text class="svgt pop" x="170" y="36" font-size="11" text-anchor="middle" style="--dl:1.2s">only the title arrives</text></svg>')
    return (f'<svg {v} aria-label="A map of files and a ledger with reasons"><path class="ln2 draw" d="M60 60 L150 40 L120 110 Z M150 40 L210 96 L120 110"/>'
            + "".join(f'<circle class="ln pop" cx="{x}" cy="{y}" r="6" fill="#faf9f6" style="--dl:{.3+i*.1:.1f}s"/>' for i, (x, y) in enumerate([(60,60),(150,40),(120,110),(210,96)]))
            + '<path class="ln draw" d="M40 150 H284" style="--dl:.8s"/><text class="svgt pop" x="40" y="172" font-size="11" style="--dl:1.0s">chg-0007   reason: matched the hand-off note</text>'
            '<text class="svgs pop" x="40" y="190" font-size="10" style="--dl:1.1s">with a reverse patch to undo it</text></svg>')


NOTES = [("2026-11-07", "Organizations are made of context and data", "https://note.com/subtractlab/n/n343073a76259"),
         ("2026-06-20", "A little further ahead in the AI era", "https://note.com/subtractlab/n/n96fd5d241fce"),
         ("2026-06-12", "Claude Opus 4.8, a wild horse — the reins were Effort", "https://note.com/subtractlab/n/n8f06045e2089"),
         ("2026-06-06", "AI memory is broken", "https://note.com/subtractlab/n/n55dd417277eb")]
REPOS = [("meaningspace", "Keep every word of every conversation; load only the meaning — with line-level addresses back to the source."),
         ("ai-native-groupware", "Everyone writes, everyone reads — without a SaaS or a database server."),
         ("progress-map", "Where every file is now, and why it changed. Each edit carries a reason and a reverse patch. No git."),
         ("threshold-skills", "Dozens of AI procedures with no catalog in the prompt. A skill lights up only above a similarity threshold.")]


def li(d, title, url, sub=""):
    s = f'<span class="x">{sub}</span>' if sub else ""
    return f'<li><span class="d">{d}</span><span><a href="{url}">{title}</a>{s}</span></li>'


def build_index(hist):
    recent = [e for era in hist for e in era["evs"]][-5:][::-1]
    title = "SubtractLab — Koji Okuda (奥田剛司) | MeaningSpace: semantic memory for working with AI"
    desc = ("SubtractLab is the solo research of Koji Okuda (奥田剛司). MeaningSpace keeps every conversation whole and puts a meaning layer "
            "on top, so an AI can carry only the meaning into each new session.")
    p = [head(title, desc, "https://subtractlab.com/", ld(PERSON, ORG, SITEJ)), header("/"), '<main>']
    p.append('<section class="hero"><div class="wrap"><p class="eyebrow">SubtractLab / Koji Okuda (奥田剛司)</p>'
             '<h1>The AI’s workspace.<wbr> The human is the guest.</h1><div class="golden">'
             '<div class="reveal" data-motion>'
             '<p class="lead">Subtract, don’t add. Keep every word of every conversation, and carry only the meaning. This is the lab of Koji Okuda, who builds MeaningSpace — a semantic memory for working with AI.</p>'
             '<p class="en">奥田剛司 · Koji Okuda</p></div>'
             '<div class="frame">' + HERO_SVG + '</div></div></div></section>')
    p.append('<section class="wrap"><div class="stats reveal" data-motion>'
             '<div class="stat"><b>4,667</b><span>conversations since February 2023 (ChatGPT 1,567, Claude 3,081 and more)</span></div>'
             '<div class="stat"><b>34,772</b><span>meaning sections (decided, overturned, open)</span></div>'
             '<div class="stat"><b>75</b><span>skills that light up</span></div></div>'
             '<p class="en" style="margin-top:13px">Counted on 2026-11-07 in the local MeaningSpace — a single DuckDB file.</p></section>')
    p.append('<section class="wrap beat" id="author"><div class="golden"><div class="reveal" data-motion><div class="mark"><i></i>The builder</div>'
             '<h2 class="display">Koji Okuda</h2><p class="en" style="margin-top:-13px">奥田剛司 ／ おくだ こうじ</p></div>'
             '<div class="reveal" data-motion><p class="lead">An independent builder running SubtractLab alone. He talks with AI every day, and builds the structures for working with it — by subtraction.</p>'
             '<ul class="list"><li><span class="d">2023-02</span><span>First conversations with AI. Every one since is kept in MeaningSpace</span></li>'
             '<li><span class="d">2024-09</span><span>Starts automating work with Claude</span></li>'
             '<li><span class="d">2025-03</span><span>Conceives MeaningSpace — the human enters the AI’s meaning space</span></li>'
             '<li><span class="d">2026-06</span><span>Starts publishing as SubtractLab</span></li></ul>'
             '<p style="margin-top:21px">Originator of MeaningSpace, 3Gravity Architecture and QIS. <a href="/about.html">About</a>　<a href="https://note.com/subtractlab">note</a>　<a href="https://x.com/subtractlabo">X</a>　<a href="https://www.youtube.com/@SUBTRACTLAB">YouTube</a>　<a href="https://github.com/subtractlab">GitHub</a></p></div></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>The common belief</div>'
             '<h2 class="display">AI gets smarter<br>by adding.</h2></div>'
             '<div class="reveal" data-motion><p class="lead">Bigger models. Longer context. More memory. Progress in AI is assumed to mean adding.</p>'
             '<p>So memory systems keep stacking summaries, adding notes and widening what they search.</p></div></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>The crack</div>'
             '<h2 class="display">The more it remembers,<br>the more it gets lost.</h2></div>'
             '<div class="reveal" data-motion><p class="lead">Work with an AI every day and every new session starts from zero again.</p>'
             '<ul class="list"><li><span class="d">Summarize and discard</span><span>It fits in context — but why a decision was made is gone. When your understanding changes, there is nothing to go back to.</span></li>'
             '<li><span class="d">Reload everything</span><span>Nothing is lost — but every question costs more reading, more time and more of your usage limit.</span></li>'
             '<li><span class="d">Keep adding notes</span><span>Nobody can tell which notes still hold and which were overturned.</span></li></ul></div></div></section>')
    cards = [("ground", "Ground — the logs", "Every conversation is kept whole, line by line, and never rewritten."),
             ("crystal", "Crystals — the meaning", "Each conversation is split into sections, each marked decided, overturned or open, with an address back to its lines."),
             ("skill", "Skills — procedures that light up", "Procedures are crystals too. Only when a task is close enough does a skill’s title arrive."),
             ("map", "Map — where things are", "The present state of every file, and a reason and a reverse patch for every change, tied to the conversation.")]
    cs = "".join(f'<div class="card">{mini(k)}<h3>{t}</h3><p>{d}</p></div>' for k, t, d in cards)
    p.append('<section class="wrap beat" id="meaningspace"><div class="mark"><i></i>The turn</div>'
             '<div class="golden"><div><h2 class="display">Subtract,<br>and meaning remains.</h2>'
             '<p class="lead">Keep every word. Carry only the meaning. That is MeaningSpace.</p>'
             '<p>Everything lives in one local DuckDB file, so a single query walks from meaning to section, to the original line, to a file, to the reason it changed.</p>'
             '<p><a href="/meaningspace.html">MeaningSpace in detail</a>　<a href="/3gravity.html">3Gravity</a>　<a href="/qis.html">QIS</a>　<a href="/architecture.html">Architecture</a></p></div>'
             f'<div class="cards">{cs}</div></div></section>')
    rs = "".join(li("GitHub", n, f"https://github.com/subtractlab/{n}", d) for n, d in REPOS)
    p.append('<section class="wrap beat" id="architectures"><div class="golden"><div><div class="mark"><i></i>Published designs</div>'
             '<h2>Every design, dated.</h2><p>Each architecture is its own repository — a dated public record of the design. Implementations are not published.</p>'
             '<p><a href="https://github.com/subtractlab">github.com/subtractlab</a></p></div>'
             f'<ul class="list reveal" data-motion>{rs}</ul></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>Completion</div>'
             '<h2 class="display">People return<br>to creating.</h2></div>'
             '<div class="reveal" data-motion><p class="lead">The AI holds the context and the data. It carries them and keeps them in order. What is left for people is thinking what no one has thought yet.</p>'
             '<p>The argument is written up on note (in Japanese): <a href="https://note.com/subtractlab/n/n343073a76259">Organizations are made of context and data</a></p></div></div></section>')
    ns = "".join(li(d, t, u, "in Japanese") for d, t, u in NOTES)
    hs = "".join(li(e["d"], e["t"], "/history.html") for e in recent)
    p.append('<section class="wrap beat" id="writing"><div class="golden">'
             '<div><div class="mark"><i></i>Writing and talks</div>'
             '<p><a href="https://note.com/subtractlab">note</a>　<a href="https://www.youtube.com/@SUBTRACTLAB">YouTube</a>　<a href="https://x.com/subtractlabo">X</a></p>'
             '<p class="en">Conversations with Eliza, his AI partner (Claude), published as a podcast on YouTube.</p></div>'
             f'<div><ul class="list">{ns}</ul><h3>From the timeline</h3><ul class="list">{hs}</ul><p style="margin-top:13px"><a href="/history.html">Full timeline</a>　<a href="/tour.html">Visual tour (previous home page)</a></p></div>'
             '</div></section>')
    p.append('</main>' + FOOT + JS + '\n</body>\n</html>\n')
    return "".join(p)


def build_history(hist):
    title = "Timeline — MeaningSpace prior-art record | SubtractLab (Koji Okuda)"
    desc = "Dated record of when each mechanism of MeaningSpace and its DP multi-agent foundation was designed, built and proven. First published 2026-07-16, updated 2026-11-07."
    p = [head(title, desc, "https://subtractlab.com/history.html", ld(PERSON, ORG)), header("/history.html"), '<main class="wrap">']
    p.append('<div class="crumb"><a href="/">SubtractLab</a> / Timeline</div><div class="golden"><div>'
             '<p class="eyebrow">Prior-art timeline</p><h1>The date it was built<br>does not move.</h1>'
             '<p class="lead">The dates on which each mechanism of MeaningSpace and its DP multi-agent foundation was designed, built and proven — a digital anchor for prior work by one builder and an AI.</p>'
             '<p class="en">First published 2026-07-16 (JST), last updated 2026-11-07. The git commit history, GitHub Pages deploy records and search-engine index dates attest to when each entry existed. Table version: <a href="/timeline.html">timeline</a></p></div><div>')
    for era in hist:
        p.append(f'<div class="tl-era">{era["era"]}</div><div class="tl">')
        for e in era["evs"]:
            p.append(f'<div class="ev{" major" if e["major"] else ""} reveal" data-motion><div class="d">{e["d"]}</div><p class="t">{e["t"]}</p><p class="b">{e["b"]}</p></div>')
        p.append('</div>')
    p.append('<p class="en" style="margin-top:55px">Source: each date comes from crystals inside MeaningSpace — structured, timestamped development records. The crystal database exists on the developer’s local machine; this page summarizes it.</p>')
    p.append('</div></div></main>' + FOOT + JS + '\n</body>\n</html>\n')
    return "".join(p)


def build_timeline_md(hist):
    out = ["# MeaningSpace / DP Multi-Agent — Prior-Art Timeline", "",
           "**First published: 2026-07-16 (JST) · Updated 2026-11-07 · SubtractLab (one builder + AI)**", "",
           "The confirmed date of each mechanism's design, implementation and proof. Source: crystals inside MeaningSpace (timestamped, structured development records). The git history of this repository serves as a third-party-verifiable timestamp. Illustrated version: [history.html](https://subtractlab.com/history.html)", ""]
    import re
    for era in hist:
        out += ["## " + era["era"], "| Date | Event |", "|---|---|"]
        for e in era["evs"]:
            b = re.sub(r'<a href="([^"]+)">([^<]+)</a>', r'[\2](\1)', e["b"])
            t = f"**{e['t']}**" if e["major"] else e["t"]
            out.append(f"| {e['d']} | {t} — {b} |")
        out.append("")
    out += ["---", "*Every addition is dated by its commit. Evidence that entries were not altered: git history, GitHub Pages deploy records and search-engine index dates.*", ""]
    return "\n".join(out)


if __name__ == "__main__":
    hist = json.load(open(os.path.join(B, "history_data.json"), encoding="utf-8"))
    w("index.html", build_index(hist))
    w("history.html", build_history(hist))
    w("timeline.md", build_timeline_md(hist))
    os.makedirs(os.path.join(SITE, "_layouts"), exist_ok=True)
    w(os.path.join("_layouts", "default.html"), layout())
    print("built")
