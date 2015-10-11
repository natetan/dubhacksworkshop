var numOne = document.getElementById("num1");
var numTwo = document.getElementById("num2");
var addSum = document.getElementById("sum");

numOne.addEventListener("input", add);
numTwo.addEventListener("input", add);

function add() {
	var one = parseFloat(numOne.value) || 0;
	var two = parseFloat(numTwo.value) || 0;
	var sum = one + two;
	addSum.innerHTML = "Your sum is " + sum;
}