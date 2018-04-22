count = 1
def show_count():
    print(count)
	
	
def set_count(c):
    global count
    count = c
    print(count)