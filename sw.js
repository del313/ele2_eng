const CACHE_NAME = 'ele2-eng-v1';
const ASSETS = [
  './',
  './index.html',
  './style-common.css',
  './style-unit.css',
  './js-common.js',
  './gk/kinder.js',
  './manifest.json'
];

// 安裝時快取資源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// 激活時清理舊快取
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.map(key => {
        if (key !== CACHE_NAME) return caches.delete(key);
      })
    ))
  );
});

// 攔截請求並優先從快取讀取 (Cache-First)
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
