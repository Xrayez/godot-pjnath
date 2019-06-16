
def can_build(env, platform):
    if env["platform"] in ["javascript", "haiku"]:
        return False
    return True

def configure(env):
    pass
