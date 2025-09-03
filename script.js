const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

canvas.width = 600;
canvas.height = 200;

let dino = { x: 50, y: 150, width: 20, height: 20, dy: 0, jumping: false };
let gravity = 0.6;
let obstacles = [];
let frame = 0;
let gameOver = false;

function drawDino() {
  ctx.fillStyle = "green";
  ctx.fillRect(dino.x, dino.y, dino.width, dino.height);
}

function drawObstacles() {
  ctx.fillStyle = "red";
  obstacles.forEach(o => ctx.fillRect(o.x, o.y, o.width, o.height));
}

function update() {
  if (gameOver) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Dino jump
  dino.y += dino.dy;
  if (dino.y + dino.height < canvas.height) {
    dino.dy += gravity;
  } else {
    dino.y = canvas.height - dino.height;
    dino.dy = 0;
    dino.jumping = false;
  }

  // Obstacles
  if (frame % 90 === 0) {
    obstacles.push({ x: canvas.width, y: 180, width: 20, height: 20 });
  }
  obstacles.forEach(o => (o.x -= 3));
  obstacles = obstacles.filter(o => o.x + o.width > 0);

  // Collision
  obstacles.forEach(o => {
    if (
      dino.x < o.x + o.width &&
      dino.x + dino.width > o.x &&
      dino.y < o.y + o.height &&
      dino.y + dino.height > o.y
    ) {
      gameOver = true;
      alert("Game Over! Refresh to try again.");
    }
  });

  drawDino();
  drawObstacles();

  frame++;
  requestAnimationFrame(update);
}

function jump() {
  if (!dino.jumping) {
    dino.dy = -10;
    dino.jumping = true;
  }
}

document.addEventListener("keydown", e => {
  if (e.code === "Space") jump();
});

document.addEventListener("touchstart", jump);

update();
