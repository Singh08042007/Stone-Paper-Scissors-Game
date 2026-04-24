#Score Storage Logic
win = 0
loss = 0

def get_score():
    return win, loss

def update_win():
    global win
    win += 1

def update_loss():
    global loss
    loss += 1