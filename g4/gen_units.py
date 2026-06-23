#!/usr/bin/env python3
"""Generate unit2.html through unit12.html for the Grade 4 English course."""

UNITS = [
    {
        "num": 2, "id": "unit2", "next_id": "unit3",
        "title": "My Family", "zh_title": "家庭成員",
        "icon": "👨‍👩‍👧", "grade_label": "UNIT 2 OF 12",
        "video_url": "https://www.youtube.com/watch?v=8S9Ynkb0EN4",
        "video_label": "開啟 Family Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 認識家人",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱 Family Song 🎤",
            "2. 唱完後，指著家裡的人說他們的英文稱呼",
            "3. 家長問：「Who is this?」孩子練習回答 😄",
        ],
        "core_vocab": [
            ("father", "爸爸"), ("mother", "媽媽"), ("brother", "哥哥/弟弟"),
            ("sister", "姊姊/妹妹"), ("grandfather", "爺爺/外公"),
            ("grandmother", "奶奶/外婆"), ("family", "家庭"), ("baby", "寶寶"),
        ],
        "ext_vocab": [
            ("uncle", "叔叔/伯伯"), ("aunt", "阿姨/姑姑"),
            ("cousin", "表/堂兄弟姊妹"), ("pet", "寵物"),
        ],
        "sentences": [
            ("句型 1", "This is my <blank>___</blank>.", "This is my mother.", "This is my mother."),
            ("句型 2", "I have a <blank>___</blank> and a <blank>___</blank>.", "I have a brother and a sister.", "I have a brother and a sister."),
            ("句型 3（延伸）", "My family has <blank>___</blank> people.", "My family has four people.", "My family has four people."),
        ],
        "qa": [
            ("How many people are in your family?", "My family has ___ people."),
            ("Do you have a brother?", "Yes, I do. / No, I don't."),
            ("Who is this?", "This is my ___."),
            ("Do you have a pet?", "Yes, I have a ___. / No, I don't."),
            ("What is your mother's name?", "My mother's name is ___."),
        ],
        "wrapup_title": "家庭介紹挑戰",
        "wrapup_sub": "5 分鐘 · 介紹你的家人！",
        "wrapup_lines": [
            "This is my <fill>father</fill>.",
            "This is my <fill>mother</fill>.",
            "I have a <fill>___</fill>.",
            "My family has <fill>___</fill> people.",
            "I love my <fill>family</fill>!",
        ],
        "wrapup_tip": "⭐ 目標：指著家人照片，流暢介紹每一位！",
        "wrapup_challenge": [
            "1. 拿出家人照片，孩子逐一介紹 📸",
            "2. 家長用英文問：「Who is this?」孩子回答",
            "3. 全部說完就給貼紙！ 🌟",
        ],
        "complete_next": "Unit 3：School Days",
        "tip_box": "💡 家長小技巧：讓孩子用英文當小老師，教你說家人的稱呼！",
    },
    {
        "num": 3, "id": "unit3", "next_id": "unit4",
        "title": "School Days", "zh_title": "學校文具",
        "icon": "🎒", "grade_label": "UNIT 3 OF 12",
        "video_url": "https://www.youtube.com/watch?v=7S_NSsUcWWw",
        "video_label": "開啟 School Supplies Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 認識文具",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱文具歌 🎤",
            "2. 唱完後，從書包裡拿出每樣文具說英文名字",
            "3. 家長說英文，孩子快速從桌上找到那個文具 😄",
        ],
        "core_vocab": [
            ("pencil", "鉛筆"), ("eraser", "橡皮擦"), ("ruler", "尺"),
            ("book", "書"), ("bag", "書包"), ("desk", "桌子"),
            ("chair", "椅子"), ("classroom", "教室"),
        ],
        "ext_vocab": [
            ("pen", "原子筆"), ("notebook", "筆記本"),
            ("scissors", "剪刀"), ("crayon", "蠟筆"),
        ],
        "sentences": [
            ("句型 1", "This is a <blank>___</blank>.", "This is a pencil.", "This is a pencil."),
            ("句型 2", "I have a <blank>___</blank> in my bag.", "I have a ruler in my bag.", "I have a ruler in my bag."),
            ("句型 3（延伸）", "How many <blank>___</blank> do you have?", "How many pencils do you have?", "How many pencils do you have?"),
        ],
        "qa": [
            ("What's this?", "This is a ___."),
            ("Is this your eraser?", "Yes, it is. / No, it isn't."),
            ("How many books do you have?", "I have ___ books."),
            ("Where is your bag?", "My bag is on the chair."),
            ("What color is your pencil?", "My pencil is ___."),
        ],
        "wrapup_title": "書包大搜查",
        "wrapup_sub": "5 分鐘 · 打開書包，一一說出文具！",
        "wrapup_lines": [
            "I have a <fill>pencil</fill> in my bag.",
            "I have an <fill>eraser</fill> in my bag.",
            "I have a <fill>ruler</fill> in my bag.",
            "I have a <fill>book</fill> in my bag.",
            "My bag is on the <fill>desk</fill>.",
        ],
        "wrapup_tip": "⭐ 目標：從書包拿出每樣文具，說出完整英文句子！",
        "wrapup_challenge": [
            "1. 孩子打開書包，邊拿邊說：「I have a ___!」📚",
            "2. 家長問：「What color is your ___?」",
            "3. 全說完就給貼紙！ 🌟",
        ],
        "complete_next": "Unit 4：I Love Food",
        "tip_box": "💡 家長小技巧：把文具貼上英文標籤貼紙，每天看到就加深記憶！",
    },
    {
        "num": 4, "id": "unit4", "next_id": "unit5",
        "title": "I Love Food", "zh_title": "食物飲料",
        "icon": "🍎", "grade_label": "UNIT 4 OF 12",
        "video_url": "https://www.youtube.com/watch?v=VNT2rWpCZ60",
        "video_label": "開啟 Food Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 認識食物",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱食物歌 🎤",
            "2. 唱完後，打開冰箱，用英文說出看到的食物",
            "3. 家長說中文，孩子說英文，比賽誰說得快 😄",
        ],
        "core_vocab": [
            ("rice", "飯"), ("noodle", "麵"), ("bread", "麵包"),
            ("apple", "蘋果"), ("milk", "牛奶"), ("water", "水"),
            ("egg", "雞蛋"), ("chicken", "雞肉"),
        ],
        "ext_vocab": [
            ("pizza", "披薩"), ("juice", "果汁"),
            ("cake", "蛋糕"), ("cookie", "餅乾"),
        ],
        "sentences": [
            ("句型 1", "I like <blank>___</blank>.", "I like rice.", "I like rice."),
            ("句型 2", "I don't like <blank>___</blank>.", "I don't like noodles.", "I don't like noodles."),
            ("句型 3（延伸）", "I want some <blank>___</blank>, please.", "I want some milk, please.", "I want some milk, please."),
        ],
        "qa": [
            ("Do you like apples?", "Yes, I do. / No, I don't."),
            ("What do you want for lunch?", "I want ___."),
            ("Do you drink milk every day?", "Yes, I do. / No, I don't."),
            ("What's your favorite food?", "My favorite food is ___."),
            ("Do you like bread or rice?", "I like ___."),
        ],
        "wrapup_title": "點餐挑戰",
        "wrapup_sub": "5 分鐘 · 假裝在餐廳點餐！",
        "wrapup_lines": [
            "I like <fill>rice</fill> and <fill>chicken</fill>.",
            "I don't like <fill>___</fill>.",
            "I want some <fill>milk</fill>, please.",
            "My favorite food is <fill>___</fill>.",
            "I eat <fill>bread</fill> in the morning.",
        ],
        "wrapup_tip": "⭐ 目標：假裝家長是服務生，孩子用英文完整點餐！",
        "wrapup_challenge": [
            "1. 角色扮演：家長是服務生，孩子是客人 🍽️",
            "2. 服務生問：「What do you want?」孩子用英文回答",
            "3. 加碼挑戰：說出不喜歡的食物，加說原因 🌟",
        ],
        "complete_next": "Unit 5：Animals Are Cool",
        "tip_box": "💡 家長小技巧：吃飯時用英文說食物名，自然增加練習機會！",
    },
    {
        "num": 5, "id": "unit5", "next_id": "unit6",
        "title": "Animals Are Cool", "zh_title": "動物",
        "icon": "🐶", "grade_label": "UNIT 5 OF 12",
        "video_url": "https://www.youtube.com/watch?v=Pk4UrpMSSuI",
        "video_label": "開啟 Animals Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 模仿動物",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱動物歌 🎤",
            "2. 唱完後，家長模仿一種動物的叫聲，孩子猜英文名字",
            "3. 換孩子模仿，家長猜 😄",
        ],
        "core_vocab": [
            ("dog", "狗"), ("cat", "貓"), ("bird", "鳥"),
            ("fish", "魚"), ("rabbit", "兔子"), ("tiger", "老虎"),
            ("elephant", "大象"), ("monkey", "猴子"),
        ],
        "ext_vocab": [
            ("bear", "熊"), ("lion", "獅子"),
            ("panda", "熊貓"), ("giraffe", "長頸鹿"),
        ],
        "sentences": [
            ("句型 1", "I have a <blank>___</blank>.", "I have a dog.", "I have a dog."),
            ("句型 2", "The <blank>___</blank> can <blank>___</blank>.", "The bird can fly.", "The bird can fly."),
            ("句型 3（延伸）", "My favorite animal is the <blank>___</blank>.", "My favorite animal is the elephant.", "My favorite animal is the elephant."),
        ],
        "qa": [
            ("Do you have a pet?", "Yes, I have a ___. / No, I don't."),
            ("What animal do you like?", "I like ___."),
            ("Can a fish fly?", "No, it can't. It can swim."),
            ("Is a tiger big or small?", "A tiger is big."),
            ("What sound does a dog make?", "A dog says Woof!"),
        ],
        "wrapup_title": "動物達人挑戰",
        "wrapup_sub": "5 分鐘 · 介紹你最喜歡的動物！",
        "wrapup_lines": [
            "My favorite animal is the <fill>___</fill>.",
            "It is <fill>big</fill> / <fill>small</fill>.",
            "It can <fill>run</fill> / <fill>swim</fill> / <fill>fly</fill>.",
            "I think it is very <fill>cool</fill>!",
            "Do you like <fill>___</fill>?",
        ],
        "wrapup_tip": "⭐ 目標：說出最喜歡的動物，並用2句話介紹它！",
        "wrapup_challenge": [
            "1. 孩子畫一隻最喜歡的動物，然後介紹它 🎨",
            "2. 家長問：「Can it fly? Can it swim?」孩子回答",
            "3. 猜謎遊戲：孩子描述，家長猜是什麼動物 🌟",
        ],
        "complete_next": "Unit 6：My Day",
        "tip_box": "💡 家長小技巧：去動物園或看動物影片時，鼓勵孩子說英文名字！",
    },
    {
        "num": 6, "id": "unit6", "next_id": "unit7",
        "title": "My Day", "zh_title": "時間與作息",
        "icon": "⏰", "grade_label": "UNIT 6 OF 12",
        "video_url": "https://www.youtube.com/watch?v=TNxCPAMVGdQ",
        "video_label": "開啟 Daily Routine Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 認識作息",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱日常作息歌 🎤",
            "2. 唱完後，家長說時間，孩子說那個時候在做什麼",
            "3. 一起比比看，誰的生活作息最規律 😄",
        ],
        "core_vocab": [
            ("morning", "早上"), ("noon", "中午"), ("afternoon", "下午"),
            ("night", "晚上"), ("eat", "吃"), ("sleep", "睡覺"),
            ("study", "讀書"), ("play", "玩"),
        ],
        "ext_vocab": [
            ("exercise", "運動"), ("shower", "淋浴"),
            ("read", "閱讀"), ("watch", "看（電視）"),
        ],
        "sentences": [
            ("句型 1", "In the morning, I <blank>___</blank>.", "In the morning, I eat breakfast.", "In the morning, I eat breakfast."),
            ("句型 2", "I <blank>___</blank> at <blank>___</blank> o'clock.", "I sleep at nine o'clock.", "I sleep at nine o'clock."),
            ("句型 3（延伸）", "Every day, I <blank>___</blank> and <blank>___</blank>.", "Every day, I study and play.", "Every day, I study and play."),
        ],
        "qa": [
            ("What do you do in the morning?", "In the morning, I ___."),
            ("When do you go to sleep?", "I sleep at ___ o'clock."),
            ("Do you study every day?", "Yes, I do. / No, I don't."),
            ("What do you do after school?", "I ___ after school."),
            ("Do you play in the afternoon?", "Yes, I do!"),
        ],
        "wrapup_title": "我的一天",
        "wrapup_sub": "5 分鐘 · 說出你今天的作息！",
        "wrapup_lines": [
            "In the morning, I <fill>eat breakfast</fill>.",
            "I go to school at <fill>___</fill> o'clock.",
            "In the afternoon, I <fill>study</fill>.",
            "At night, I <fill>sleep</fill>.",
            "Every day, I <fill>play</fill> and <fill>read</fill>.",
        ],
        "wrapup_tip": "⭐ 目標：說出今天從早到晚做了哪些事！",
        "wrapup_challenge": [
            "1. 孩子畫一個今天的時間表，用英文說每格 📅",
            "2. 家長問：「What time do you eat lunch?」孩子回答",
            "3. 互相比較作息，說說有什麼不同 🌟",
        ],
        "complete_next": "Unit 7：Colors & Clothes",
        "tip_box": "💡 家長小技巧：每天問孩子一句「What did you do this morning?」養成英文習慣！",
    },
    {
        "num": 7, "id": "unit7", "next_id": "unit8",
        "title": "Colors & Clothes", "zh_title": "顏色衣物",
        "icon": "👕", "grade_label": "UNIT 7 OF 12",
        "video_url": "https://www.youtube.com/watch?v=0KjX7OhGBos",
        "video_label": "開啟 Colors Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 指顏色",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱顏色歌 🎤",
            "2. 唱完後，家長說顏色，孩子快速找到房間裡該顏色的東西",
            "3. 換孩子出題 😄",
        ],
        "core_vocab": [
            ("red", "紅色"), ("blue", "藍色"), ("green", "綠色"),
            ("yellow", "黃色"), ("shirt", "上衣"), ("pants", "褲子"),
            ("shoes", "鞋子"), ("hat", "帽子"),
        ],
        "ext_vocab": [
            ("white", "白色"), ("black", "黑色"),
            ("dress", "洋裝"), ("jacket", "外套"),
        ],
        "sentences": [
            ("句型 1", "My <blank>___</blank> is <blank>___</blank>.", "My shirt is blue.", "My shirt is blue."),
            ("句型 2", "I am wearing a <blank>___</blank> <blank>___</blank>.", "I am wearing a red hat.", "I am wearing a red hat."),
            ("句型 3（延伸）", "I like the <blank>___</blank> <blank>___</blank>.", "I like the green shoes.", "I like the green shoes."),
        ],
        "qa": [
            ("What color is your shirt?", "My shirt is ___."),
            ("What are you wearing today?", "I am wearing a ___."),
            ("Do you like the color blue?", "Yes, I do! / No, I don't."),
            ("What color are your shoes?", "My shoes are ___."),
            ("Is your hat red or yellow?", "My hat is ___."),
        ],
        "wrapup_title": "今日穿搭介紹",
        "wrapup_sub": "5 分鐘 · 說出你今天穿什麼！",
        "wrapup_lines": [
            "Today, I am wearing a <fill>___</fill> shirt.",
            "My pants are <fill>___</fill>.",
            "My shoes are <fill>___</fill>.",
            "I like the color <fill>___</fill>.",
            "My favorite clothes are <fill>___</fill>.",
        ],
        "wrapup_tip": "⭐ 目標：站在鏡子前，說出你身上穿的每樣東西！",
        "wrapup_challenge": [
            "1. 孩子站在鏡子前，說出整套穿著 🪞",
            "2. 家長問：「What color is your ___?」孩子回答",
            "3. 加碼：設計夢想穿搭，畫下來並介紹 🌟",
        ],
        "complete_next": "Unit 8：How's the Weather?",
        "tip_box": "💡 家長小技巧：每天早上問孩子穿什麼衣服出門，用英文說！",
    },
    {
        "num": 8, "id": "unit8", "next_id": "unit9",
        "title": "How's the Weather?", "zh_title": "天氣季節",
        "icon": "🌤", "grade_label": "UNIT 8 OF 12",
        "video_url": "https://www.youtube.com/watch?v=rD5goS69LF4",
        "video_label": "開啟 Weather Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 看天氣",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱天氣歌 🎤",
            "2. 唱完後，看看窗外，用英文說今天的天氣",
            "3. 猜猜明天天氣如何，用英文說出來 😄",
        ],
        "core_vocab": [
            ("sunny", "晴天"), ("cloudy", "多雲"), ("rainy", "下雨"),
            ("windy", "刮風"), ("hot", "熱"), ("cold", "冷"),
            ("spring", "春天"), ("winter", "冬天"),
        ],
        "ext_vocab": [
            ("snowy", "下雪"), ("foggy", "起霧"),
            ("summer", "夏天"), ("autumn", "秋天"),
        ],
        "sentences": [
            ("句型 1", "It is <blank>___</blank> today.", "It is sunny today.", "It is sunny today."),
            ("句型 2", "The weather is <blank>___</blank> and <blank>___</blank>.", "The weather is hot and sunny.", "The weather is hot and sunny."),
            ("句型 3（延伸）", "In <blank>___</blank>, it is <blank>___</blank>.", "In winter, it is cold.", "In winter, it is cold."),
        ],
        "qa": [
            ("How's the weather today?", "It is ___ today."),
            ("Is it hot or cold?", "It is ___."),
            ("What's your favorite season?", "My favorite season is ___."),
            ("Do you like rainy days?", "Yes, I do. / No, I don't."),
            ("What do you wear when it's cold?", "I wear a jacket."),
        ],
        "wrapup_title": "天氣播報員",
        "wrapup_sub": "5 分鐘 · 假裝你是天氣播報員！",
        "wrapup_lines": [
            "Hello! Today is <fill>___</fill>.",
            "The weather is <fill>___</fill>.",
            "It is <fill>hot</fill> / <fill>cold</fill>.",
            "My favorite season is <fill>___</fill>.",
            "In <fill>summer</fill>, it is very <fill>hot</fill>!",
        ],
        "wrapup_tip": "⭐ 目標：像播報員一樣，流暢報告今日天氣！",
        "wrapup_challenge": [
            "1. 假裝攝影機，孩子對著家長播報天氣 📺",
            "2. 家長問：「What should I wear today?」孩子建議穿著",
            "3. 加碼：說說最喜歡的季節和原因 🌟",
        ],
        "complete_next": "Unit 9：I Can Do It!",
        "tip_box": "💡 家長小技巧：每天早上讓孩子看天氣，用英文說天氣狀況！",
    },
    {
        "num": 9, "id": "unit9", "next_id": "unit10",
        "title": "I Can Do It!", "zh_title": "能力嗜好",
        "icon": "💪", "grade_label": "UNIT 9 OF 12",
        "video_url": "https://www.youtube.com/watch?v=dHbkaMpiVBk",
        "video_label": "開啟 I Can Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 表演動作",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱能力歌 🎤",
            "2. 唱完後，家長說動詞，孩子馬上做出那個動作",
            "3. 用英文說「I can ___!」 😄",
        ],
        "core_vocab": [
            ("run", "跑步"), ("swim", "游泳"), ("sing", "唱歌"),
            ("dance", "跳舞"), ("draw", "畫畫"), ("read", "閱讀"),
            ("cook", "做飯"), ("ride", "騎"),
        ],
        "ext_vocab": [
            ("jump", "跳"), ("climb", "爬"),
            ("paint", "繪畫"), ("play piano", "彈鋼琴"),
        ],
        "sentences": [
            ("句型 1", "I can <blank>___</blank>.", "I can swim.", "I can swim."),
            ("句型 2", "I can't <blank>___</blank>.", "I can't cook.", "I can't cook."),
            ("句型 3（延伸）", "Can you <blank>___</blank>? Yes, I can. / No, I can't.", "Can you dance? Yes, I can!", "Can you dance? Yes, I can!"),
        ],
        "qa": [
            ("Can you swim?", "Yes, I can! / No, I can't."),
            ("What can you do?", "I can ___ and ___."),
            ("Can you cook?", "Yes, I can. / No, I can't."),
            ("Can your mother sing?", "Yes, she can. / No, she can't."),
            ("What do you like to do?", "I like to ___."),
        ],
        "wrapup_title": "才藝秀",
        "wrapup_sub": "5 分鐘 · 展示你的才能！",
        "wrapup_lines": [
            "I can <fill>___</fill> and <fill>___</fill>.",
            "I can't <fill>___</fill> yet.",
            "I want to learn to <fill>___</fill>.",
            "My best skill is <fill>___</fill>.",
            "Can you <fill>___</fill>? Let me show you!",
        ],
        "wrapup_tip": "⭐ 目標：展示一項才能，並用英文介紹！",
        "wrapup_challenge": [
            "1. 孩子展示一項才能（唱歌/畫畫/跑步） 🎭",
            "2. 說出：「I can ___! Watch me!」",
            "3. 家長也表演一項，孩子猜並說英文 🌟",
        ],
        "complete_next": "Unit 10：In the City",
        "tip_box": "💡 家長小技巧：鼓勵孩子說「I can do it!」當遇到困難的時候！",
    },
    {
        "num": 10, "id": "unit10", "next_id": "unit11",
        "title": "In the City", "zh_title": "城市場所",
        "icon": "🏙", "grade_label": "UNIT 10 OF 12",
        "video_url": "https://www.youtube.com/watch?v=QnJcWMnS4sE",
        "video_label": "開啟 Places in the City Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 認識地點",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱城市歌 🎤",
            "2. 唱完後，說說你家附近有哪些地方，用英文說",
            "3. 比賽：誰能說出最多城市地點的英文 😄",
        ],
        "core_vocab": [
            ("school", "學校"), ("park", "公園"), ("hospital", "醫院"),
            ("store", "商店"), ("library", "圖書館"), ("bus", "公車"),
            ("car", "汽車"), ("road", "路"),
        ],
        "ext_vocab": [
            ("bank", "銀行"), ("restaurant", "餐廳"),
            ("museum", "博物館"), ("subway", "地鐵"),
        ],
        "sentences": [
            ("句型 1", "I go to the <blank>___</blank>.", "I go to the park.", "I go to the park."),
            ("句型 2", "Let's go to the <blank>___</blank>!", "Let's go to the library!", "Let's go to the library!"),
            ("句型 3（延伸）", "The <blank>___</blank> is near here.", "The store is near here.", "The store is near here."),
        ],
        "qa": [
            ("Where do you go on weekends?", "I go to the ___."),
            ("Is there a park near your home?", "Yes, there is. / No, there isn't."),
            ("How do you go to school?", "I go by bus / car."),
            ("What do you do at the library?", "I read books there."),
            ("Let's go to the park! Do you want to go?", "Yes! / No, let's go to the ___."),
        ],
        "wrapup_title": "城市導遊",
        "wrapup_sub": "5 分鐘 · 介紹你家附近的地方！",
        "wrapup_lines": [
            "Near my home, there is a <fill>park</fill>.",
            "I go to the <fill>school</fill> every day.",
            "On weekends, I go to the <fill>___</fill>.",
            "I go by <fill>bus</fill> / <fill>car</fill>.",
            "Let's go to the <fill>library</fill>!",
        ],
        "wrapup_tip": "⭐ 目標：介紹三個你家附近的地方，說明怎麼去！",
        "wrapup_challenge": [
            "1. 孩子畫一張簡單地圖，標上英文地點名稱 🗺️",
            "2. 用英文說：「Near my home, there is a ___」",
            "3. 家長說：「I want to go to the ___」，孩子指地圖說方向 🌟",
        ],
        "complete_next": "Unit 11：My Body",
        "tip_box": "💡 家長小技巧：外出時，路過地點就說英文名字，自然學習！",
    },
    {
        "num": 11, "id": "unit11", "next_id": "unit12",
        "title": "My Body", "zh_title": "身體部位",
        "icon": "🙋", "grade_label": "UNIT 11 OF 12",
        "video_url": "https://www.youtube.com/watch?v=ZanHgPprl-0",
        "video_label": "開啟 Head Shoulders Knees & Toes 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 指身體部位",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱 Head, Shoulders, Knees and Toes 🎤",
            "2. 唱完後，家長說身體部位，孩子快速指到",
            "3. 越唱越快，看能不能跟上 😄",
        ],
        "core_vocab": [
            ("head", "頭"), ("eyes", "眼睛"), ("ears", "耳朵"),
            ("nose", "鼻子"), ("mouth", "嘴巴"), ("hands", "手"),
            ("legs", "腿"), ("feet", "腳"),
        ],
        "ext_vocab": [
            ("neck", "脖子"), ("shoulders", "肩膀"),
            ("fingers", "手指"), ("stomach", "肚子"),
        ],
        "sentences": [
            ("句型 1", "I have two <blank>___</blank>.", "I have two eyes.", "I have two eyes."),
            ("句型 2", "Touch your <blank>___</blank>!", "Touch your nose!", "Touch your nose!"),
            ("句型 3（延伸）", "My <blank>___</blank> hurts.", "My head hurts.", "My head hurts."),
        ],
        "qa": [
            ("How many eyes do you have?", "I have two eyes."),
            ("Point to your nose!", "Here it is! (點鼻子)"),
            ("Does your head hurt?", "Yes, it does. / No, it doesn't."),
            ("What do you use your hands for?", "I use my hands to ___."),
            ("How many fingers do you have?", "I have ten fingers."),
        ],
        "wrapup_title": "Simon Says 挑戰",
        "wrapup_sub": "5 分鐘 · 玩 Simon Says 遊戲！",
        "wrapup_lines": [
            "I have a <fill>head</fill>, <fill>eyes</fill>, and a <fill>nose</fill>.",
            "I have two <fill>hands</fill> and two <fill>feet</fill>.",
            "Simon says: touch your <fill>ears</fill>!",
            "I use my <fill>eyes</fill> to see.",
            "I use my <fill>mouth</fill> to speak English!",
        ],
        "wrapup_tip": "⭐ 目標：玩 Simon Says，指令全部用英文說！",
        "wrapup_challenge": [
            "1. 孩子當 Simon，用英文發指令給家長 🎭",
            "2. 說：「Simon says, touch your ___!」",
            "3. 不說 Simon says 直接下指令時，家長不要動，看孩子記不記得規則 🌟",
        ],
        "complete_next": "Unit 12：Show & Tell",
        "tip_box": "💡 家長小技巧：洗澡時，讓孩子一邊洗一邊說身體部位的英文！",
    },
    {
        "num": 12, "id": "unit12", "next_id": None,
        "title": "Show & Tell", "zh_title": "綜合發表",
        "icon": "🎤", "grade_label": "UNIT 12 OF 12",
        "video_url": "https://www.youtube.com/watch?v=l4WNrvVjiTw",
        "video_label": "開啟 Feelings Song 影片",
        "warmup_sub": "5 分鐘 · 唱歌 + 說心情",
        "warmup_tasks": [
            "1. 點上面按鈕，一起唱心情歌 🎤",
            "2. 唱完後，說說今天的心情是什麼",
            "3. 互相用英文問：「How do you feel today?」 😄",
        ],
        "core_vocab": [
            ("happy", "快樂"), ("sad", "難過"), ("big", "大"),
            ("small", "小"), ("fast", "快"), ("slow", "慢"),
            ("pretty", "漂亮"), ("strong", "強壯"),
        ],
        "ext_vocab": [
            ("scared", "害怕"), ("angry", "生氣"),
            ("quiet", "安靜"), ("loud", "吵鬧"),
        ],
        "sentences": [
            ("句型 1", "I feel <blank>___</blank> today.", "I feel happy today.", "I feel happy today."),
            ("句型 2", "It is <blank>___</blank> and <blank>___</blank>.", "It is big and strong.", "It is big and strong."),
            ("句型 3（延伸）", "This is my <blank>___</blank> because <blank>___</blank>.", "This is my favorite book because it is funny.", "This is my favorite book because it is funny."),
        ],
        "qa": [
            ("How do you feel today?", "I feel ___ today."),
            ("Are you happy or sad?", "I am ___."),
            ("Tell me about your favorite thing.", "My favorite ___ is ___."),
            ("Is a elephant fast or slow?", "An elephant is slow."),
            ("What makes you happy?", "___ makes me happy."),
        ],
        "wrapup_title": "Show & Tell 大挑戰！",
        "wrapup_sub": "10 分鐘 · 完整發表你的最愛！",
        "wrapup_lines": [
            "Hello, everyone! I feel <fill>happy</fill> today.",
            "My name is <fill>___</fill>. I am in Grade <fill>4</fill>.",
            "My favorite animal is the <fill>___</fill>.",
            "My favorite food is <fill>___</fill>.",
            "I can <fill>___</fill>. Thank you!",
        ],
        "wrapup_tip": "⭐ 最終目標：60秒完整英文自我介紹，從 Unit 1 到 Unit 12 全用上！",
        "wrapup_challenge": [
            "1. 孩子拿著最喜歡的東西（玩具/書），站起來發表 🌟",
            "2. 介紹：名字、年齡、家人、最喜歡的食物/動物/活動",
            "3. 說得流暢就給大獎！ 🏆",
        ],
        "complete_next": None,
        "tip_box": "💡 恭喜完成全部12個單元！你的孩子太棒了！💪",
    },
]


