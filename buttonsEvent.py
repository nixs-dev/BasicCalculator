from CalcSolver import CalcSolver


def button1Clicked(window):
	window.inputText.setText(window.inputText.text() + '1')

def button2Clicked(window):
	window.inputText.setText(window.inputText.text() + '2')

def button3Clicked(window):
	window.inputText.setText(window.inputText.text() + '3')

def button4Clicked(window):
	window.inputText.setText(window.inputText.text() + '4')

def button5Clicked(window):
	window.inputText.setText(window.inputText.text() + '5')

def button6Clicked(window):
	window.inputText.setText(window.inputText.text() + '6')

def button7Clicked(window):
	window.inputText.setText(window.inputText.text() + '7')

def button8Clicked(window):
	window.inputText.setText(window.inputText.text() + '8')

def button9Clicked(window):
	window.inputText.setText(window.inputText.text() + '9')

def button0Clicked(window):
	window.inputText.setText(window.inputText.text() + '0')

def buttonSumClicked(window):
	window.inputText.setText(window.inputText.text() + '+')

def buttonSubClicked(window):
	window.inputText.setText(window.inputText.text() + '-')

def buttonMultClicked(window):
	window.inputText.setText(window.inputText.text() + 'x')

def buttonDivClicked(window):
	window.inputText.setText(window.inputText.text() + '/')

def buttonDotClicked(window):
	window.inputText.setText(window.inputText.text() + '.')

def buttonEnterClicked(window):
	calc = window.inputText.text()
	result = CalcSolver(calc).solve()
	window.inputText.setText(str(result[0]))