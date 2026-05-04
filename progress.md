# 小二英文教材開發進度表 (Grade 2 English Progress)

## 🎯 專案目標
打造具備「強視覺、高互動、低負擔」的小二英文學習網頁。
- **技術平台**: Vanilla JS + Web Speech API
- **進度儲存**: `localStorage` (key: `progress_g2`)

---

## 📅 課程地圖 (Curriculum Map)

| 階段 | 範圍 | 內容 | 解鎖遊戲 | 狀態 |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Unit 1 - 3 | 字母、數字、學校 | Game 1, 2 | ✅ 已完成 |
| **Phase 2** | Unit 4 - 6 | 身體、家庭、心情 | Game 3, 4 | ✅ 已完成 |
| **Phase 3** | Unit 7 - 9 | 色彩、動物、天氣、運動 | Game 5, 6 | ✅ 已完成 |
| **Phase 4** | Unit 10 - 12 | 食物、房屋、公園 | Game 7, 8 | ✅ 已完成 |

### 遊戲清單 (8 Games)
- **Phase 1**: `game1` (Memory), `game2` (Bubble)
- **Phase 2**: `game3` (Monster), `game4` (Path)
- **Phase 3**: `game5` (Scramble), `game6` (Flash)
- **Phase 4**: `game7` (Catcher), `game8` (Final)

---

## 📝 待辦清單 (TODO)

### 🧪 系統驗證 (未檢查項目)
- [ ] **音效相容性檢查**：在 iOS/Android 瀏覽器測試 Web Speech API 是否需手動點擊觸發。
- [ ] **斷點與佈局檢查**：測試在窄螢幕手機上 `vocab-grid` 與 `game-grid` 的顯示是否會跑版。
- [ ] **進度解鎖邏輯測試**：確認完成 Unit 3 是否確實解鎖 Game 1, 2。
- [ ] **影片連結效能**：檢查 YouTube 嵌入/連結在不同網路環境下的載入速度。

