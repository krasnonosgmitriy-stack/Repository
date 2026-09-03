const button = document.getElementById("changeColorButton");

button.addEventListener("click", function () {
const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
document.body.style.backgroundColor = randomColor;
});


function greet(name) {
    return `Hello, ${name}!`;
}

console.log(gpeet("Alice")); // Виведе: Hello, Alice!