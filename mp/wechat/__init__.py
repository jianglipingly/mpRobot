# -*- coding: utf-8 -*-

from error import Error
from mp.config import Config
from wechat import WeChat


error = Error()
wechat = WeChat(token=Config.WECHAT.get('token'))