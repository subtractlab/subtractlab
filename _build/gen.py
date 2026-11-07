# SubtractLab site generator — 和紙と墨 × φ (2026-11-07)
# python _build/gen.py で index.html / history.html / _layouts/default.html を書き出す。
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
        out.append(f'<text class="svgs pop" x="60" y="{y+4}" font-size="16" style="--dl:{i*0.08:.2f}s">{i+1}</text>'
                   f'<path class="ln draw" d="M84 {y} H{x2}" style="--dl:{i*0.08:.2f}s"/>')
    return "".join(out)


HERO_SVG = ('<svg viewBox="0 0 1000 618" role="img" aria-labelledby="hs-t hs-d" data-motion>'
            '<title id="hs-t">MeaningSpace のしくみ</title>'
            '<desc id="hs-d">会話の記録はそのまま残し、その上に意味の層（結晶）を重ねる。結晶の節は元の行への住所を持つ。問いに近い作法だけが灯り、ファイルの地図は変更の理由を持つ。</desc>'
            '<text class="svgs" x="60" y="66" font-size="20">会話の記録（そのまま残す）</text>'
            '<text class="svgs" x="400" y="66" font-size="20">結晶（意味の層）</text>'
            '<text class="svgs" x="740" y="66" font-size="20">作法と地図</text>'
            + log_lines() +
            '<path class="ln draw" d="M400 150 H600 V468 H400 Z" style="--dl:.9s"/>'
            '<path class="ln2 draw" d="M400 256 H600 M400 362 H600" style="--dl:1.3s"/>'
            '<text class="svgt pop" x="424" y="210" font-size="24" style="--dl:1.5s">決まった</text>'
            '<text class="svgt pop" x="424" y="316" font-size="24" style="--dl:1.7s">覆った</text>'
            '<text class="svgt pop" x="424" y="422" font-size="24" style="--dl:1.9s">未決着</text>'
            '<text class="svgs pop" x="424" y="232" font-size="16" style="--dl:1.6s">住所 L2</text>'
            '<text class="svgs pop" x="424" y="338" font-size="16" style="--dl:1.8s">住所 L5</text>'
            '<text class="svgs pop" x="424" y="444" font-size="16" style="--dl:2.0s">住所 L8</text>'
            '<path class="dash draw" d="M400 203 C350 203 330 154 300 154" style="--dl:2.2s"/>'
            '<path class="dash draw" d="M400 309 C350 309 330 280 302 280" style="--dl:2.35s"/>'
            '<path class="dash draw" d="M400 415 C350 415 330 406 280 406" style="--dl:2.5s"/>'
            '<path class="ln draw" d="M600 230 L782 196" style="--dl:2.7s"/>'
            '<circle class="lamp" cx="820" cy="190" r="34" stroke-width="1.2" style="--dl:3.0s"/>'
            '<text class="svgt pop" x="820" y="258" font-size="21" text-anchor="middle" style="--dl:3.1s">近い作法だけが灯る</text>'
            '<text class="svgs pop" x="868" y="160" font-size="16" style="--dl:3.1s">≥ 0.80</text>'
            '<path class="ln draw" d="M600 400 L752 404" style="--dl:2.8s"/>'
            '<path class="ln2 draw" d="M760 404 L860 384 L812 474 L760 404 M860 384 L904 462 L812 474" style="--dl:3.2s"/>'
            '<circle class="ln pop" cx="760" cy="404" r="7" fill="#faf9f6" style="--dl:3.3s"/>'
            '<circle class="ln pop" cx="860" cy="384" r="7" fill="#faf9f6" style="--dl:3.4s"/>'
            '<circle class="ln pop" cx="812" cy="474" r="7" fill="#faf9f6" style="--dl:3.5s"/>'
            '<circle class="ln pop" cx="904" cy="462" r="7" fill="#faf9f6" style="--dl:3.6s"/>'
            '<text class="svgt pop" x="832" y="530" font-size="21" text-anchor="middle" style="--dl:3.7s">地図と、変更の理由</text>'
            '<text class="svgs pop" x="500" y="596" font-size="20" text-anchor="middle" style="--dl:3.9s">Keep every word. Carry only the meaning.</text>'
            '</svg>')