CSS = """  :root {
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
  .nav-step-info { text-align: center; font-size: 13px; color: var(--muted); min-width: 50px; }"""


def safe_js_str(s):
    return s.replace("'", "\\'").replace('"', '&quot;')


def render_pattern(pattern):
    """Convert <blank>___</blank> markers to HTML spans."""
    return pattern.replace('<blank>', '<span class="blank btn-hover">').replace('</blank>', '</span>')


def render_wrapup_line(line):
    """Convert <fill>text</fill> to styled spans."""
    return line.replace('<fill>', '<span class="fill btn-hover">').replace('</fill>', '</span>')


def build_unit(u):
    num = u["num"]
    uid = u["id"]
    title = u["title"]
    icon = u["icon"]
    grade_label = u["grade_label"]
    next_unit = u.get("next_id")
    complete_next = u.get("complete_next")

    # Core/ext vocab JS arrays
    core_js = ",\n  ".join(f'{{en:"{v[0]}",zh:"{v[1]}"}}'
                            for v in u["core_vocab"])
    ext_js = ",\n  ".join(f'{{en:"{v[0]}",zh:"{v[1]}"}}'
                           for v in u["ext_vocab"])

    # QA items HTML
    qa_html = ""
    for i, (q, a) in enumerate(u["qa"]):
        safe_q = q.replace("`", "\\`").replace("'", "\\'")
        qa_html += f'''  <div class="qa-item btn-hover">
    <div class="qa-num btn-hover">{{i+1}}</div>
    <div>
      <div class="qa-q btn-hover">Q: {{q}} <button class="speak-btn qa-speak btn-hover" onclick="speak(\`{safe_q}\`,this)">🔊</button></div>
      <div class="qa-a btn-hover">A: {{a}}</div>
    </div>
  </div>\n'''

    # Sentences HTML
    sent_html = ""
    for label, pattern, example, speak_text in u["sentences"]:
        safe_st = speak_text.replace("`", "\\`").replace("'", "\\'")
        sent_html += f'''  <div class="sentence-box btn-hover">
    <div class="slabel btn-hover">{{label}}</div>
    <div class="pattern btn-hover">{{render_pattern(pattern)}}</div>
    <div class="example btn-hover">→ {{example}} <button class="speak-btn sentence-speak btn-hover" onclick="speak(\`{safe_st}\`,this)">🔊</button></div>
  </div>\n'''

    # Wrapup lines
    wrapup_lines_html = "\n    ".join(
        render_wrapup_line(l) + "<br>" for l in u["wrapup_lines"]
    )

    # Warmup tasks
    warmup_tasks_html = "<br>\n    ".join(u["warmup_tasks"])

    # Wrapup challenge
    wrapup_challenge_html = "<br>\n    ".join(u["wrapup_challenge"])

    # Calculate anchor_num
    anchor_num = 1
    if u["num"] > 8: anchor_num = 3
    elif u["num"] > 4: anchor_num = 2

    # Complete section
    if complete_next:
        complete_next_text = f"你真棒！下次繼續 {complete_next}"
        home_btn = f'<a href="index.html#p{anchor_num}" class="home-link-btn btn-hover">回首頁 🏠</a>'
    else:
        complete_next_text = "恭喜你完成全部 12 個單元！你真的太棒了！🏆"
        home_btn = '<a href="index.html" class="home-link-btn btn-hover">回首頁查看成果 🏠</a>'

    html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unit {num} – {title}</title>
