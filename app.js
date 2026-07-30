// ===== 小潘工作台 - App Logic =====

// State
let currentSection = 'chinese';
let allData = {};
let mathTab = 'calculation';
let deleteMode = false;
let periodRecords = [];
let logicCustom = [];

// Constants
const PERIOD_KEY = 'xiaopan_period_records';
const LOGIC_CUSTOM_KEY = 'xiaopan_logic_custom';

// DOM
const contentArea = document.getElementById('contentArea');
const dateBadge = document.getElementById('dateBadge');
const toast = document.getElementById('toast');
const modalOverlay = document.getElementById('modalOverlay');
const modalTitle = document.getElementById('modalTitle');
const modalBody = document.getElementById('modalBody');
const addTaskBtn = document.getElementById('addTaskBtn');
const deleteTaskBtn = document.getElementById('deleteTaskBtn');

// ===== Init =====
document.addEventListener('DOMContentLoaded', () => {
  updateDateBadge();
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => switchSection(item.dataset.section));
  });
  loadPeriodRecords();
  loadLogicCustom();
  loadAllData();
});

function updateDateBadge() {
  const now = new Date();
  const days = ['日','一','二','三','四','五','六'];
  dateBadge.textContent = (now.getMonth()+1) + '/' + now.getDate() + ' 周' + days[now.getDay()];
}

function getDayOfYear() {
  const now = new Date();
  const start = new Date(now.getFullYear(), 0, 0);
  return Math.floor((now - start) / 86400000);
}

// ===== Load Data =====
async function loadAllData() {
  const files = ['poems', 'idioms', 'characters', 'math', 'logic', 'hotboard'];
  for (const name of files) {
    try {
      const resp = await fetch('data/' + name + '.json?' + Date.now(), { cache: 'no-store' });
      if (resp.ok) allData[name] = await resp.json();
    } catch (e) { console.warn('Failed to load ' + name, e); }
  }
  renderSection(currentSection);
}

function refreshAll() {
  showToast('刷新中...');
  loadAllData().then(() => showToast('已刷新'));
}

// ===== Switch Section =====
function switchSection(section) {
  currentSection = section;
  document.querySelectorAll('.nav-item').forEach(item => {
    item.classList.toggle('active', item.dataset.section === section);
  });
  var showAddDelete = (section === 'logic');
  addTaskBtn.style.display = showAddDelete ? '' : 'none';
  deleteTaskBtn.style.display = showAddDelete ? '' : 'none';
  if (deleteMode && !showAddDelete) deleteMode = false;
  renderSection(section);
}

function renderSection(section) {
  contentArea.innerHTML = '';
  switch (section) {
    case 'chinese': renderChinese(); break;
    case 'math': renderMath(); break;
    case 'logic': renderLogic(); break;
    case 'inspiration': renderInspiration(); break;
    case 'period': renderPeriod(); break;
  }
}

