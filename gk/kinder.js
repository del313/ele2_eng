const PROGRESS_KEY = 'progress_kinder';

const unit1Data = {
  id: 'unit1',
  title: 'Letters A-D',
  videoUrl: 'https://www.youtube.com/watch?v=75p-N9YKqNo',
  items: [
    { letter: 'A', word: 'Apple', icon: '🍎' },
    { letter: 'B', word: 'Bear', icon: '🐻' },
    { letter: 'C', word: 'Cat', icon: '🐱' },
    { letter: 'D', word: 'Dog', icon: '🐶' }
  ]
};

const unit2Data = {
  id: 'unit2',
  title: 'Numbers 1-10',
  vocab: [
    { word: 'One', icon: '1️⃣' },
    { word: 'Two', icon: '2️⃣' },
    { word: 'Three', icon: '3️⃣' },
    { word: 'Four', icon: '4️⃣' },
    { word: 'Five', icon: '5️⃣' },
    { word: 'Six', icon: '6️⃣' }
  ],
  speakLines: ['One, two, three.', 'Four, five, six.', 'I can count.']
};

const unit3Data = {
  id: 'unit3',
  title: 'Colors',
  vocab: [
    { word: 'Red', icon: '🔴' },
    { word: 'Blue', icon: '🔵' },
    { word: 'Yellow', icon: '🟡' },
    { word: 'Green', icon: '🟢' },
    { word: 'Pink', icon: '🩷' },
    { word: 'Black', icon: '⚫' }
  ],
  speakLines: ['I like red.', 'Blue is pretty.', 'Colors are fun.']
};

const unit4Data = {
  id: 'unit4',
  title: 'Animals',
  vocab: [
    { word: 'Cat', icon: '🐱' },
    { word: 'Dog', icon: '🐶' },
    { word: 'Bird', icon: '🐦' },
    { word: 'Fish', icon: '🐟' },
    { word: 'Duck', icon: '🦆' },
    { word: 'Rabbit', icon: '🐰' }
  ],
  speakLines: ['This is a cat.', 'That is a dog.', 'I love animals.']
};

const unit5Data = {
  id: 'unit5',
  title: 'Family',
  vocab: [
    { word: 'Dad', icon: '👨' },
    { word: 'Mom', icon: '👩' },
    { word: 'Brother', icon: '👦' },
    { word: 'Sister', icon: '👧' },
    { word: 'Grandpa', icon: '👴' },
    { word: 'Grandma', icon: '👵' }
  ],
  speakLines: ['This is my dad.', 'This is my mom.', 'I love my family.']
};

const unit6Data = {
  id: 'unit6',
  title: 'Food',
  vocab: [
    { word: 'Apple', icon: '🍎' },
    { word: 'Banana', icon: '🍌' },
    { word: 'Bread', icon: '🍞' },
    { word: 'Rice', icon: '🍚' },
    { word: 'Milk', icon: '🥛' },
    { word: 'Egg', icon: '🥚' }
  ],
  speakLines: ['I like apples.', 'I drink milk.', 'Food is yummy.']
};

const unit7Data = {
  id: 'unit7',
  title: 'Body Parts',
  vocab: [
    { word: 'Head', icon: '🙂' },
    { word: 'Eyes', icon: '👀' },
    { word: 'Nose', icon: '👃' },
    { word: 'Mouth', icon: '👄' },
    { word: 'Hands', icon: '🖐️' },
    { word: 'Feet', icon: '🦶' }
  ],
  speakLines: ['Touch your head.', 'Clap your hands.', 'Stamp your feet.']
};

const unit8Data = {
  id: 'unit8',
  title: 'Daily Actions',
  vocab: [
    { word: 'Run', icon: '🏃' },
    { word: 'Jump', icon: '🦘' },
    { word: 'Eat', icon: '🍽️' },
    { word: 'Sleep', icon: '😴' },
    { word: 'Read', icon: '📖' },
    { word: 'Sing', icon: '🎤' }
  ],
  speakLines: ['I can run.', 'I can jump.', 'I can sing.']
};

const unitsMeta = [
  { id: 'unit1', title: 'ABC & Sounds', icon: '🔤' },
  { id: 'unit2', title: 'Numbers 1-10', icon: '🔢' },
  { id: 'unit3', title: 'Colors', icon: '🎨' },
  { id: 'unit4', title: 'Animals', icon: '🐾' },
  { id: 'unit5', title: 'Family', icon: '👨‍👩‍👧' },
  { id: 'unit6', title: 'Food', icon: '🍎' },
  { id: 'unit7', title: 'Body Parts', icon: '🖐️' },
  { id: 'unit8', title: 'Daily Actions', icon: '🏃' }
];

const gamesMeta = [
  { id: 'game1', title: '氣球快手', icon: '🎈' },
  { id: 'game2', title: '對對碰', icon: '🎴' },
  { id: 'game3', title: '單字敲敲樂', icon: '🔨' },
  { id: 'game4', title: '影子拼圖', icon: '🧩' },
  { id: 'game5', title: '單字轉盤', icon: '🎡' },
  { id: 'game6', title: '字母接接樂', icon: '🧺' },
  { id: 'game7', title: '圖片拼拼看', icon: '🖼️' },
  { id: 'game8', title: '終極挑戰', icon: '👑' }
];

const unitDataMap = {
  unit1: unit1Data,
  unit2: unit2Data,
  unit3: unit3Data,
  unit4: unit4Data,
  unit5: unit5Data,
  unit6: unit6Data,
  unit7: unit7Data,
  unit8: unit8Data
};

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
  } catch (e) {
    return {};
  }
}

function saveProgress(progress) {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
}

function setProgress(id, state) {
  const p = loadProgress();
  p[id] = state;
  saveProgress(p);
}

function speakText(text) {
  if (!('speechSynthesis' in window)) {
    return;
  }
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US';
  u.rate = 0.9;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(u);
}

function playSound(type) {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    const now = ctx.currentTime;
    if (type === 'success') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(500, now);
      osc.frequency.exponentialRampToValueAtTime(1000, now + 0.1);
      gain.gain.setValueAtTime(0.1, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
      osc.start(now);
      osc.stop(now + 0.3);
    } else if (type === 'error') {
      osc.type = 'square';
      osc.frequency.setValueAtTime(150, now);
      osc.frequency.exponentialRampToValueAtTime(100, now + 0.1);
      gain.gain.setValueAtTime(0.05, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
      osc.start(now);
      osc.stop(now + 0.2);
    }
  } catch (e) {
    console.error("AudioContext error:", e);
  }
}

function shuffle(arr) {
  const next = arr.slice();
  for (let i = next.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const t = next[i];
    next[i] = next[j];
    next[j] = t;
  }
  return next;
}