<script src="../js-common.js"></script>
<style>
{CSS}
</style>
</head>
<body>

<header style="position:relative">
  <a href="index.html" class="home-btn btn-hover">🏠 首頁</a>
  <div class="unit-label btn-hover">{grade_label} &nbsp;·&nbsp; GRADE 4</div>
  <h1>{icon} {title}</h1>
</header>

<div class="step-nav btn-hover" id="stepNav"></div>

<!-- PAGE 1: WARM UP -->
<div class="page active btn-hover" id="page-0">
  <div class="page-title btn-hover"><span>🎵</span> 暖身</div>
  <div class="page-sub btn-hover">{u["warmup_sub"]}</div>
  <div class="video-btn-wrap btn-hover">
    <a class="video-btn btn-hover" href="{u["video_url"]}" target="_blank" rel="noopener">
      <span class="yt-icon btn-hover">▶️</span> {u["video_label"]}
    </a>
  </div>
  <div class="task-card btn-hover">
    <strong>一起做：</strong><br>
    {warmup_tasks_html}
  </div>
</div>

<!-- PAGE 2: VOCABULARY -->
<div class="page btn-hover" id="page-1">
  <div class="page-title btn-hover"><span>🃏</span> 本期單字</div>
  <div class="page-sub btn-hover">10 分鐘 · 翻牌記單字 + 配對遊戲</div>

  <div class="vocab-section-label btn-hover">⭐ 核心單字（要記住！）</div>
  <div class="vocab-grid btn-hover" id="coreGrid"></div>

  <div class="vocab-section-label btn-hover" style="color:#00897B">🌱 延伸單字（有印象就好）</div>
  <div class="ext-note btn-hover">點卡片翻面看中文，認識就好，不列入測驗</div>
  <div class="vocab-grid btn-hover" id="extGrid"></div>

  <button class="flip-all-btn btn-hover" onclick="flipAll()">全部翻面 / 全部收起</button>

  <div class="game-label btn-hover">🎮 配對遊戲：點左邊英文，再點右邊中文</div>
  <div class="game-score btn-hover" id="matchScore"></div>
  <div class="match-board btn-hover">
    <div class="match-col btn-hover" id="matchEn"></div>
    <div class="match-col btn-hover" id="matchZh"></div>
  </div>
  <button class="reset-btn btn-hover" onclick="initMatch()">🔄 重新開始</button>