// ===== 语文 =====
function renderChinese() {
  var dayIdx = getDayOfYear();
  var poems = (allData.poems && allData.poems.poems) || [];
  var poem = poems.length > 0 ? poems[dayIdx % poems.length] : null;
  var idioms = (allData.idioms && allData.idioms.idioms) || [];
  var idiom = idioms.length > 0 ? idioms[dayIdx % idioms.length] : null;
  var chars = (allData.characters && allData.characters.characters) || [];
  var startIdx = (dayIdx * 10) % Math.max(1, chars.length);
  var todayChars = chars.slice(startIdx, startIdx + 10);
  if (todayChars.length < 10 && chars.length >= 10) todayChars = todayChars.concat(chars.slice(0, 10 - todayChars.length));

  var html = '<div class="theme-chinese" style="min-height:100%;border-radius:0;padding:0;">';
  html += '<h2 class="section-header">📚 语文<span class="section-badge">每日更新</span></h2>';

  if (poem) {
    html += '<div class="card poem-card">' +
      '<div class="card-title">📜 每日古诗</div>' +
      '<div style="text-align:center;margin-bottom:6px;">' +
      '<strong style="font-size:1.05rem;">' + poem.title + '</strong>' +
      '<span style="font-size:0.78rem;color:#999;margin-left:8px;">[' + poem.dynasty + '] ' + poem.author + '</span></div>' +
      '<div class="poem-content">' + poem.content + '</div>' +
      '<div class="card-pinyin">' + poem.pinyin + '</div>' +
      '<div style="font-size:0.8rem;color:#666;margin-top:8px;line-height:1.7;"><strong>释义：</strong>' + poem.meaning + '</div></div>';
  }

  if (idiom) {
    html += '<div class="card" style="border-left:3px solid #F48FB1;">' +
      '<div class="card-title">📖 成语故事</div>' +
      '<div style="font-size:1.1rem;font-weight:700;text-align:center;margin:8px 0;">' + idiom.name +
      '<span style="font-size:0.75rem;color:#F06292;font-weight:400;"> ' + idiom.pinyin + '</span></div>' +
      '<div style="font-size:0.82rem;color:#555;margin-bottom:6px;"><strong>释义：</strong>' + idiom.meaning + '</div>' +
      '<div class="idiom-story"><strong>故事：</strong>' + idiom.story + '</div></div>';
  }

  if (todayChars.length > 0) {
    html += '<div class="card"><div class="card-title">✏️ 每日识字 <span style="font-size:0.75rem;color:#999;font-weight:400;">10个字</span></div><div class="char-grid">';
    todayChars.forEach(function(c) {
      html += '<div class="char-item"><div class="char-big">' + c.char + '</div>' +
        '<div class="char-py">' + c.pinyin + '</div><div class="char-word">' + c.word + '</div>' +
        '<div class="char-sentence">' + c.sentence + '</div></div>';
    });
    html += '</div></div>';
  }

  // 拼音表
  html += '<div class="card"><div class="card-title">🔤 拼音表</div>';
  html += '<div class="pinyin-table">';

  // 声母
  html += '<div class="pinyin-group"><div class="pinyin-group-title">声母（23个）</div><div class="pinyin-items">';
  var initials = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s','y','w'];
  initials.forEach(function(s) { html += '<span class="pinyin-chip initial">' + s + '</span>'; });
  html += '</div></div>';

  // 韵母
  html += '<div class="pinyin-group"><div class="pinyin-group-title">韵母</div>';
  
  html += '<div class="pinyin-subgroup"><span class="pinyin-subtitle">单韵母（6个）</span>';
  var singles = ['a','o','e','i','u','ü'];
  singles.forEach(function(s) { html += '<span class="pinyin-chip final-single">' + s + '</span>'; });
  html += '</div>';

  html += '<div class="pinyin-subgroup"><span class="pinyin-subtitle">复韵母（8个）</span>';
  var compounds = ['ai','ei','ui','ao','ou','iu','ie','üe'];
  compounds.forEach(function(s) { html += '<span class="pinyin-chip final-compound">' + s + '</span>'; });
  html += '</div>';

  html += '<div class="pinyin-subgroup"><span class="pinyin-subtitle">特殊韵母（1个）</span>';
  html += '<span class="pinyin-chip final-special">er</span>';
  html += '</div>';

  html += '<div class="pinyin-subgroup"><span class="pinyin-subtitle">前鼻韵母（5个）</span>';
  var frontNasals = ['an','en','in','un','ün'];
  frontNasals.forEach(function(s) { html += '<span class="pinyin-chip final-nasal">' + s + '</span>'; });
  html += '</div>';

  html += '<div class="pinyin-subgroup"><span class="pinyin-subtitle">后鼻韵母（4个）</span>';
  var backNasals = ['ang','eng','ing','ong'];
  backNasals.forEach(function(s) { html += '<span class="pinyin-chip final-nasal">' + s + '</span>'; });
  html += '</div>';

  html += '</div>'; // 韵母 end

  // 整体认读音节
  html += '<div class="pinyin-group"><div class="pinyin-group-title">整体认读音节（16个）</div><div class="pinyin-items">';
  var wholeSyllables = ['zhi','chi','shi','ri','zi','ci','si','yi','wu','yu','ye','yue','yuan','yin','yun','ying'];
  wholeSyllables.forEach(function(s) { html += '<span class="pinyin-chip whole">' + s + '</span>'; });
  html += '</div></div>';

  html += '</div></div>'; // pinyin-table end

  html += '</div>';
  contentArea.innerHTML = html;
}

