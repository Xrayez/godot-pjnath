
def can_build(env, platform):
    if platform in ["javascript", "haiku"]:
        return False
    return True

def configure(env):
    pass
