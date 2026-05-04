/**
 * ele2_eng 通用 JavaScript 工具函式庫
 * 整合：語音播放 (TTS)、進度管理、通用工具
 */

// 避免 Utterance 被垃圾回收導致播放中斷
let speechInstance = null;

/**
 * 強健的語音播放函數
 * @param {string} text 要朗讀的文字
 * @param {function|HTMLElement} btnOrCallback 播放結束後的回調或按鈕元素
 */
function speak(text, btnOrCallback) {
    if (!window.speechSynthesis) {
        console.error("此瀏覽器不支持 Web Speech API");
        return;
    }

    // 1. 先取消正在進行的所有語音
    window.speechSynthesis.cancel();

    // 2. 建立新的語音物件
    const msg = new SpeechSynthesisUtterance(text);
    msg.lang = 'en-US';
    msg.rate = 0.9;
    msg.pitch = 1.0;

    // 處理按鈕動畫
    const isButton = btnOrCallback instanceof HTMLElement;
    if (isButton) {
        btnOrCallback.classList.add('speaking');
    }

    // 3. 保持引用防止 GC
    speechInstance = msg;

    // 4. 事件處理
    msg.onend = () => {
        speechInstance = null;
        if (isButton) {
            btnOrCallback.classList.remove('speaking');
        } else if (typeof btnOrCallback === 'function') {
            btnOrCallback();
        }
    };

    msg.onerror = (event) => {
        console.error("SpeechSynthesis Error:", event);
        speechInstance = null;
        if (isButton) {
            btnOrCallback.classList.remove('speaking');
        }
    };

    // 5. 行動裝置修復
    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
    }

    // 6. 執行播放
    window.speechSynthesis.speak(msg);
}

/**
 * 進度儲存輔助
 * @param {string} key localStorage 鍵名
 * @param {string} unitId 單元 ID
 */
function markUnitComplete(key, unitId) {
    try {
        const progress = JSON.parse(localStorage.getItem(key) || '{}');
        progress[unitId] = true;
        localStorage.setItem(key, JSON.stringify(progress));
    } catch (e) {
        console.error("Progress save failed:", e);
    }
}