// ===== 数学 =====
function renderMath() {
  var math = allData.math || {};
  var dayIdx = getDayOfYear();
  var html = '<div class="theme-math" style="min-height:100%;border-radius:0;padding:0;">';
  html += '<h2 class="section-header">🔢 数学<span class="section-badge">每日练习</span></h2>';

  html += '<div class="math-tab">' +
    '<button class="math-tab-btn ' + (mathTab==='counting'?'active':'') + '" onclick="switchMathTab(\'counting\')">数数题</button>' +
    '<button class="math-tab-btn ' + (mathTab==='calculation'?'active':'') + '" onclick="switchMathTab(\'calculation\')">计算题</button>' +
    '<button class="math-tab-btn ' + (mathTab==='number_sense'?'active':'') + '" onclick="switchMathTab(\'number_sense\')">数感星球</button>' +
    '<button class="math-tab-btn ' + (mathTab==='thinking'?'active':'') + '" onclick="switchMathTab(\'thinking\')">思维练习</button></div>';

  var questions = math[mathTab] || [];
  var daily = [];
  if (questions.length > 0) {
    var start = (dayIdx * 10) % questions.length;
    daily = questions.slice(start, start + 10);
    if (daily.length < 10) daily = daily.concat(questions.slice(0, 10 - daily.length));
  }

  daily.forEach(function(q, i) {
    var qid = 'math-q' + i;
    html += '<div class="card"><div class="card-subtitle">第 ' + (i+1) + ' 题</div>';
    if (q.visual) html += '<div class="math-visual">' + q.visual + '</div>';
    html += '<div class="math-question">' + q.question + '</div><div class="math-options" id="' + qid + '">';
    q.options.forEach(function(opt, j) {
      var btnId = qid + '-opt' + j;
      html += '<button class="math-opt" id="' + btnId + '" onclick="checkMath(\'' + qid + '\',' + j + ',' + q.answer + ',\'' + btnId + '\')">' + opt + '</button>';
    });
    html += '</div></div>';
  });

  if (daily.length === 0) html += '<div class="card"><p style="text-align:center;color:#999;">暂无题目</p></div>';
  html += '</div>';
  contentArea.innerHTML = html;
}

function switchMathTab(tab) { mathTab = tab; renderMath(); }

function checkMath(qid, selected, answer, btnId) {
  var container = document.getElementById(qid);
  var buttons = container.querySelectorAll('.math-opt');
  buttons.forEach(function(b) { b.style.pointerEvents = 'none'; });
  var btn = document.getElementById(btnId);
  // answer 是正确选项的值，需要通过值找索引
  var correctIdx = -1;
  buttons.forEach(function(b, idx) {
    if (b.textContent.trim() == String(answer)) correctIdx = idx;
  });
  if (selected === correctIdx) { btn.classList.add('correct'); showToast('✅ 答对了！'); }
  else {
    btn.classList.add('wrong');
    if (correctIdx >= 0 && buttons[correctIdx]) buttons[correctIdx].classList.add('correct');
    showToast('❌ 再试试');
  }
}

// ===== 逻辑思维 =====
function renderLogic() {
  var builtIn = (allData.logic && allData.logic.questions) || [];
  var all = builtIn.concat(logicCustom);
  var dayIdx = getDayOfYear();
  var daily = [];
  if (all.length > 0) {
    var start = (dayIdx * 10) % all.length;
    daily = all.slice(start, start + 10);
    if (daily.length < 10) daily = daily.concat(all.slice(0, 10 - daily.length));
  }

  var html = '<div class="theme-logic" style="min-height:100%;border-radius:0;padding:0;">';
  html += '<h2 class="section-header">🧩 逻辑思维<span class="section-badge">每日10题</span></h2>';
  if (deleteMode) html += '<div style="font-size:0.8rem;color:#EF5350;margin-bottom:8px;text-align:center;">删除模式：点击右上角 × 删除</div>';

  daily.forEach(function(q, i) {
    var qid = 'logic-q' + i;
    var isCustom = q.custom === true;
    html += '<div class="card logic-card ' + (deleteMode?'delete-mode':'') + '">';
    if (isCustom) html += '<span class="delete-btn" onclick="deleteLogicQuestion(' + (q.id || -1) + ',this)">×</span>';
    html += '<span class="logic-cat">' + (q.category || '逻辑') + '</span>';
    html += '<div class="logic-q">第 ' + (i+1) + ' 题：' + q.question + '</div>';
    html += '<div class="logic-opts" id="' + qid + '">';
    q.options.forEach(function(opt, j) {
      var btnId = qid + '-opt' + j;
      html += '<button class="logic-opt" id="' + btnId + '" onclick="checkLogic(\'' + qid + '\',' + j + ',' + q.answer + ',\'' + btnId + '\')">' + opt + '</button>';
    });
    html += '</div><div class="logic-explain" id="' + qid + '-explain">' + (q.explanation || '') + '</div></div>';
  });

  if (daily.length === 0) html += '<div class="card"><p class="empty-tip">暂无题目，点击底部「新增」添加</p></div>';
  html += '</div>';
  contentArea.innerHTML = html;
}

