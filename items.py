class SchoolsItem(object):
    """学校属性

    Attributes:
        name 学校名
        url 学校网址
        school_character 学校特色['985','211','普通']
        education_level 高校性质['本科'，'专科']
        school_type 学校类别['工科',...]
        region 学校所在地区
        subjection 学校隶属
    """

    name = None
    url = None
    education_level = None
    region = None
    school_character = None
    school_type = None
    subjection = None



class PartyInfoItem(object):
    """
    相关的信息
    """
    school_url = None
    related_url = None
    related_title = None
    brief_introduction = None
    release_time = None