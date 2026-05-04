import json
import os
import sys

# 通用 CSS 樣式 (與產生器脫鉤，方便未來統一修改)
CSS_STYLE = """  :root {
    --orange: #FF8C00;
    --yellow: #FFD700;
    --light:  #FFF8EC;
    --text:   #333;
    --muted:  #888;
    --green:  #4CAF50;
    --radius: 18px;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: var(--light);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  header {
    background: linear-gradient(135deg, var(--orange), var(--yellow));
    color: white;
    padding: 16px 24px 14px;
    text-align: center;
  }
  header .unit-label { font-size: 12px; letter-spacing: 2px; opacity: .8; }
  header h1 { font-size: 1.7rem; font-weight: 900; margin-top: 4px; }
  .home-btn {
    position: absolute; top: 14px; left: 14px;
    background: rgba(255,255,255,.25);
    border: none; border-radius: 10px;
    color: white; font-size: 13px; font-weight: 700;
    padding: 6px 12px; cursor: pointer; text-decoration: none;
    display: inline-block;
  }
  .step-nav {
    display: flex; background: white;
    border-bottom: 3px solid #FFE0A0;
    overflow-x: auto; scrollbar-width: none;
  }
  .step-nav::-webkit-scrollbar { display: none; }
  .step-btn {
    flex: 1; min-width: 70px;
    padding: 10px 6px 8px;
    border: none; background: none; cursor: pointer;
    font-size: 12px; font-weight: 700; color: var(--muted);
    display: flex; flex-direction: column; align-items: center; gap: 3px;
    border-bottom: 4px solid transparent; transition: all .2s;
  }
  .step-btn .si { font-size: 1.3rem; }
  .step-btn.active { color: var(--orange); border-bottom-color: var(--orange); background: #FFF8EC; }
  .page { display: none; flex: 1; padding: 18px 16px 90px; max-width: 700px; margin: 0 auto; width: 100%; }
  .page.active { display: block; }
  .page-title { font-size: 1.4rem; font-weight: 900; color: var(--orange); margin-bottom: 4px; display: flex; align-items: center; gap: 8px; }
  .page-sub { font-size: 13px; color: var(--muted); margin-bottom: 18px; }
  .video-btn-wrap { text-align: center; margin-bottom: 16px; }
  .video-btn {
    display: inline-flex; align-items: center; gap: 10px;
    background: #FF0000; color: white;
    border: none; border-radius: var(--radius);
    padding: 16px 28px; font-size: 1.1rem; font-weight: 800;
    cursor: pointer; text-decoration: none;
    box-shadow: 0 4px 14px rgba(255,0,0,.3);
    transition: transform .15s, box-shadow .15s;
  }
  .video-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(255,0,0,.35); }
  .video-btn .yt-icon { font-size: 1.5rem; }
  .task-card {
    background: white; border-radius: var(--radius);
    padding: 16px 20px; box-shadow: 0 2px 8px rgba(0,0,0,.07);
    border-left: 5px solid var(--orange); font-size: 15px; line-height: 1.8;
  }
  .task-card strong { color: var(--orange); }
  .vocab-section-label {
    font-size: 13px; font-weight: 800; letter-spacing: 1px;
    margin: 16px 0 8px; color: #555; text-transform: uppercase;
  }
  .vocab-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 10px; margin-bottom: 6px;
  }
  .vocab-card { height: 95px; perspective: 600px; cursor: pointer; }
  .vocab-inner {
    width: 100%; height: 100%;
    transform-style: preserve-3d; transition: transform .45s ease;
    border-radius: var(--radius); position: relative;
  }
  .vocab-card.flipped .vocab-inner { transform: rotateY(180deg); }
  .vocab-front, .vocab-back {
    position: absolute; width: 100%; height: 100%;
    border-radius: var(--radius);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    backface-visibility: hidden; -webkit-backface-visibility: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
  }
  .vocab-front { background: white; border: 3px solid #FFD180; }
  .vocab-front.ext { border-color: #B2DFDB; }
  .vocab-front .en { font-size: 1.2rem; font-weight: 800; color: var(--orange); }
  .vocab-front.ext .en { color: #00897B; }
  .vocab-front .tap { font-size: 11px; color: var(--muted); margin-top: 3px; }
  .vocab-back { background: linear-gradient(135deg, var(--orange), var(--yellow)); color: white; transform: rotateY(180deg); }
  .vocab-back.ext { background: linear-gradient(135deg, #00897B, #4DB6AC); }
  .vocab-back .zh { font-size: 1.1rem; font-weight: 700; }
  .vocab-back .en2 { font-size: 12px; opacity: .85; margin-top: 2px; }
  .flip-all-btn {
    display: block; margin: 8px auto 16px;
    background: var(--orange); color: white;
    border: none; border-radius: 24px;
    padding: 7px 20px; font-size: 13px; font-weight: 700; cursor: pointer;
  }
  .ext-note { font-size: 12px; color: #00897B; margin-bottom: 14px; }
  .speak-btn {
    background: none; border: none; cursor: pointer;
    font-size: 1rem; padding: 3px 5px; border-radius: 8px;
    transition: background .15s; line-height: 1; flex-shrink: 0;
  }
  .speak-btn:hover { background: rgba(0,0,0,.08); }
  .speak-btn.speaking { animation: spk-pulse .5s infinite alternate; }
  @keyframes spk-pulse { from{opacity:1} to{opacity:.3} }
  .vocab-front .speak-btn { margin-top: 4px; }
  .sentence-speak { float: right; margin-top: -2px; }
  .qa-speak { margin-left: 4px; vertical-align: middle; }
  .game-label { font-weight: 800; font-size: .95rem; margin-bottom: 8px; color: #555; }
  .game-score { text-align: center; font-weight: 800; font-size: .95rem; color: var(--green); margin-bottom: 8px; min-height: 22px; }
  .match-board { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px; }
  .match-col { display: flex; flex-direction: column; gap: 7px; }
  .match-item {
    background: white; border: 3px solid #FFD180; border-radius: 12px;
    padding: 9px 12px; text-align: center; cursor: pointer;
    font-weight: 700; font-size: 14px; transition: all .2s; user-select: none;
  }
  .match-item:hover { border-color: var(--orange); background: #FFF3E0; }
  .match-item.selected { border-color: var(--orange); background: var(--orange); color: white; }
  .match-item.correct { border-color: var(--green); background: #E8F5E9; color: #2E7D32; pointer-events: none; }
  .match-item.wrong { border-color: #f44336; background: #FFEBEE; animation: shake .3s; }
  @keyframes shake { 0%,100%{transform:translateX(0)} 25%{transform:translateX(-5px)} 75%{transform:translateX(5px)} }
  .reset-btn {
    display: block; margin: 0 auto;
    background: #eee; color: #555; border: none; border-radius: 24px;
    padding: 6px 18px; font-size: 13px; font-weight: 700; cursor: pointer;
  }
  .sentence-box {
    background: white; border-radius: var(--radius);
    padding: 16px 20px; margin-bottom: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,.07);
    border-left: 6px solid var(--orange);
  }
  .sentence-box .slabel { font-size: 11px; color: var(--muted); letter-spacing: 1px; margin-bottom: 5px; text-transform: uppercase; }
  .sentence-box .pattern { font-size: 1.15rem; font-weight: 700; }
  .sentence-box .blank {
    display: inline-block; min-width: 75px;
    border-bottom: 3px solid var(--orange); color: var(--orange);
    text-align: center; margin: 0 3px; font-weight: 700;
  }
  .sentence-box .example { margin-top: 7px; font-size: 13px; color: var(--muted); }
  .quiz-progress { text-align: center; font-size: 13px; color: var(--muted); margin-bottom: 10px; }
  .quiz-question {
    background: white; border-radius: var(--radius);
    padding: 18px; text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,.07); margin-bottom: 12px;
  }
  .quiz-q { font-size: .95rem; color: var(--muted); margin-bottom: 6px; }
  .quiz-en { font-size: 1.9rem; font-weight: 900; color: var(--orange); }
  .quiz-choices { display: grid; grid-template-columns: 1fr 1fr; gap: 9px; margin-bottom: 10px; }
  .quiz-btn {
    background: white; border: 3px solid #FFD180; border-radius: 12px;
    padding: 11px; font-size: 1rem; font-weight: 700; cursor: pointer; transition: all .2s;
  }
  .quiz-btn:hover { border-color: var(--orange); background: #FFF3E0; }
  .quiz-btn.correct { border-color: var(--green); background: #E8F5E9; color: #2E7D32; }
  .quiz-btn.wrong   { border-color: #f44336; background: #FFEBEE; }
  .quiz-status { text-align: center; font-weight: 800; font-size: .95rem; min-height: 26px; margin-bottom: 8px; }
  .next-quiz-btn {
    display: none; margin: 0 auto;
    background: var(--orange); color: white;
    border: none; border-radius: 24px;
    padding: 8px 22px; font-size: 14px; font-weight: 700; cursor: pointer;
  }
  .qa-item {
    background: white; border-radius: var(--radius);
    padding: 13px 16px; margin-bottom: 9px;
    box-shadow: 0 2px 8px rgba(0,0,0,.07);
    display: grid; grid-template-columns: 34px 1fr; gap: 10px; align-items: start;
  }
  .qa-num {
    background: var(--orange); color: white; width: 34px; height: 34px;
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 14px; flex-shrink: 0;
  }
  .qa-q { font-weight: 700; font-size: 15px; }
  .qa-a { color: var(--orange); margin-top: 3px; font-size: 14px; }
  .tip-box {
    background: #FFF3E0; border-left: 4px solid var(--orange);
    border-radius: 10px; padding: 11px 14px;
    font-size: 14px; color: #E65100; margin-top: 8px;
  }
  .intro-box {
    background: white; border-radius: var(--radius);
    padding: 22px; box-shadow: 0 2px 8px rgba(0,0,0,.07);
    font-size: 1.1rem; line-height: 2.6; margin-bottom: 14px;
  }
  .intro-box .fill {
    display: inline-block; min-width: 85px;
    border-bottom: 2.5px solid var(--orange); color: var(--orange);
    font-weight: 700; text-align: center;
  }
  .star-tip { text-align: center; font-size: 13px; color: var(--muted); margin-bottom: 18px; }
  .complete-area { text-align: center; margin-top: 24px; }
  .complete-btn {
    background: linear-gradient(135deg, var(--green), #66BB6A);
    color: white; border: none; border-radius: var(--radius);
    padding: 16px 36px; font-size: 1.15rem; font-weight: 900;
    cursor: pointer; box-shadow: 0 4px 14px rgba(76,175,80,.35);
    transition: transform .15s;
  }
  .complete-btn:hover { transform: translateY(-2px); }
  .complete-done {
    display: none; text-align: center; padding: 20px;
    background: white; border-radius: var(--radius);
    box-shadow: 0 2px 8px rgba(0,0,0,.07);
  }
  .complete-done .big { font-size: 3rem; }
  .complete-done h3 { font-size: 1.3rem; font-weight: 900; color: var(--green); margin: 8px 0 4px; }
  .complete-done p { font-size: 14px; color: var(--muted); margin-bottom: 16px; }
  .home-link-btn {
    display: inline-block; background: var(--orange); color: white;
    border: none; border-radius: 24px;
    padding: 10px 28px; font-size: 15px; font-weight: 800;
    cursor: pointer; text-decoration: none;
  }
  .bottom-nav-outer {
    position: fixed; bottom: 0; left: 0; right: 0;
    background: white; border-top: 2px solid #FFE0A0; z-index: 100;
  }
  .bottom-nav {
    display: flex; align-items: center;
    padding: 9px 14px; gap: 9px;
    max-width: 700px; margin: 0 auto;
  }
  .nav-btn {
    flex: 1; padding: 11px; border: none; border-radius: 12px;
    font-size: 14px; font-weight: 800; cursor: pointer; transition: all .2s;
  }
  .nav-prev { background: #F5F5F5; color: #555; }
  .nav-next { background: var(--orange); color: white; }
  .nav-btn:disabled { opacity: .3; pointer-events: none; }
  .nav-step-info { text-align: center; font-size: 13px; color: var(--muted); min-width: 50px; }
"""

