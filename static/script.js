const noBtn = document.getElementById('noBtn');
const yesBtn = document.getElementById('yesBtn');
const btnRow = document.getElementById('btnRow');
const content = document.getElementById('content');
const card = document.getElementById('card');

let followUps = [];
let step = 0;

async function loadFollowUps() {
  const res = await fetch('/api/followups');
  followUps = await res.json();
}
loadFollowUps();

function moveNoButton() {
  const rect = card.getBoundingClientRect();
  const maxX = rect.width - 120;
  const x = Math.floor(Math.random() * Math.max(40, maxX));
  const y = Math.floor(Math.random() * 100);

  noBtn.style.position = 'absolute';
  noBtn.style.left = `${x}px`;
  noBtn.style.top = `${y + 80}px`;
}

noBtn.addEventListener('mouseenter', async () => {
  moveNoButton();
  const res = await fetch('/api/no-message');
  const data = await res.json();
  noBtn.textContent = data.message;
});
noBtn.addEventListener('click', moveNoButton);

yesBtn.addEventListener('click', () => {
  if (!followUps.length) return;
  if (step < followUps.length) {
    const q = followUps[step];
    content.innerHTML = `<h3>${q.q}</h3>` + q.options.map(o => `<button class="btn yes opt">${o}</button>`).join(' ');
    document.querySelectorAll('.opt').forEach(btn => btn.onclick = () => {
      step++;
      if (step === followUps.length) {
        content.innerHTML = `<div class="popup"><h2>Yay!!! 🎉💞</h2><p>You made me the happiest! 🥰</p></div>`;
      } else {
        yesBtn.click();
      }
    });
  }
});
