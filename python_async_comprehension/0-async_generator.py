#!/usr/bin/env python3
""" 0. Async Generator
"""

import asyncio
import random
from typing import Generator


async def async_generator():
    '''Generate a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