def render_pattern(pattern):
    return pattern.replace('<blank>', '<span class="blank">').replace('</blank>', '</span>')

def render_wrapup_line(line):
    return line.replace('<fill>', '<span class="fill">').replace('</fill>', '</span>')

def build_unit(u, template, grade_num, progress_key):
    # Core/ext vocab JS arrays
    core_js = ",\n  ".join(f'{{en:"{v[0]}",zh:"{v[1]}"}}' for v in u["core_vocab"])
    ext_js = ",\n  ".join(f'{{en:"{v[0]}",zh:"{v[1]}"}}' for v in u["ext_vocab"])

    # Prepare Sentences and QA as JSON
    sentences_json = []
    for label, pattern, example, speak_text in u["sentences"]:
        sentences_json.append({
            "label": label,
            "pattern": pattern,
            "example": example,
            "speak_text": speak_text
        })
    
    qa_json = []
    for q, a in u["qa"]:
        qa_json.append({"q": q, "a": a})

    # Wrapup lines
    wrapup_lines_html = "\n    ".join(render_wrapup_line(l) + "<br>" for l in u["wrapup_lines"])

    # Warmup tasks
    warmup_tasks_html = "<br>\n    ".join(u["warmup_tasks"])

    # Wrapup challenge
    wrapup_challenge_html = "<br>\n    ".join(u["wrapup_challenge"])

    # Complete section
    complete_next = u.get("complete_next")
    if complete_next:
        complete_next_text = f"你真棒！下次繼續 {complete_next}"
        home_btn = '<a href="index.html" class="home-link-btn">回首頁 🏠</a>'
    else:
        complete_next_text = "恭喜你完成全部單元！你真的太棒了！🏆"
        home_btn = '<a href="index.html" class="home-link-btn">回首頁查看成果 🏠</a>'

    # Fill template
    html = template
    replacements = {
        "{{num}}": str(u["num"]),
        "{{title}}": u["title"],
        "{{icon}}": u["icon"],
        "{{grade_label}}": u["grade_label"],
        "{{grade_num}}": grade_num,
        "{{warmup_sub}}": u["warmup_sub"],
        "{{video_url}}": u["video_url"],
        "{{video_label}}": u["video_label"],
        "{{warmup_tasks_html}}": warmup_tasks_html,
        "{{core_js}}": core_js,
        "{{ext_js}}": ext_js,
        "{{sentences_json}}": json.dumps(sentences_json, ensure_ascii=False),
        "{{qa_json}}": json.dumps(qa_json, ensure_ascii=False),
        "{{tip_box}}": u["tip_box"],
        "{{wrapup_title}}": u["wrapup_title"],
        "{{wrapup_sub}}": u["wrapup_sub"],
        "{{wrapup_lines_html}}": wrapup_lines_html,
        "{{wrapup_tip}}": u["wrapup_tip"],
        "{{wrapup_challenge_html}}": wrapup_challenge_html,
        "{{complete_next_text}}": complete_next_text,
        "{{home_btn}}": home_btn,
        "{{uid}}": u["id"],
        "{{progress_key}}": progress_key,
        "{{CSS}}": CSS_STYLE
    }

    for k, v in replacements.items():
        html = html.replace(k, v)
    
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 build_units.py <grade_id> (e.g. g4, g2, gk)")
        return

    grade_id = sys.argv[1]
    json_path = f"vocab_{grade_id}.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        units = json.load(f)

    with open('templates/unit_template.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Determine grade-specific info
    grade_map = {
        "g4": {"num": "4", "key": "progress_g4", "dir": "g4"},
        "g2": {"num": "2", "key": "progress_g2", "dir": "g2"},
        "gk": {"num": "K", "key": "progress_kinder", "dir": "gk"}
    }
    
    info = grade_map.get(grade_id, {"num": "?", "key": f"progress_{grade_id}", "dir": grade_id})
    out_dir = info["dir"]
    os.makedirs(out_dir, exist_ok=True)

    for u in units:
        html = build_unit(u, template, info["num"], info["key"])
        path = os.path.join(out_dir, f"{u['id']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
