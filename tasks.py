from invoke import task

@task
def test(c):
    """
    Run tests
    """
    c.run("python -m unittest discover")
    # c.run("pytest")
    

@task
def run(c):
    """
    Run tests
    """
    c.run("python  reproject/app.py")    