def mini(kind):
    v = 'viewBox="0 0 324 200" role="img" data-motion'
    if kind == "ground":
        rows = "".join(f'<text class="svgs pop" x="28" y="{40+i*26}" font-size="10" style="--dl:{i*.1:.1f}s">{i+1}</text>'
                       f'<path class="ln draw" d="M48 {36+i*26} H{[260,220,250,200,270,230][i]}" style="--dl:{i*.1:.1f}s"/>' for i in range(6))
        return f'<svg {v} aria-label="行番号つきの会話の記録">{rows}</svg>'
    if kind == "crystal":
        return (f'<svg {v} aria-label="節ごとの決着と住所"><path class="ln draw" d="M60 28 H264 V172 H60 Z"/>'
                '<path class="ln2 draw" d="M60 76 H264 M60 124 H264" style="--dl:.4s"/>'
                '<text class="svgt pop" x="78" y="58" font-size="13" style="--dl:.6s">決まった</text><text class="svgs pop" x="200" y="58" font-size="10" style="--dl:.7s">L12–40</text>'
                '<text class="svgt pop" x="78" y="106" font-size="13" style="--dl:.8s">覆った</text><text class="svgs pop" x="200" y="106" font-size="10" style="--dl:.9s">L41–77</text>'
                '<text class="svgt pop" x="78" y="154" font-size="13" style="--dl:1.0s">未決着</text><text class="svgs pop" x="200" y="154" font-size="10" style="--dl:1.1s">L78–96</text></svg>')
    if kind == "skill":
        dots = "".join(f'<circle class="ln2 pop" cx="{x}" cy="{y}" r="11" style="--dl:{i*.08:.2f}s"/>' for i, (x, y) in enumerate([(70,70),(120,130),(170,60),(230,120),(270,64),(90,150)]))
        return (f'<svg {v} aria-label="閾値を超えた作法だけが灯る">{dots}<path class="dash draw" d="M40 100 H290" style="--dl:.5s"/>'
                '<text class="svgs pop" x="292" y="96" font-size="10" text-anchor="end" style="--dl:.6s">0.80</text>'
                '<circle class="lamp" cx="170" cy="60" r="11" stroke-width="1.2" style="--dl:1.0s"/>'
                '<text class="svgt pop" x="170" y="36" font-size="11" text-anchor="middle" style="--dl:1.2s">題名だけが届く</text></svg>')
    return (f'<svg {v} aria-label="ファイルの地図と理由つきの台帳"><path class="ln2 draw" d="M60 60 L150 40 L120 110 Z M150 40 L210 96 L120 110"/>'
            + "".join(f'<circle class="ln pop" cx="{x}" cy="{y}" r="6" fill="#faf9f6" style="--dl:{.3+i*.1:.1f}s"/>' for i, (x, y) in enumerate([(60,60),(150,40),(120,110),(210,96)]))
            + '<path class="ln draw" d="M40 150 H284" style="--dl:.8s"/><text class="svgt pop" x="40" y="172" font-size="11" style="--dl:1.0s">chg-0007　理由：申し送りに合わせた</text>'
            '<text class="svgs pop" x="40" y="190" font-size="10" style="--dl:1.1s">戻し方（逆向きの差分）つき</text></svg>')


NOTES = [("2026-11-07", "組織は、文脈とデータでできている", "https://note.com/subtractlab/n/n343073a76259"),
         ("2026-06-20", "AI時代、もうちょっと先のはなし", "https://note.com/subtractlab/n/n96fd5d241fce"),
         ("2026-06-12", "Claude Opus 4.8というジャジャ馬。手綱はEffortにあった", "https://note.com/subtractlab/n/n8f06045e2089"),
         ("2026-06-06", "AIの記憶は壊れている", "https://note.com/subtractlab/n/n55dd417277eb")]