</div>

<!-- PAGE 3: SENTENCES + QUIZ -->
<div class="page btn-hover" id="page-2">
  <div class="page-title btn-hover"><span>✏️</span> 核心句型</div>
  <div class="page-sub btn-hover">換成你自己的資料試試看！</div>

{sent_html}
  <div class="game-label btn-hover" style="margin-top:22px">🧠 單字小測驗：看中文選英文</div>
  <div class="quiz-progress btn-hover" id="quizProgress"></div>
  <div class="quiz-question btn-hover">
    <div class="quiz-q btn-hover">這個中文是哪個英文單字？</div>
    <div class="quiz-en btn-hover" id="quizWord"></div>
  </div>
  <div class="quiz-status btn-hover" id="quizStatus"></div>
  <div class="quiz-choices btn-hover" id="quizChoices"></div>
  <button class="next-quiz-btn btn-hover" id="nextQuizBtn" onclick="nextQuiz()">下一題 →</button>
</div>

<!-- PAGE 4: QA PRACTICE -->
<div class="page btn-hover" id="page-3">
  <div class="page-title btn-hover"><span>🎯</span> 問答接力</div>
  <div class="page-sub btn-hover">10 分鐘 · 輪流問答，練習說英文</div>
{qa_html}
  <div class="tip-box btn-hover">{u["tip_box"]}</div>
