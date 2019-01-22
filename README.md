# Celery demo
This is an example about how to setup celery on localhost so python
app can call async tasks.

Prerequisites:

Make sure install redis or any other broker (like rabbitMQ) first. 

Reference:
https://medium.com/@petehouston/install-and-config-redis-on-mac-os-x-via-homebrew-eb8df9a4f298

## commands to start redis locally (MAC):
redis-server /usr/local/etc/redis.conf

## command to start celery:
```bash
celery -A tasks worker --loglevel=info
```

Then you will see this message:
```bash

The pickle serializer is a security concern as it may give attackers
the ability to execute any command.  It's important to secure
your broker from unauthorized access when using pickle, so we think
that enabling pickle should require a deliberate action and not be
the default choice.

If you depend on pickle then you should set a setting to disable this
warning and to be sure that everything will continue working
when you upgrade to Celery 3.2::

    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

You must only enable the serializers that you will actually use.


  warnings.warn(CDeprecationWarning(W_PICKLE_DEPRECATED))

 -------------- celery@TanGes-MacBook.local v3.1.26.post2 (Cipater)
---- **** -----
--- * ***  * -- Darwin-18.0.0-x86_64-i386-64bit
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x10509b978
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ----
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery


[tasks]
  . tasks.showMessage

[2019-01-22 13:21:19,228: INFO/MainProcess] Connected to redis://localhost:6379/0
[2019-01-22 13:21:19,252: INFO/MainProcess] mingle: searching for neighbors
[2019-01-22 13:21:20,275: INFO/MainProcess] mingle: all alone
[2019-01-22 13:21:20,299: WARNING/MainProcess] celery@local ready.
```


Run the python code in python console:

```bash
Python 2.7.13 (default, Dec 17 2016, 23:03:43)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from tasks import celery_add
>>> celery_add.delay(2,10)
<AsyncResult: e19abf77-8220-4fb1-b772-e28a783a33ff>
```


You will see

```bash
[tasks]
  . tasks.celery_add

[2019-01-22 14:29:59,338: INFO/MainProcess] Connected to redis://127.0.0.1:6379//
[2019-01-22 14:29:59,382: INFO/MainProcess] mingle: searching for neighbors
[2019-01-22 14:30:00,521: INFO/MainProcess] mingle: all alone
[2019-01-22 14:30:00,574: INFO/MainProcess] celery@TanGes-MacBook.local ready.
[2019-01-22 14:30:57,872: INFO/MainProcess] Received task: tasks.celery_add[e19abf77-8220-4fb1-b772-e28a783a33ff]
[2019-01-22 14:30:59,883: WARNING/ForkPoolWorker-1] The add result is 12.
[2019-01-22 14:30:59,925: INFO/ForkPoolWorker-1] Task tasks.celery_add[e19abf77-8220-4fb1-b772-e28a783a33ff] succeeded in 2.047685897s: 12
```