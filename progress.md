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

### 🧪 系統驗證 (待執行項目)
- [ ] **斷點與佈局檢查**：測試在窄螢幕手機上 `vocab-grid` 與 `game-grid` 的顯示是否會跑版。
- [ ] **GK 視覺優化**：確保按鈕寬度一致、對齊與平板互動友善。

### 🏗️ 基礎建設
- [x] 建立通用樣式 `style-common.css`
- [x] 整合入口網頁 `index.html` (串聯幼兒園、小二、小四)
- [x] **網站線上託管**：已透過 GitHub Pages 上線 (https://del313.github.io/ele2_eng/)
- [x] **系統驗證簡化**：根據指示跳過音效相容性、解鎖邏輯與影片效能之細部檢查，專注於佈局優化。
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
- [x] **GK 單元教學內容簡化**：已將 Unit 1-8 全面轉型為「字母 A-Z 與基礎單字」啟蒙模式，符合幼兒教學需求。
- [x] **GK 單元結構重構**：完成三頁式流程（暖身影片、字母單字、完成頁面），並優化 UI 導覽。
- [x] **自動化流程建立**：新增 `unit_template_gk.html` 模板，並讓 `build_units.py` 支援 GK 批次產生。
- [x] **GK 影片修復**：解決所有 404 失效連結，並為 8 個單元配置獨立且高品質的影片。

### 2. 📚 國小各年級教材擴充 (Grade 2-6 Roadmap)
- [x] **Grade 2 (小二)**：12單元 (已完成) - 基礎生活單字。
- [x] **Grade 3 (小三)**：12單元 (已完成) - 螺旋式上升，含 8 款專屬遊戲與個別化收尾解說。
- [x] **Grade 4 (小四)**：12單元 (已完成) - 情境對話與進階單字。
- [x] **Grade 5 (小五)**：15單元 (已完成) - 功能性生活應用，含 5 款專屬遊戲 (語音支援、全寬佈局、離線備援)。
| **Grade 6** | Unit 1 - 6 | 不規則動詞三態 (Phase 1) | Game 1 | ✅ Phase 1 全面完成 |
| **Grade 6** | Unit 7 - 12 | 邏輯連接詞 (Phase 2) | Game 2 | ⏳ 待啟動 |
| **Grade 6** | Unit 13 - 18 | 時態與整合 (Phase 3) | Game 3, 4 | ⏳ 待啟動 |

### 3. 📱 平台優化 (Platform Optimization)
- [x] **全域進度邏輯修復**：修正 `index.html` 的進度計算 Bug，現在能正確讀取物件格式的進度資料。
- [x] **G3/G5 課程擴充**：
    - [x] 完成 G3 8 款遊戲整合與 12 單元發布。
    - [x] 完成 G5 `vocab_g5.json` (15 單元) 資料庫建立、15 個單元產生與 100% 影片驗證。
    - [x] 完成 G5 5 款互動遊戲 (Word Scramble, Mystery Clue, Sentence Pro, Bubble Pop 2.0, Final Challenge) 開發。
    - [x] 實作 G5 遊戲全寬佈局 (Full-width) 與語音播放按鈕 🔊。
- [x] **UI/UX 深度修復**：
    - [x] 修復 Game 7 在寬螢幕下的對齊偏移。
    - [x] 移除造句遊戲選項中的標點符號暗示，增加挑戰性。
    - [x] 為所有遊戲加入 Fallback 備援機制，支援本地直接開啟。
- [x] **Git 安全流程**：建立 `GEMINI.md` 規範 `git push` 前必須獲得人工許可。
- [x] **Git 遠端同步**：所有修改已推送到 GitHub Pages 伺服器。
...

- [x] **全域語效修復 (Speech & Sound Fix)**：
    - [x] 修正 G4 系列遊戲缺少 `js-common.js` 引用導致的 `playSound` 崩潰。
    - [x] 修正 G4 Game 4 翻牌配對錯誤後無法自動回復的 Bug。
- [x] **跨裝置相容性測試**：
    - [x] 測試 iOS Safari 的 Web Speech API 是否能自動播放音效 (透過 `js-common.js` 整合)。
    - [x] 檢查小二/小四遊戲在不同解析度手機上的佈局。
- [x] **載入速度優化**：已將單元 CSS 外部化至 `style-unit.css`，大幅縮減 HTML 體積並提升維護效率。

### 3. ✨ 功能增強 (Feature Requests)
- [x] **全域進度統計**：在主入口頁面實作各年級完成度百分比顯示。
- [x] **音效回饋**：實作「答對/答錯」動態音效產生邏輯，並整合至全站測驗與遊戲。
- [x] **離線功能**：實作 PWA (Service Worker + Manifest)，支援資源快取與「新增至桌面」。

### 4. 🛠️ 系統底層優化 (System Optimization) - [已完成]
- [x] **全域語音修復 (Speech Synthesis Fix)**：建立 `js-common.js` 並整合，解決點擊失效與 GC 中斷。
- [x] **G4 教材重構**：完成 JSON 化、萬用產生器、動態渲染修復。
- [x] **G2 教材重構**：完成 JSON 化、難度調降、重新生成。
- [x] **G2 遊戲修復**：全系列 Game 1-8 語音修復完成，Game 4 難度同步調降。
- [x] **GK 內容增強**：完成 GK 單元重構，並整合 YouTube 唱歌學習連結。
- [x] **連結檢查**：使用 `check_videos.py` 完成全站遞迴掃描，影片有效率 100% (含替換失效 404 連結)。
    - [x] **檢查工具優化**：為 `check_videos.py` 加入 10s 逾時機制，解決 GK 目錄掃描卡住問題。
- [x] **G4 Unit 9 影片修正**：更換為 Super Simple Songs 英文版 "Yes, I Can!" 並重新生成。
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