function checkLogic(qid, selected, answer, btnId) {
  var container = document.getElementById(qid);
  var buttons = container.querySelectorAll('.logic-opt');
  buttons.forEach(function(b) { b.style.pointerEvents = 'none'; });
  var btn = document.getElementById(btnId);
  // answer 可能是索引也可能是值，统一通过值匹配
  var correctIdx = -1;
  if (typeof answer === 'number' && answer >= 0 && answer < buttons.length) {
    correctIdx = answer;
  } else {
    buttons.forEach(function(b, idx) {
      if (b.textContent.trim() == String(answer)) correctIdx = idx;
    });
  }
  if (selected === correctIdx) { btn.classList.add('correct'); showToast('✅ 答对了！'); }
  else {
    btn.classList.add('wrong');
    if (correctIdx >= 0 && buttons[correctIdx]) buttons[correctIdx].classList.add('correct');
    showToast('❌ 答错了');
  }
  var explain = document.getElementById(qid + '-explain');
  if (explain) explain.classList.add('show');
}

// Logic CRUD
function loadLogicCustom() {
  try { var s = localStorage.getItem(LOGIC_CUSTOM_KEY); logicCustom = s ? JSON.parse(s) : []; } catch(e) { logicCustom = []; }
}
function saveLogicCustom() { try { localStorage.setItem(LOGIC_CUSTOM_KEY, JSON.stringify(logicCustom)); } catch(e) {} }
function toggleDeleteMode() { deleteMode = !deleteMode; deleteTaskBtn.style.background = deleteMode ? '#FFCDD2' : ''; renderLogic(); }
function deleteLogicQuestion(id, btn) {
  if (!confirm('确定删除？')) return;
  logicCustom = logicCustom.filter(function(q) { return q.id !== id; });
  saveLogicCustom(); renderLogic(); showToast('已删除');
}
function showAddTask() {
  if (currentSection === 'logic') showAddLogicModal();
  else showToast('该板块暂不支持新增');
}
function showAddLogicModal() {
  modalTitle.textContent = '新增逻辑题';
  modalBody.innerHTML = '<label>分类</label><select id="newLogicCat"><option value="分类">分类</option><option value="排序">排序</option><option value="推理">推理</option><option value="找不同">找不同</option></select>' +
    '<label>题目</label><textarea id="newLogicQ" placeholder="输入题目"></textarea>' +
    '<label>选项（每行一个，正确答案放第一个）</label><textarea id="newLogicOpts" placeholder="选项A\n选项B\n选项C\n选项D"></textarea>' +
    '<label>解析</label><textarea id="newLogicExplain" placeholder="输入解析"></textarea>';
  modalOverlay.classList.remove('hidden');
}
function saveTask() {
  if (currentSection !== 'logic') return;
  var cat = document.getElementById('newLogicCat').value;
  var q = document.getElementById('newLogicQ').value.trim();
  var optsText = document.getElementById('newLogicOpts').value.trim();
  var explain = document.getElementById('newLogicExplain').value.trim();
  if (!q || !optsText) { showToast('请填写题目和选项'); return; }
  var opts = optsText.split('\n').filter(function(o) { return o.trim(); });
  if (opts.length < 2) { showToast('至少需要2个选项'); return; }
  logicCustom.push({ id: Date.now(), type: 'custom', category: cat, question: q, options: opts, answer: 0, explanation: explain, custom: true });
  saveLogicCustom(); closeModal(); renderLogic(); showToast('已添加');
}
function closeModal() { modalOverlay.classList.add('hidden'); }

