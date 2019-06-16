
def can_build(env, platform):
    if platform in ["javascript", "haiku"]:
        return False
    return True

def configure(env):
    pass

def get_defines(env):
    if env["platform"] == "android":
        return {
            'PJ_ANDROID' : 1,
            'PJ_M_NAME' : '\\\"' + env['android_arch'] + '\\\"',
            'PJ_IS_LITTLE_ENDIAN' : 1,
            'PJ_IS_BIG_ENDIAN' : 0,
        }
    