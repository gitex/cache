#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


class Cache(object):
    """Class caching function's results for some time.

    Using:

    1) Create instance of Cache with parameter default_max_time or without

    cache = Cache(seconds)

    2.1) You need to add decorator with instance's name to function without max_time

    @cache()
    def some_function(*args, **kwargs)
        return someone

    2.2) ...or with one

    @cache(30)
    def some_function(*args, **kwargs)
        return someone
    """

    def __init__(self, default_max_time=20):
        self.default_max_time = default_max_time
        self.cached_responses = {}

    def __call__(self, max_time=None):
        max_time = max_time if max_time else self.default_max_time

        def cache_function(function):
            def wrapped(*args, **kwargs):
                last_time = None

                if function in self.cached_responses:
                    last_time = self.cached_responses[function]['datetime']

                    if (datetime.now() - last_time).seconds > max_time:
                        last_time = None

                if function not in self.cached_responses or not last_time:
                    response = function(*args, **kwargs)

                    self.cached_responses[function] = {
                        'datetime': datetime.now(),
                        'response': response
                    }

                    return response

                else:
                    return self.cached_responses[function]['response']
            return wrapped
        return cache_function

    def clear(self):
        self.cached_responses = {}