REPOS = [("meaningspace", "会話はまるごと残し、意味だけを読み込む意味記憶。"),
         ("ai-native-groupware", "SaaS もデータベースサーバーも立てずに、全員が書き、全員が読む。"),
         ("progress-map", "ファイルの「今」と、理由つきの変更の足跡。git を使わない、AIとの開発のための履歴。"),
         ("threshold-skills", "作法は一覧で持たず、問いに近い時だけ灯らせる。")]


def li(d, title, url, sub=""):
    s = f'<span class="x">{sub}</span>' if sub else ""
    return f'<li><span class="d">{d}</span><span><a href="{url}">{title}</a>{s}</span></li>'


def build_index(hist):
    recent = [e for era in hist for e in era["evs"]][-5:][::-1]
    title = "SubtractLab — 奥田剛司 (Koji Okuda) | MeaningSpace：AIと働くための意味記憶"
    desc = ("SubtractLab は奥田剛司（Koji Okuda）が個人で続ける研究と開発。会話をまるごと残し、その上に意味の層を重ねる "
            "AI ネイティブな意味記憶 MeaningSpace を作っています。 / Solo research by Koji Okuda: MeaningSpace, an AI-native semantic memory.")
    p = [head(title, desc, "https://subtractlab.com/", ld(PERSON, ORG, SITEJ)), header("/"), '<main>']
    p.append('<section class="hero"><div class="wrap"><p class="eyebrow">SubtractLab ／ 奥田剛司（Koji Okuda）</p>'
             '<h1>AIの作業場に、<wbr>人間がお邪魔する。</h1><div class="golden">'
             '<div class="reveal" data-motion>'
             '<p class="lead">足すのではなく、引く。会話の記録はまるごと残し、意味だけを運ぶ。奥田剛司が個人で作る意味記憶 MeaningSpace の研究室です。</p>'
             '<p class="en">The AI’s workspace. The human is the guest. SubtractLab is the solo research identity of Koji Okuda, building MeaningSpace — an AI-native semantic memory.</p></div>'
             '<div class="frame">' + HERO_SVG + '</div></div></div></section>')
    p.append('<section class="wrap"><div class="stats reveal" data-motion>'
             '<div class="stat"><b>4,667</b><span>会話（2023年2月から。ChatGPT 1,567・Claude 3,081 ほか）</span></div>'
             '<div class="stat"><b>34,772</b><span>意味の節（決まった・覆った・未決着）</span></div>'
             '<div class="stat"><b>75</b><span>作法（灯る手順）</span></div></div>'
             '<p class="en" style="margin-top:13px">2026-11-07 時点、手元の MeaningSpace（DuckDB 1ファイル）で数えた値。</p></section>')
    p.append('<section class="wrap beat" id="author"><div class="golden"><div class="reveal" data-motion><div class="mark"><i></i>作っている人</div>'
             '<h2 class="display">奥田剛司</h2><p class="en" style="margin-top:-13px">おくだ こうじ ／ Koji Okuda</p></div>'
             '<div class="reveal" data-motion><p class="lead">SubtractLab を一人で営む開発者。AIと毎日話しながら、AIと一緒に働くための仕組みを、引き算で組み立てています。</p>'
             '<ul class="list"><li><span class="d">2023-02</span><span>AIとの会話を始める。ここからの会話がすべて MeaningSpace に残っている</span></li>'
             '<li><span class="d">2024-09</span><span>Claude と組んで、仕事の自動化を始める</span></li>'
             '<li><span class="d">2025-03</span><span>MeaningSpace を構想。「人間がAIの意味空間に入る」方向へ反転</span></li>'
             '<li><span class="d">2026-06</span><span>SubtractLab として公開を始める</span></li></ul>'
             '<p style="margin-top:21px">MeaningSpace、3Gravity Architecture、QIS の考案者。<a href="/about.html">プロフィール</a>　<a href="https://note.com/subtractlab">note</a>　<a href="https://x.com/subtractlabo">X</a>　<a href="https://www.youtube.com/@SUBTRACTLAB">YouTube</a>　<a href="https://github.com/subtractlab">GitHub</a></p></div></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>常識</div>'
             '<h2 class="display">AIは、足して<br>賢くなる。</h2></div>'
             '<div class="reveal" data-motion><p class="lead">もっと大きなモデル。もっと長い文脈。もっと多くの記憶。AIの進歩は「足すこと」だと信じられています。</p>'
             '<p>だから記憶の仕組みも、要約を積み、メモを増やし、検索の対象を広げる方向へ進んでいます。</p></div></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>ひび</div>'
             '<h2 class="display">覚えるほど、<br>迷う。</h2></div>'
             '<div class="reveal" data-motion><p class="lead">毎日AIと話していると、新しい会話のたびに一から説明し直すことになります。</p>'
             '<ul class="list"><li><span class="d">要約して捨てる</span><span>文脈には収まる。でも、なぜそう決めたかが消える。考えが変わった時に戻る場所がない。</span></li>'
             '<li><span class="d">全部を読み直す</span><span>何も失わない。でも、問いのたびに読む量が膨らみ、時間と上限が消える。</span></li>'
             '<li><span class="d">メモを足し続ける</span><span>どのメモが今も正しく、どれが覆ったのかが分からなくなる。</span></li></ul></div></div></section>')
    cards = [("ground", "土台 — 会話の記録", "会話は行番号つきでまるごと残し、書き換えません。"),
             ("crystal", "結晶 — 意味の層", "会話を節に分け、各節に「決まった・覆った・未決着」と、元の行への住所を付けます。"),
             ("skill", "作法 — 灯る手順", "手順も結晶として置き、問いとの近さが閾値を超えた時だけ題名が届きます。"),
             ("map", "地図 — 今どこ", "ファイルの「今」と、変更ごとの理由と戻し方を、会話の節に結んで持ちます。")]
    cs = "".join(f'<div class="card">{mini(k)}<h3>{t}</h3><p>{d}</p></div>' for k, t, d in cards)
    p.append('<section class="wrap beat" id="meaningspace"><div class="mark"><i></i>反転</div>'
             '<div class="golden"><div><h2 class="display">引くと、<br>意味が残る。</h2>'
             '<p class="lead">言葉はすべて残す。運ぶのは意味だけ。それが MeaningSpace です。</p>'
             '<p>すべてがローカルの DuckDB 1ファイルに入っているので、1本の問い合わせで「意味 → 節 → 元の行 → ファイル → 変えた理由」までたどれます。</p>'
             '<p><a href="/meaningspace.html">MeaningSpace の詳しい説明</a>　<a href="/3gravity.html">3Gravity</a>　<a href="/qis.html">QIS</a></p></div>'
             f'<div class="cards">{cs}</div></div></section>')
    rs = "".join(li("GitHub", n, f"https://github.com/subtractlab/{n}", d) for n, d in REPOS)
    p.append('<section class="wrap beat" id="architectures"><div class="golden"><div><div class="mark"><i></i>公開している設計</div>'
             '<h2>設計は、日付ごと置いておく。</h2><p>アーキテクチャを1つずつリポジトリにして、日付の入った公開記録として置いています。実装は公開していません。</p>'
             '<p><a href="https://github.com/subtractlab">github.com/subtractlab</a></p></div>'
             f'<ul class="list reveal" data-motion>{rs}</ul></div></section>')
    p.append('<section class="wrap beat"><div class="golden"><div><div class="mark"><i></i>完成</div>'
             '<h2 class="display">人は、<br>創造に還る。</h2></div>'
             '<div class="reveal" data-motion><p class="lead">文脈とデータはAIが持つ。運ぶのも整えるのもAI。人間に残るのは、まだ誰も考えていないことを考えること。</p>'
             '<p>この見立ては note に書いています。<a href="https://note.com/subtractlab/n/n343073a76259">組織は、文脈とデータでできている</a></p></div></div></section>')
    ns = "".join(li(d, t, u) for d, t, u in NOTES)
    hs = "".join(li(e["d"], e["t"], "/history.html") for e in recent)
    p.append('<section class="wrap beat" id="writing"><div class="golden">'
             '<div><div class="mark"><i></i>書いたもの・話したこと</div>'
             '<p><a href="https://note.com/subtractlab">note</a>　<a href="https://www.youtube.com/@SUBTRACTLAB">YouTube</a>　<a href="https://x.com/subtractlabo">X</a></p>'
             '<p class="en">AIの相棒イライザ（Claude）との対話を、YouTube でポッドキャストの形で出しています。</p></div>'
             f'<div><ul class="list">{ns}</ul><h3>年表から</h3><ul class="list">{hs}</ul><p style="margin-top:13px"><a href="/history.html">年表をすべて見る</a>　<a href="/tour.html">旧トップ（ビジュアルツアー）</a></p></div>'
             '</div></section>')
    p.append('</main>' + FOOT + JS + '\n</body>\n</html>\n')
    return "".join(p)


