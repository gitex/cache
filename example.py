#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cache import Cache
import time

# Creating instance for Cache with default cache time
cache = Cache(10)


# Time for current function
@cache(3)
def test_function():
    return time.time()


print test_function()  # Function will call and return result
print test_function()  # Function won't call and it will take result from cache
time.sleep(5)
print test_function()  # Time of cache is over and function will call again