// ===== 创作灵感 =====
function renderInspiration() {
  var hb = allData.hotboard || {};
  var hot = hb.hotTopics || [];
  var insp = hb.inspiration || { ideas: [], remix: [] };
  var html = '<div class="theme-inspiration" style="min-height:100%;border-radius:0;padding:0;">';
  html += '<h2 class="section-header">💡 创作灵感<span class="section-badge">每日更新</span></h2>';

  html += '<div class="card"><div class="card-title">🔥 今日热榜</div><div>';
  hot.forEach(function(t, i) {
    var url = 'https://www.douyin.com/search/' + encodeURIComponent(t.title);
    html += '<a href="' + url + '" target="_blank" style="text-decoration:none;"><span class="hot-tag"><span class="rank">' + (i+1) + '</span>' + t.title + '</span></a>';
  });
  html += '</div></div>';

  if (insp.ideas && insp.ideas.length > 0) {
    html += '<div class="card"><div class="card-title">💡 选题灵感</div>';
    insp.ideas.forEach(function(item) {
      var url = 'https://www.douyin.com/search/' + encodeURIComponent(item.title);
      html += '<div class="idea-card"><div class="idea-title">' + item.title + '</div><div class="idea-desc">' + item.desc + '</div><a class="douyin-link" href="' + url + '" target="_blank">👉 在抖音查看</a></div>';
    });
    html += '</div>';
  }

  if (insp.remix && insp.remix.length > 0) {
    html += '<div class="card"><div class="card-title">🎬 二创角度</div>';
    insp.remix.forEach(function(item) {
      html += '<div class="idea-card" style="border-left-color:#FFB74D;"><div class="idea-title">' + item.title + '</div><div class="idea-desc">' + item.desc + '</div></div>';
    });
    html += '</div>';
  }

  html += '</div>';
  contentArea.innerHTML = html;
}

// ===== 经期记录 =====
function loadPeriodRecords() { try { var s = localStorage.getItem(PERIOD_KEY); periodRecords = s ? JSON.parse(s) : []; } catch(e) { periodRecords = []; } }
function savePeriodRecords() { try { localStorage.setItem(PERIOD_KEY, JSON.stringify(periodRecords)); } catch(e) {} }
function parseDate(s) { var p = s.split('-').map(Number); return new Date(p[0], p[1]-1, p[2]); }
function formatDate(d) { return d.getFullYear() + '-' + String(d.getMonth()+1).padStart(2,'0') + '-' + String(d.getDate()).padStart(2,'0'); }
function dateDiff(a, b) { var am = new Date(a.getFullYear(),a.getMonth(),a.getDate()); var bm = new Date(b.getFullYear(),b.getMonth(),b.getDate()); return Math.round((am-bm)/86400000); }
function addDays(d, n) { var r = new Date(d); r.setDate(r.getDate()+n); return r; }

function getAvgCycle() {
  if (periodRecords.length < 2) return 28;
  var sorted = periodRecords.slice().sort(function(a,b) { return parseDate(a.startDate) - parseDate(b.startDate); });
  var cycles = [];
  for (var i = 1; i < sorted.length; i++) {
    var diff = dateDiff(parseDate(sorted[i].startDate), parseDate(sorted[i-1].startDate));
    if (diff > 14 && diff < 60) cycles.push(diff);
  }
  return cycles.length ? Math.round(cycles.reduce(function(a,b){return a+b;},0)/cycles.length) : 28;
}
function getLastPeriod() {
  if (!periodRecords.length) return null;
  return periodRecords.slice().sort(function(a,b) { return parseDate(b.startDate) - parseDate(a.startDate); })[0];
}
function getCurrentPhase() {
  var last = getLastPeriod();
  if (!last) return { phase: '未记录', day: 0 };
  var start = parseDate(last.startDate);
  var today = new Date();
  var days = dateDiff(today, start) + 1;
  var cycle = getAvgCycle();
  if (days < 1) return { phase: '经期前', day: 0 };
  if (days <= 5) return { phase: '经期中', day: days };
  var ov = cycle - 14;
  if (Math.abs(days - ov) <= 2) return { phase: '排卵期', day: days };
  if (days < ov) return { phase: '卵泡期', day: days };
  if (days < cycle) return { phase: '黄体期', day: days };
  return { phase: '周期外', day: days };
}

