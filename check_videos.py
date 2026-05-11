import os
import re
import urllib.request
import urllib.error
import json

def check_youtube_video(video_id):
    # 使用 YouTube 官方 OEmbed API，這對自動化檢查最友善
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            # 如果能拿到 title，代表影片存在且公開
            return True, f"OK ({data.get('title', 'No Title')})"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "❌ 影片不存在或已刪除 (404)"
        if e.code == 401:
            return False, "❌ 影片不開放嵌入或私人影片 (401)"
        return False, f"❌ HTTP 錯誤 {e.code}"
    except urllib.error.URLError as e:
        return False, f"❌ 網路連線錯誤或逾時: {str(e)}"
    except Exception as e:
        return False, f"❌ 檢查出錯: {str(e)}"

def scan_and_fix():
    youtube_pattern = re.compile(r'youtube\.com/watch\?v=([a-zA-Z0-9_{}-]{11,})')
    
    print("🔍 啟動全站影片驗證程序 (含子目錄)...\n")
    
    all_ok = True
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = youtube_pattern.findall(content)
                    
                    if not matches:
                        continue
                        
                    for video_id in set(matches):
                        if video_id == "{video_id}":
                            print(f"🚨 檔案: {file_path} | 發現錯誤佔位符: {{video_id}}")
                            all_ok = False
                            continue
                            
                        is_ok, msg = check_youtube_video(video_id)
                        status_icon = "✅" if is_ok else "🚨"
                        print(f"{status_icon} 檔案: {file_path} | ID: {video_id} | 狀態: {msg}")
                        if not is_ok:
                            all_ok = False

    if all_ok:
        print("\n🎉 恭喜！目前所有檔案中的影片連結在 API 驗證下皆為有效。")
    else:
        print("\n⚠️ 仍有部分連結失效，請根據上述報告更新 ID。")

if __name__ == "__main__":
    scan_and_fix()