</div>

<!-- PAGE 5: WRAP UP -->
<div class="page btn-hover" id="page-4">
  <div class="page-title btn-hover"><span>🎤</span> {u["wrapup_title"]}</div>
  <div class="page-sub btn-hover">{u["wrapup_sub"]}</div>
  <div class="intro-box btn-hover">
    {wrapup_lines_html}
  </div>
  <div class="star-tip btn-hover">{u["wrapup_tip"]}</div>
  <div class="task-card btn-hover" style="margin-bottom:0">
    <strong>最後挑戰：</strong><br>
    {wrapup_challenge_html}
  </div>

  <div class="complete-area btn-hover">
    <button class="complete-btn btn-hover" onclick="markDone()">✅ 完成本課！</button>
  </div>
  <div class="complete-done btn-hover" id="completeDone">
    <div class="big btn-hover">🎉</div>
    <h3>Unit {num} 完成！</h3>
    <p>{complete_next_text}</p>
    {home_btn}
  </div>
</div>

<!-- BOTTOM NAV -->
<div class="bottom-nav-outer btn-hover">
  <div class="bottom-nav btn-hover">
    <button class="nav-btn nav-prev btn-hover" id="prevBtn" onclick="changePage(-1)">← 上一步</button>
    <div class="nav-step-info btn-hover" id="stepInfo"></div>
    <button class="nav-btn nav-next btn-hover" id="nextBtn" onclick="changePage(1)">下一步 →</button>
  </div>
