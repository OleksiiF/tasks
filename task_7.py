#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import asyncio
import time

import aiohttp

# Сделать скрипт, который будет делать GET запросы на ресурсы.
# Для каждого запроса должен быть вывод по примеру:
# "Resource 'google.com.ua', request took 0.23 sec, response status - 200."
# В реализации нет ограничений - можно использовать процессы, потоки,
# асинхронность. Любые вспомогательные механизмы типа Lock, Semaphore,
# пулы для тредов и потоков.
def print_str_resp_with_time(func):
    start = time.time()
    if asyncio.iscoroutinefunction(func):
        async def wrapper(*args):
            result = await func(*args)
            print(
                f"Time is {round(time.time() - start, 3)}.",
                f"{result}. " if result else '',
            )
    else:
        def wrapper(*args):
            result = func(*args)
            print(
                f"Time is {round(time.time() - start, 3)}.",
                f"{result}. " if result else '',
            )
    return wrapper


@print_str_resp_with_time
async def get_response(session, resource):
    async with session.get(resource) as response:
        return f"{resource=}, {response.status=}"


async def async_worker(links):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *(get_response(session, link) for link in links)
        )


@print_str_resp_with_time
def async_starter(links):
    asyncio.run(async_worker(links))


if __name__ == '__main__':
    links = [
        "http://docs.python-requests.org/",
        "https://httpbin.org/get",
        "https://httpbin.org/",
        "https://api.github.com/",
        "https://example.com/",
        "https://www.python.org/",
        "https://www.google.com.ua/",
        "https://regex101.com/",
        "https://docs.python.org/3/this-url-will-404.html",
        "https://www.nytimes.com/guides/",
        "https://www.mediamatters.org/",
        "https://1.1.1.1/",
        "https://www.politico.com/tipsheets/morning-money",
        "https://www.bloomberg.com/markets/economics",
        "https://www.ietf.org/rfc/rfc2616.txt"
    ]
    async_starter(links)