function renderPeriod() {
  var phase = getCurrentPhase();
  var last = getLastPeriod();
  var next = last ? addDays(parseDate(last.startDate), getAvgCycle()) : null;
  var ov = next ? addDays(next, -14) : null;

  var html = '<div class="theme-period" style="min-height:100%;border-radius:0;padding:0;">';
  html += '<h2 class="section-header">🌷 经期记录</h2>';

  html += '<div class="period-status"><div class="period-ring"><div class="period-day">' + (phase.day > 0 ? phase.day : '-') + '</div><div class="period-phase">' + phase.phase + '</div></div>';
  html += '<div class="period-info"><p class="period-next">' + (next ? '下次经期：' + formatDate(next) : '点击下方开始记录') + '</p>';
  html += '<p class="period-symptoms">' + (ov ? '排卵期：' + formatDate(ov) : '') + (last ? ' | 上次：' + last.startDate : '') + '</p></div></div>';

  html += '<div class="period-actions"><button class="btn-period" onclick="startPeriod()">今天经期开始</button><button class="btn-period btn-period-light" onclick="endPeriod()">今天经期结束</button></div>';

  html += '<div class="card" style="background:white;"><div class="card-subtitle">自定义记录</div><div class="period-form"><input type="date" id="periodDateInput" /><input type="text" id="periodNoteInput" placeholder="备注" /><button class="btn-small" onclick="addCustomPeriod()">添加</button></div></div>';

  html += '<div class="card" style="background:white;"><div class="card-subtitle">历史记录</div>';
  if (periodRecords.length === 0) html += '<p class="empty-tip">暂无记录</p>';
  else {
    var sorted = periodRecords.slice().sort(function(a,b) { return parseDate(b.startDate) - parseDate(a.startDate); });
    sorted.forEach(function(r) {
      var days = dateDiff(new Date(), parseDate(r.startDate));
      var timeText = days === 0 ? '今天' : days === 1 ? '昨天' : days < 7 ? days+'天前' : days < 30 ? Math.floor(days/7)+'周前' : Math.floor(days/30)+'月前';
      html += '<div class="period-item"><span style="font-weight:600;color:#8C6B4A;">' + r.startDate + '</span><span style="color:#777;flex:1;margin:0 8px;">' + (r.note||'') + ' (' + timeText + ')</span><button class="period-item-del" onclick="deletePeriod(\'' + r.startDate + '\')">×</button></div>';
    });
  }
  html += '</div></div>';
  contentArea.innerHTML = html;

  var dateInput = document.getElementById('periodDateInput');
  if (dateInput) { dateInput.value = formatDate(new Date()); dateInput.max = formatDate(new Date()); }
}

function startPeriod() {
  var today = formatDate(new Date());
  if (periodRecords.find(function(r) { return r.startDate === today; })) { showToast('今天已记录'); return; }
  periodRecords.push({ startDate: today, note: '经期开始', createdAt: new Date().toISOString() });
  savePeriodRecords(); renderPeriod(); showToast('已记录经期开始');
}
function endPeriod() {
  var last = getLastPeriod();
  if (!last) { showToast('请先记录开始'); return; }
  last.endDate = formatDate(new Date()); savePeriodRecords(); renderPeriod(); showToast('已记录经期结束');
}
function addCustomPeriod() {
  var date = document.getElementById('periodDateInput').value;
  var note = document.getElementById('periodNoteInput').value.trim();
  if (!date) { showToast('请选择日期'); return; }
  if (parseDate(date) > new Date()) { showToast('不能选未来'); return; }
  if (periodRecords.find(function(r) { return r.startDate === date; })) { showToast('该日期已记录'); return; }
  periodRecords.push({ startDate: date, note: note || '经期', createdAt: new Date().toISOString() });
  savePeriodRecords(); renderPeriod(); showToast('已添加');
}
function deletePeriod(date) {
  if (!confirm('确定删除？')) return;
  periodRecords = periodRecords.filter(function(r) { return r.startDate !== date; });
  savePeriodRecords(); renderPeriod(); showToast('已删除');
}

// ===== Utils =====
function showToast(msg) {
  toast.textContent = msg; toast.classList.add('show');
  clearTimeout(toast._t); toast._t = setTimeout(function() { toast.classList.remove('show'); }, 2000);
}
function openDouyin(e) {
  var isIOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
  if (!isIOS) {
    e.preventDefault(); var start = Date.now();
    window.location.href = 'snssdk1128://';
    setTimeout(function() { if (Date.now()-start < 2500) window.location.href = 'https://www.douyin.com'; }, 2000);
  }
}
