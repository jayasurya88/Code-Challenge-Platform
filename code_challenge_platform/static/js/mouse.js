const dot = document.createElement('div');
dot.className = 'dot';
document.body.appendChild(dot);

let dotX = window.innerWidth / 2 - dot.clientWidth / 2;
let dotY = window.innerHeight / 2 - dot.clientHeight / 2;

let targetX = dotX;
let targetY = dotY;

const speed = 0.009;  // Even slower speed for smoother movement

const updatePosition = () => {
    const dx = targetX - dotX;
    const dy = targetY - dotY;
    
    dotX += dx * speed;
    dotY += dy * speed;

    dot.style.left = `${dotX}px`;
    dot.style.top = `${dotY}px`;

    requestAnimationFrame(updatePosition); // Continuously update the position
};

// Start the position update
updatePosition();

// Update the target position to follow the mouse
document.addEventListener('mousemove', (e) => {
    targetX = e.clientX - dot.clientWidth / 2;
    targetY = e.clientY - dot.clientHeight / 2;
});

// Blinking caret effect for the title
let titleText = 'DEVBIT_';
let caretVisible = true;
setInterval(() => {
  document.title = caretVisible ? titleText + '_' : titleText;
  caretVisible = !caretVisible;
}, 500); // Toggle the caret visibility every 500ms

document.addEventListener("DOMContentLoaded", () => {
  const body = document.querySelector('body');
  body.style.opacity = "0"; // Initially hide the page
  body.style.transition = "opacity 1.5s ease-in-out"; // Smooth transition
  body.style.opacity = "1"; // Fade in when DOM is fully loaded
});