</div>

<script>
const UNIT_KEY = '{uid}';
const PROGRESS_KEY = 'progress_g4';
const steps = [
  {{ label: '暖身', icon: '🎵' }},
  {{ label: '單字', icon: '🃏' }},
  {{ label: '句型', icon: '✏️' }},
  {{ label: '練習', icon: '🎯' }},
  {{ label: '收尾', icon: '🎤' }},
];
const coreVocab = [
  {core_js}
];
const extVocab = [
  {ext_js}
];

(function() {{
  const p = JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{{}}');
  if (p[UNIT_KEY] !== 'done') {{ p[UNIT_KEY] = 'in_progress'; localStorage.setItem(PROGRESS_KEY, JSON.stringify(p)); }}
  else {{ document.getElementById('completeDone').style.display = 'block'; document.querySelector('.complete-btn').style.display = 'none'; }}
}})();

let currentPage = 0;
const stepNav = document.getElementById('stepNav');
steps.forEach((s, i) => {{
  const btn = document.createElement('button');
  btn.className = 'step-btn' + (i === 0 ? ' active' : '');
  btn.id = `step-${{i}}`;
  btn.innerHTML = `<span class="si btn-hover">${{s.icon}}</span>${{s.label}}`;
  btn.onclick = () => goTo(i);
  stepNav.appendChild(btn);
}});

