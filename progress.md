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
- [x] 建立 `style-g2.css`
- [x] 索引頁面 `index.html` (12單元+8遊戲，3+2 解鎖邏輯)
- [x] **網站線上託管**：已透過 GitHub Pages 上線 (https://del313.github.io/ele2_eng/)

### ✍️ 內容開發
- [x] 完成 Unit 1 - 12 所有單元內容與互動邏輯
- [x] 完成 Game 1 - 8 所有遊戲機制

---

## 🚀 託管與佈局 (Hosting & Deployment)
- **託管平台**: GitHub Pages
- **部署方式**: GitHub Actions / Branch Deploy (main)
- **連線優化**: 已確認 Cloudflare 台北節點支援，連線品質優良。
- **線上網址**: [https://del313.github.io/ele2_eng/](https://del313.github.io/ele2_eng/)

---

## 🛠️ 單元標準規範 (Unit Standards)
1. **Page 1**: YouTube 暖身
2. **Page 2**: 6 個核心單字 (大圖、點擊發音)
3. **Page 3**: 3 選 1 圖文測驗
4. **Page 4**: 固定句型朗讀練習
5. **Page 5**: 獎勵特效與進度寫入
