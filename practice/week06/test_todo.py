from todo_app import cmd_add, cmd_done, cmd_del

def test_add():
    tasks = []
    cmd_add(tasks,'买牛奶')
    assert len(tasks) == 1
    assert tasks[0]['text'] == '买牛奶'
    assert tasks[0]['done'] == False

def test_done():
    tasks = [{'text':'买牛奶','done':False}]
    cmd_done(tasks,1)
    assert tasks[0]['done'] ==True

def test_done_out_of_range():
    tasks = [{'text':'买牛奶','done':False}]
    cmd_done(tasks,99)
    assert tasks[0]['done'] == False

def test_del():
    tasks = [{'text':'A'},{'text':'B'}]
    cmd_del(tasks,1)
    assert len(tasks) == 1
    assert tasks[0]['text'] == 'B'

