  const API = 'http://localhost:4000/api';
  let currentLesson = null;
  let translationVisible = false;

  //  Load lessons from backend 
  async function loadLessons() {
    try {
      const res = await fetch(`${API}/lessons`);
      const lessons = await res.json();
      renderLessons(lessons);
    } catch (e) {
      document.getElementById('lessonsGrid').innerHTML =
        `<div class="lesson-card" style="border-color:#c0392b">
          <div class="lesson-title" style="color:#c0392b">Backend not running</div>
          <div class="lesson-meta">start: python main.py</div>
        </div>`;
    }
  }

  function renderLessons(lessons) {
    const grid = document.getElementById('lessonsGrid');
    grid.innerHTML = lessons.map(l => `
      <div class="lesson-card" id="card-${l.id}" onclick="selectLesson(${l.id}, this)">
        <div class="lesson-title">${l.title}</div>
        <div class="lesson-meta">${l.word_count} words</div>
      </div>
    `).join('');
  }

  //  Select a lesson 
  async function selectLesson(id, el) {
    document.querySelectorAll('.lesson-card').forEach(c => c.classList.remove('active'));
    el.classList.add('active');

    const res = await fetch(`${API}/lessons/${id}`);
    currentLesson = await res.json();

    document.getElementById('practiceLabel').textContent = `Lesson: ${currentLesson.title}`;
    document.getElementById('practiceArea').classList.add('visible');

    renderWordList(currentLesson.words);
    await nextWord();
  }

  //  Fetch a random word 
  async function nextWord() {
    if (!currentLesson) return;
    setStatus('');
    hideTranslation();

    const res = await fetch(`${API}/lessons/${currentLesson.id}/random`);
    const data = await res.json();

    document.getElementById('wordOriginal').textContent = data.word.dutch;
    document.getElementById('wordTranslation').textContent = data.word.english;
  }

  //  Show / hide translation 
  function revealTranslation() {
    const el = document.getElementById('wordTranslation');
    el.classList.remove('hidden');
    translationVisible = true;
  }

  function hideTranslation() {
    const el = document.getElementById('wordTranslation');
    el.classList.add('hidden');
    translationVisible = false;
  }

  //  Render full word list 
  function renderWordList(words) {
    const list = document.getElementById('wordList');
    list.innerHTML = `
      <div class="section-label" style="margin-bottom:12px">All words in this lesson</div>
      ${words.map(w => `
        <div class="word-row">
          <span class="w-nl">${w.dutch}</span>
          <span class="w-en">${w.english}</span>
        </div>
      `).join('')}
    `;
  }

  function setStatus(msg) {
    document.getElementById('status').textContent = msg;
  }

  //  Init 
  loadLessons();