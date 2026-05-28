import json
import os
import sys

def generate_unit(u, grade_info, template):
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
    
    # 處理 GK 特有的 items 欄位
    if 'items' in u:
        html = html.replace("{{items_json}}", json.dumps(u['items'], ensure_ascii=False))
    
    # 處理 G2/G4 特有的 vocab 欄位
    if 'core_vocab' in u:
        core_js = ",\n  ".join([f"{{en:'{v[0]}', zh:'{v[1]}'}}" for v in u['core_vocab']])
        html = html.replace("{{core_js}}", core_js)
    if 'ext_vocab' in u:
        ext_js  = ",\n  ".join([f"{{en:'{v[0]}', zh:'{v[1]}'}}" for v in u['ext_vocab']])
        html = html.replace("{{ext_js}}", ext_js)
    
    # ... (其餘原有的欄位替換，加入防呆判斷)
    if 'warmup_tasks' in u:
        warmup_html = "".join([f"<li>{t}</li>" for t in u['warmup_tasks']])
        html = html.replace("{{warmup_tasks_html}}", f"<ul>{warmup_html}</ul>")
    
    if 'sentences' in u:
        sentences_list = [{"label": s[0], "pattern": s[1], "example": s[2], "speak_text": s[3]} for s in u['sentences']]
        html = html.replace("{{sentences_json}}", json.dumps(sentences_list, ensure_ascii=False))
    
    if 'qa' in u:
        qa_list = [{"q": item[0], "a": item[1]} for item in u['qa']]
        html = html.replace("{{qa_json}}", json.dumps(qa_list, ensure_ascii=False))

    # 處理下一個單元按鈕
    next_text = f"下一課：{u['complete_next']}" if u.get('complete_next') else "恭喜完成本年級所有課程！"
    html = html.replace("{{complete_next_text}}", next_text)
    
    # 補上缺少的模板標籤替換
    html = html.replace("{{warmup_sub}}", u.get('warmup_sub', "10 分鐘 · 唱唱歌，熟悉本課主題"))
    html = html.replace("{{tip_box}}", u.get('tip_box', "💡 試著用剛學到的單字來回答問題吧！"))
    html = html.replace("{{wrapup_title}}", u.get('wrapup_title', "學習收尾"))
    html = html.replace("{{wrapup_sub}}", u.get('wrapup_sub', "5 分鐘 · 複習成果"))
    html = html.replace("{{wrapup_tip}}", u.get('wrapup_tip', "✨ 記得每天練習，進步會更快喔！"))
    
    wrapup_lines = u.get('wrapup_lines', ["今天表現得很好！我們學會了本課的核心單字與句型。"])
    html = html.replace("{{wrapup_lines_html}}", "".join([f"<p>{line}</p>" for line in wrapup_lines]))
    
    wrapup_challenges = u.get('wrapup_challenges', ["嘗試在生活中使用今天學到的單字。"])
    html = html.replace("{{wrapup_challenge_html}}", "<ul>" + "".join([f"<li>{c}</li>" for c in wrapup_challenges]) + "</ul>")

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
        "g2": {"json": "vocab_g2.json", "dir": "g2", "num": 2, "key": "progress_g2", "tpl": "templates/unit_template.html"},
        "g3": {"json": "vocab_g3.json", "dir": "g3", "num": 3, "key": "progress_g3", "tpl": "templates/unit_template.html"},
        "g4": {"json": "vocab_g4.json", "dir": "g4", "num": 4, "key": "progress_g4", "tpl": "templates/unit_template.html"},
        "g5": {"json": "vocab_g5.json", "dir": "g5", "num": 5, "key": "progress_g5", "tpl": "templates/unit_template.html"},
        "g6": {"json": "vocab_g6.json", "dir": "g6", "num": 6, "key": "progress_g6", "tpl": "templates/unit_template.html"},
        "gk": {"json": "vocab_gk.json", "dir": "gk", "num": "K", "key": "progress_kinder", "tpl": "templates/unit_template_gk.html"}
    }

    if grade not in config:
        print(f"Error: Unknown grade '{grade}'")
        return

    info = config[grade]
    
    # 載入單元資料
    with open(info["json"], "r", encoding="utf-8") as f:
        units = json.load(f)

    # 載入模板
    with open(info["tpl"], "r", encoding="utf-8") as f:
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
