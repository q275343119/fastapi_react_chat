"""
启动项 - 应用
"""
import logging

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.providers import app_provider
from app.providers import handle_exception
from app.providers import logging_provider
from app.providers import route_provider


def create_app() -> FastAPI:
    """
    建立app
    :return:
    """
    app = FastAPI(default_response_class=ORJSONResponse)
    # 注册日志
    register(app, logging_provider)
    # 注册app 启动项 结束项 中间件
    register(app, app_provider)
    # 注册 异常处理
    register(app, handle_exception)
    # 添加路由
    boot(app, route_provider)

    return app


def register(app, provider):
    """
    provider 注册
    :param app:
    :param provider:
    :return:
    """
    provider.register(app)
    logging.info(provider.__name__ + ' registered')


def boot(app, provider):
    """
    启动项
    :param app:
    :param provider:
    :return:
    """
    provider.boot(app)
    logging.info(provider.__name__ + ' booted')
