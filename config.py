
def can_build(env, platform):
    if platform in ["javascript", "haiku"]:
        return False
    return True

def configure(env):
    pass
    
def get_doc_classes():
    return [
        "PJNATH",
    ]
    
def get_doc_path():
    return "doc_classes"

def get_defines(env):
    if env["platform"] == "android":
        # note: this could be handled by config_site.h as well
        return {
            'PJ_CONFIG_ANDROID' : 1,
            'PJ_ANDROID' : 1,
            'PJ_M_NAME' : '\\\"' + env['android_arch'] + '\\\"',
            'PJ_IS_LITTLE_ENDIAN' : 1,
            'PJ_IS_BIG_ENDIAN' : 0,
        }
    