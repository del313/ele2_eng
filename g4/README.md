# 小四英文課程 — 製作成果

> 純 HTML 單檔課程，雙擊即可在 Chrome / Edge 開啟，不需要伺服器。

---

## 檔案總覽（16 個 HTML）

| 檔案 | 類型 | 主題 | 大小 |
|------|------|------|------|
| `index.html` | 首頁 | 課程地圖 + 進度追蹤 | 13 KB |
| `unit1.html` | 單元 1 | Hello, I'm Me!（自我介紹）| 27 KB |
| `unit2.html` | 單元 2 | My Family（家庭成員）| 27 KB |
| `unit3.html` | 單元 3 | School Days（學校文具）| 26 KB |
| `unit4.html` | 單元 4 | I Love Food（食物飲料）| 26 KB |
| `game1.html` | 關卡 1 | 單字大富翁（Unit 1–4）| 20 KB |
| `unit5.html` | 單元 5 | Animals Are Cool（動物）| 27 KB |
| `unit6.html` | 單元 6 | My Day（時間作息）| 27 KB |
| `unit7.html` | 單元 7 | Colors & Clothes（顏色衣物）| 27 KB |
| `unit8.html` | 單元 8 | How's the Weather?（天氣季節）| 27 KB |
| `game2.html` | 關卡 2 | 打地鼠（Unit 5–8）| 15 KB |
| `unit9.html` | 單元 9 | I Can Do It!（能力嗜好）| 26 KB |
| `unit10.html` | 單元 10 | In the City（城市場所）| 27 KB |
| `unit11.html` | 單元 11 | My Body（身體部位）| 27 KB |
| `unit12.html` | 單元 12 | Show & Tell（綜合發表）| 27 KB |
| `game3.html` | 關卡 3 | 句子拼圖（Unit 9–12）| 18 KB |

---

## 各單元結構（每期約 30 分鐘）

每個單元分 5 頁：

| 頁 | 內容 |
|----|------|
| 1 暖身 | YouTube 影片連結（開新分頁）+ 任務說明 |
| 2 單字 | 翻牌卡（8 核心 + 4 延伸）+ 配對遊戲 |
| 3 句型 | 3 組句型示範 + 選擇題測驗 |
| 4 練習 | Q&A 問答接力卡 |
| 5 收尾 | 造句挑戰 + 完成按鈕（寫入進度）|

---

## 三個關卡遊戲

### game1.html — 單字大富翁（Unit 1–4）
- 雙人（小孩 vs 家長），骰子推進
- 落格出題：看中文選英文（四選一）
- 答錯退 1 格，⭐ 格前進 2 格，💀 格退 2 格
- 先到終點（第 21 格）獲勝

### game2.html — 打地鼠（Unit 5–8）
- 60 秒倒數計時
- 地鼠冒出顯示中文，下方選英文單字
- Combo 連擊加乘得分（最高 x8）
- 難度隨分數漸增（地鼠出現間隔縮短）

### game3.html — 句子拼圖（Unit 9–12）
- 共 10 關，每關一句英文
- 中文提示 + 打亂單字磁貼
- 支援點擊或拖曳排列
- 答對得 10 分；答錯顯示正確答案後繼續

---

## 技術規格

- **純 HTML 單檔**：內嵌 CSS + Vanilla JS，無外部依賴
- **進度儲存**：`localStorage`（key: `progress`，JSON 格式）
  - 進入單元寫入 `in_progress`，完成寫入 `done`
  - 關閉瀏覽器後進度保留
- **順序解鎖**：Unit N 完成後才能進 Unit N+1；Game 需對應 4 單元全完成
- **bfcache 修正**：`pageshow` 事件偵測返回，自動 reload index
- **建議瀏覽器**：Chrome / Edge（Firefox 在 `file://` 下 localStorage 有限制）
- **重設進度**：index.html 右上角「🔄 重設進度」按鈕

---

## 詞彙來源

每單元核心詞彙 8 個 + 延伸詞彙 4 個，依主題整理：

| 單元 | 核心詞彙（8 個）|
|------|----------------|
| 1 | name, old, grade, favorite, color, food, friend, hello |
| 2 | father, mother, brother, sister, grandfather, grandmother, family, baby |
| 3 | pencil, eraser, ruler, book, bag, desk, chair, classroom |
| 4 | rice, noodle, bread, apple, milk, water, egg, chicken |
| 5 | dog, cat, bird, fish, rabbit, tiger, elephant, monkey |
| 6 | morning, noon, afternoon, night, eat, sleep, study, play |
| 7 | red, blue, green, yellow, shirt, pants, shoes, hat |
| 8 | sunny, cloudy, rainy, windy, hot, cold, spring, winter |
| 9 | run, swim, sing, dance, draw, read, cook, ride |
| 10 | school, park, hospital, store, library, bus, car, road |
| 11 | head, eyes, ears, nose, mouth, hands, legs, feet |
| 12 | happy, sad, big, small, fast, slow, pretty, strong |

---

## 影片連結（已驗證可播放）

| 單元 | 影片 | YouTube ID |
|------|------|-----------|
| 1 | Hello Song – Super Simple Songs | `nPvMnGSQ3aI` |
| 2 | The Family Song – Super Simple Songs | `1THpFoxzAsI` |
| 3 | Do You Have A Crayon? – Super Simple Songs | `dbklZrO5H78` |
| 4 | Do You Like Broccoli Ice Cream? – Super Simple Songs | `frN3nvhIHUk` |
| 5 | Let's Go To The Zoo – Super Simple Songs | `OwRmivbNgQk` |
| 6 | Daily Routine Song – ELF Learning | `oPo77rZW58M` |
| 7 | I See Something Blue – Super Simple Songs | `jYAWf8Y91hA` |
| 8 | How's The Weather? – Super Simple Songs | `KBL5aXSJTlE` |
| 9 | Yes, I Can! – Fun Kids English | `Z0x95qiDKeg` |
| 10 | My Little Neighborhood – Maple Leaf Learning | `A61624xjl_I` |
| 11 | Head Shoulders Knees & Toes – Super Simple Songs | *(原始連結)* |
| 12 | Show and Tell Song – Super Simple Songs | *(原始連結)* |
