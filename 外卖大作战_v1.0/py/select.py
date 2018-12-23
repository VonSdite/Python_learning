import easygui as e

def choice_people():
	msg = "\n\n\t\t( ‵▽′)ψ  谁叫了外卖"
	title = "外卖大作战!(°ー°〃)_v1.0"
	choices = ["大佬杰", "大佬忠", "大佬A", "大佬王"]

	choice = e.multchoicebox(msg, title, choices)
	return choice

if __name__ == '__main__':
	choice_people()