function goTo(i) {{
  document.getElementById(`page-${{currentPage}}`).classList.remove('active');
  document.getElementById(`step-${{currentPage}}`).classList.remove('active');
  currentPage = i;
  document.getElementById(`page-${{i}}`).classList.add('active');
  document.getElementById(`step-${{i}}`).classList.add('active');
  updateNav();
  window.scrollTo(0, 0);
}}
function changePage(d) {{ goTo(currentPage + d); }}
function updateNav() {{
  document.getElementById('prevBtn').disabled = currentPage === 0;
  const nb = document.getElementById('nextBtn');
  nb.disabled = currentPage === steps.length - 1;
  nb.textContent = '下一步 →';
  document.getElementById('stepInfo').textContent = `${{currentPage + 1}} / ${{steps.length}}`;
}}
updateNav();

function makeCards(arr, gridId, isExt) {{
  const grid = document.getElementById(gridId);
  arr.forEach(v => {{
    const card = document.createElement('div');
    card.className = 'vocab-card';
    card.innerHTML = `<div class="vocab-inner btn-hover">
      <div class="vocab-front${{isExt?' ext':''}} btn-hover">
        <div class="en btn-hover">${{v.en}}</div>
        <button class="speak-btn btn-hover" onclick="event.stopPropagation();speak(\`${{v.en}}\`,this)">🔊</button>
      </div>
      <div class="vocab-back${{isExt?' ext':''}} btn-hover"><div class="zh btn-hover">${{v.zh}}</div><div class="en2 btn-hover">${{v.en}}</div></div>
    </div>`;
    card.addEventListener('click', () => card.classList.toggle('flipped'));
    grid.appendChild(card);
  }});
}}
makeCards(coreVocab, 'coreGrid', false);
makeCards(extVocab, 'extGrid', true);

