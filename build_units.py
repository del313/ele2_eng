import json
import os
import sys

def generate_unit(u, grade_info, template):
    # 準備單字資料
    core_js = ",\n  ".join([f"{{en:'{v[0]}', zh:'{v[1]}'}}" for v in u['core_vocab']])
    ext_js  = ",\n  ".join([f"{{en:'{v[0]}', zh:'{v[1]}'}}" for v in u['ext_vocab']])
    
    # 準備 Warmup 任務 HTML
    warmup_html = "".join([f"<li>{t}</li>" for t in u['warmup_tasks']])
    
    # 準備 Wrapup 挑戰 HTML
    wrapup_html = "".join([f"<li>{t}</li>" for t in u['wrapup_challenge']])
    
    # 準備 Wrapup 句子 HTML
    wrapup_lines_html = "".join([f"<p>{l}</p>" for l in u['wrapup_lines']])

    # 準備句型資料 (JSON)
    sentences_list = []
    for s in u['sentences']:
        sentences_list.append({
            "label": s[0],
            "pattern": s[1],
            "example": s[2],
            "speak_text": s[3]
        })
    
    # 準備問答資料 (JSON)
    qa_list = []
    for item in u['qa']:
        qa_list.append({"q": item[0], "a": item[1]})

    # 替換模板標籤
    html = template
    html = html.replace("{{num}}", str(u['num']))
    html = html.replace("{{title}}", u['title'])
    html = html.replace("{{icon}}", u['icon'])
    html = html.replace("{{grade_label}}", u['grade_label'])
    html = html.replace("{{grade_num}}", str(grade_info['num']))
    html = html.replace("{{uid}}", u['id'])
    html = html.replace("{{progress_key}}", grade_info['key'])
    html = html.replace("{{video_url}}", u['video_url'])
    html = html.replace("{{video_label}}", u['video_label'])
    html = html.replace("{{warmup_sub}}", u['warmup_sub'])
    html = html.replace("{{warmup_tasks_html}}", f"<ul>{warmup_html}</ul>")
    html = html.replace("{{core_js}}", core_js)
    html = html.replace("{{ext_js}}", ext_js)
    html = html.replace("{{sentences_json}}", json.dumps(sentences_list, ensure_ascii=False))
    html = html.replace("{{qa_json}}", json.dumps(qa_list, ensure_ascii=False))
    html = html.replace("{{tip_box}}", u.get('tip_box', ''))
    html = html.replace("{{wrapup_title}}", u['wrapup_title'])
    html = html.replace("{{wrapup_sub}}", u['wrapup_sub'])
    html = html.replace("{{wrapup_lines_html}}", wrapup_lines_html)
    html = html.replace("{{wrapup_tip}}", u['wrapup_tip'])
    html = html.replace("{{wrapup_challenge_html}}", f"<ul>{wrapup_html}</ul>")
    
    # 處理下一個單元按鈕
    next_text = f"下一課：{u['complete_next']}" if u['complete_next'] else "恭喜完成本年級所有課程！"
    html = html.replace("{{complete_next_text}}", next_text)
    
    home_btn = '<a href="index.html" class="home-btn" style="position:static; margin-top:15px; background:var(--orange)">🏠 返回課程列表</a>'
    html = html.replace("{{home_btn}}", home_btn)

    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_units.py <grade>  (e.g., g2, g4, gk)")
        return

    grade = sys.argv[1]
    
    # 設定對應的 JSON 與資料夾
    config = {
        "g2": {"json": "vocab_g2.json", "dir": "g2", "num": 2, "key": "progress_g2"},
        "g4": {"json": "vocab_g4.json", "dir": "g4", "num": 4, "key": "progress_g4"},
        "gk": {"json": "vocab_gk.json", "dir": "gk", "num": "K", "key": "progress_kinder"}
    }

    if grade not in config:
        print(f"Error: Unknown grade '{grade}'")
        return

    info = config[grade]
    
    # 載入單元資料
    with open(info["json"], "r", encoding="utf-8") as f:
        units = json.load(f)

    # 載入模板
    with open("templates/unit_template.html", "r", encoding="utf-8") as f:
        template = f.read()

    # 確保輸出目錄存在
    out_dir = info["dir"]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # 產生每個單元的 HTML
    for u in units:
        html = generate_unit(u, info, template)
        path = os.path.join(out_dir, f"{u['id']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {path}")

if __name__ == "__main__":
    main()