### 🏗️ 基礎建設
- [x] 建立通用樣式 `style-common.css`
- [x] 整合入口網頁 `index.html` (串聯幼兒園、小二、小四)
- [x] **網站線上託管**：已透過 GitHub Pages 上線 (https://del313.github.io/ele2_eng/)
| **Phase K** | Unit 1 - 8 | 幼兒啟蒙、顏色、動作 | Game 1 - 8 | ✅ 已完成 |
| **Phase 1** | Unit 1 - 3 | 字母、數字、學校 | Game 1, 2 | ✅ 已完成 |
...
### ✍️ 內容開發
- [x] 完成幼兒園 (Grade K) Unit 1 - 8 與 Game 1 - 8
- [x] 完成小二 (Grade 2) Unit 1 - 12 與 Game 1 - 8
- [x] 完成小四 (Grade 4) Unit 1 - 12 與 Game 1 - 6

---

## 🚀 託管與佈局 (Hosting & Deployment)
- **託管平台**: GitHub Pages
- **部署方式**: GitHub Actions / Branch Deploy (main)
- **子目錄結構**: `/gk/` (幼兒), `/g2/` (小二), `/g4/` (小四), `/` (入口首頁)
- **線上網址**: [https://del313.github.io/ele2_eng/](https://del313.github.io/ele2_eng/)

---

## 🏗️ 多年級整合計畫 (Multi-Grade Integration Plan)

### 1. 目錄結構重構
採用子目錄結構以避免檔案衝突：
- `/` (根目錄)：主入口首頁 `index.html`
- `/gk/`：幼兒園教材檔案
- `/g2/`：存放所有小二英文教材檔案
- `/g4/`：存放所有小四英文教材檔案

### 2. 實作步驟
- [x] **A. 遷移小二教材 (Grade 2)**
  - 建立 `g2/` 資料夾並移入所有 `unit*.html`, `game*.html`, `index.html`, `style-common.css`。
- [x] **B. 遷移小四教材 (Grade 4)**
  - 建立 `g4/` 資料夾並從 `child_eng/` 複製所有教材檔案。
- [x] **C. 整合幼兒園教材 (Grade K)**
  - 建立 `gk/` 資料夾並從 `ls_eng/` 整合教材檔案。
  - 套用通用樣式並重新設計 Unit/Game 流程。
- [x] **D. 建立主入口首頁**
  - 在根目錄建立新的 `index.html`，設計「幼兒園」、「小二」、「小四」三個切換按鈕。
- [x] **E. 驗證測試**
  - 確認各年級連結正確、進度獨立且 GitHub Pages 部署正常。

---
## 📝 後續待辦清單 (Future TODOs)

### 1. 🐣 幼兒園教材開發 (Kindergarten)
- [x] **按鈕樣式與佈局統一**：在 `gk/index.html`、`g2/index.html` 與 `g4/index.html` 統一「重設進度」與「回首頁」的按鈕高度 (40px) 與兩端對齊佈局。
- [x] **遊戲機制全面升級**：已完成 8 種新的平板友善互動遊戲：
    1. **氣球快手 (Balloon Pop)**：氣球飄動點擊。
    2. **對對碰 (Tap the Pair)**：散落卡片配對。
    3. **單字敲敲樂 (Whack-a-Mole)**：**3x3 (9 洞)** 網格快節奏反應。
    4. **影子拼圖 (Silhouette Fill)**：**6 組** 拖曳配對，區域等高優化。
    5. **單字轉盤 (Spin & Match)**：**conic-gradient 重構**，加入旋轉滴答音效。
    6. **字母接接樂 (Letter Catcher)**：順序字母點擊。
    7. **圖片拼拼看 (Jigsaw Puzzle)**：**3x3 (9 格)** 拼圖難度。
    8. **指令大挑戰 (Action Challenge)**：全新 **Simon Says** 記憶玩法。
- [ ] **視覺優化**：確保按鈕寬度一致、對齊與平板互動友善。

### 2. 📱 平台優化 (Platform Optimization)
...

- [ ] **跨裝置相容性測試**：
    - [ ] 測試 iOS Safari 的 Web Speech API 是否能自動播放音效。
    - [ ] 檢查小二/小四遊戲在不同解析度手機上的佈局。
- [ ] **載入速度優化**：檢查較大的 HTML 檔案，考慮將通用 JS/CSS 外部化以減少重複載入。

### 3. ✨ 功能增強 (Feature Requests)
- [ ] **全域進度統計**：在主入口頁面顯示三個年級的總體完成百分比。
- [ ] **音效回饋**：除了語音朗讀，加入「答對 (Success)」與「答錯 (Try Again)」的音效回饋。
- [ ] **離線功能**：研究 Service Worker 技術，讓教材在無網路環境（PWA）下也能開啟。

### 4. 🛠️ 系統底層優化 (System Optimization) - [已完成]
- [x] **全域語音修復 (Speech Synthesis Fix)**：建立 `js-common.js` 並整合，解決點擊失效與 GC 中斷。
- [x] **G4 教材重構**：完成 JSON 化、萬用產生器、動態渲染修復。
- [x] **G2 教材重構**：完成 JSON 化、難度調降、重新生成。
- [x] **G2 遊戲修復**：全系列 Game 1-8 語音修復完成，Game 4 難度同步調降。
- [x] **GK 內容增強**：完成 GK 單元重構，並整合 YouTube 唱歌學習連結。
- [x] **連結檢查**：使用 `check_videos.py` 完成全站遞迴掃描，影片有效率 100% (含替換失效 404 連結)。
- [x] **單字庫 JSON 化 (Vocabulary Refactoring)**：
    - [x] 已完成 `vocab_gk.json`, `vocab_g2.json` 與 `vocab_g4.json`。
    - [x] 成功對齊台灣教育部小學英語建議字彙難度。
    - [x] 開發基於萬用模板的通用教材產生器 `build_units.py`。

---

## 🛠️ 單元標準規範 (Unit Standards)
1. **Page 1**: YouTube 暖身
2. **Page 2**: 6 個核心單字 (大圖、點擊發音)
3. **Page 3**: 3 選 1 圖文測驗
4. **Page 4**: 固定句型朗讀練習
5. **Page 5**: 獎勵特效與進度寫入