let allFlipped = false;
function flipAll() {{
  allFlipped = !allFlipped;
  document.querySelectorAll('.vocab-card').forEach(c => c.classList.toggle('flipped', allFlipped));
}}

let matchSel = null, matchCorrect = 0;
function shuffle(a) {{ return [...a].sort(() => Math.random() - .5); }}
function initMatch() {{
  matchSel = null; matchCorrect = 0;
  document.getElementById('matchScore').textContent = '';
  const sub = shuffle(coreVocab).slice(0, 5);
  document.getElementById('matchEn').innerHTML = '';
  document.getElementById('matchZh').innerHTML = '';
  shuffle(sub).forEach(v => document.getElementById('matchEn').appendChild(makeMatchEl(v.en, 'en', v.en)));
  shuffle(sub).forEach(v => document.getElementById('matchZh').appendChild(makeMatchEl(v.zh, 'zh', v.en)));
}}
function makeMatchEl(text, side, key) {{
  const el = document.createElement('div');
  el.className = 'match-item'; el.textContent = text;
  el.dataset.key = key; el.dataset.side = side;
  el.addEventListener('click', () => onMatch(el));
  return el;
}}
function onMatch(el) {{
  if (el.classList.contains('correct')) return;
  if (!matchSel) {{ document.querySelectorAll('.match-item.selected').forEach(e=>e.classList.remove('selected')); el.classList.add('selected'); matchSel = el; return; }}
  if (matchSel === el) {{ el.classList.remove('selected'); matchSel = null; return; }}
  if (matchSel.dataset.side === el.dataset.side) {{ matchSel.classList.remove('selected'); matchSel = el; el.classList.add('selected'); return; }}
  if (matchSel.dataset.key === el.dataset.key) {{
    [matchSel, el].forEach(e => {{ e.classList.remove('selected'); e.classList.add('correct'); }});
    matchCorrect++;
    document.getElementById('matchScore').textContent = matchCorrect === 5 ? '🎉 全對！太厲害了！' : `✅ 答對 ${{matchCorrect}} 組`;
  }} else {{
    [matchSel, el].forEach(e => {{ e.classList.add('wrong'); setTimeout(()=>e.classList.remove('wrong','selected'),500); }});
  }}
  matchSel = null;
}}
initMatch();

let quizQueue = [], quizIdx = 0, quizAnswered = false;
function buildQuiz() {{ quizQueue = shuffle(coreVocab); quizIdx = 0; nextQuiz(); }}
function nextQuiz() {{
  if (quizIdx >= quizQueue.length) {{
    document.getElementById('quizWord').textContent = '🎉 全部完成！';
    document.getElementById('quizChoices').innerHTML = '';
    document.getElementById('quizStatus').textContent = '';
    document.getElementById('nextQuizBtn').style.display = 'none';
    document.getElementById('quizProgress').textContent = '';
    return;
  }}
  quizAnswered = false;
  const cur = quizQueue[quizIdx];
  document.getElementById('quizWord').textContent = cur.zh;
  document.getElementById('quizStatus').textContent = '';
  document.getElementById('nextQuizBtn').style.display = 'none';
  document.getElementById('quizProgress').textContent = `第 ${{quizIdx+1}} / ${{quizQueue.length}} 題`;
  const wrongs = shuffle(coreVocab.filter(v => v.en !== cur.en)).slice(0, 3);
  const choices = shuffle([cur, ...wrongs]);
  const cont = document.getElementById('quizChoices');
  cont.innerHTML = '';
  choices.forEach(c => {{
    const btn = document.createElement('button');
    btn.className = 'quiz-btn'; btn.textContent = c.en;
    btn.onclick = () => {{
      if (quizAnswered) return; quizAnswered = true;
      if (c.en === cur.en) {{ btn.classList.add('correct'); document.getElementById('quizStatus').textContent = '✅ 答對了！'; document.getElementById('quizStatus').style.color = '#4CAF50'; }}
      else {{ btn.classList.add('wrong'); cont.querySelectorAll('.quiz-btn').forEach(b=>{{if(b.textContent===cur.en)b.classList.add('correct');}}); document.getElementById('quizStatus').textContent = `❌ 答錯了，是 "${{cur.en}}"`; document.getElementById('quizStatus').style.color = '#f44336'; }}
      quizIdx++; document.getElementById('nextQuizBtn').style.display = 'block';
    }};
    cont.appendChild(btn);
  }});
}}
buildQuiz();


function markDone() {{
  const p = JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{{}}');
  p[UNIT_KEY] = 'done';
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(p));
  document.querySelector('.complete-btn').style.display = 'none';
  document.getElementById('completeDone').style.display = 'block';
}}
</script>
</body>
</html>"""
    return html


import os

out_dir = "./g4"
for u in UNITS:
    html = build_unit(u)
    path = os.path.join(out_dir, f"{u['id']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {path}")

print("Done! All 11 units generated.")