def build_history(hist):
    title = "年表 — MeaningSpace 先行実装タイムライン｜SubtractLab（奥田剛司）"
    desc = "MeaningSpace と DPマルチエージェント基盤の各機構について、設計・実装・実証の確定日を記録した先行実装のタイムライン。初版 2026-07-16、更新 2026-11-07。"
    p = [head(title, desc, "https://subtractlab.com/history.html", ld(PERSON, ORG)), header("/history.html"), '<main class="wrap">']
    p.append('<div class="crumb"><a href="/">SubtractLab</a> ／ 年表</div><div class="golden"><div>'
             '<p class="eyebrow">Prior-Art Timeline</p><h1>作った日付は、<br>動かない。</h1>'
             '<p class="lead">MeaningSpace と DPマルチエージェント基盤の各機構について、設計・実装・実証の確定日を記録します。個人開発（開発者1名 + AI）による先行実装のデジタルアンカーです。</p>'
             '<p class="en">初版公開 2026-07-16 (JST)・最終更新 2026-11-07。git のコミット履歴、GitHub Pages の配信記録、検索エンジンのインデックス日時が、記載内容の存在時点を裏付けます。表の版: <a href="/timeline.html">timeline</a></p></div><div>')
    for era in hist:
        p.append(f'<div class="tl-era">{era["era"]}</div><div class="tl">')
        for e in era["evs"]:
            p.append(f'<div class="ev{" major" if e["major"] else ""} reveal" data-motion><div class="d">{e["d"]}</div><p class="t">{e["t"]}</p><p class="b">{e["b"]}</p></div>')
        p.append('</div>')
    p.append('<p class="en" style="margin-top:55px">出典: 各日付は MeaningSpace 内の結晶（作成日時つきの構造化された開発記録）に基づきます。結晶のデータベースは開発者のローカル環境に実在し、本ページの記述はその要約です。</p>')
    p.append('</div></div></main>' + FOOT + JS + '\n</body>\n</html>\n')
    return "".join(p)


if __name__ == "__main__":
    hist = json.load(open(os.path.join(B, "history_data.json"), encoding="utf-8"))
    w("index.html", build_index(hist))
    w("history.html", build_history(hist))
    os.makedirs(os.path.join(SITE, "_layouts"), exist_ok=True)
    w(os.path.join("_layouts", "default.html"), layout())
    print("built")
