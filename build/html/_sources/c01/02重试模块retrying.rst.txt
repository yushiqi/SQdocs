1.2 重试模块retrying
--------------------

1.简介
~~~~~~

一个很好用的关于重试的Python包，可以用来自动重试一些可能会运行失败的程序段。

2.安装
~~~~~~

.. code:: shell

   $ pip install retrying

3.API介绍
~~~~~~~~~

.. code:: python

   def __init__(self,
                    stop=None, wait=None,
                    stop_max_attempt_number=None,
                    stop_max_delay=None,
                    wait_fixed=None,
                    wait_random_min=None, wait_random_max=None,
                    wait_incrementing_start=None, wait_incrementing_increment=None,
                    wait_exponential_multiplier=None, wait_exponential_max=None,
                    retry_on_exception=None,
                    retry_on_result=None,
                    wrap_exception=False,
                    stop_func=None,
                    wait_func=None,
                    wait_jitter_max=None)

-  stop_max_attempt_number：用来设定最大的尝试次数，超过该次数就停止重试

-  stop_max_delay：比如设置成10000，那么从被装饰的函数开始执行的时间点开始，到函数成功运行结束或者失败报错中止的时间点，只要这段时间超过10秒，函数就不会再执行了

-  wait_fixed：设置在两次retrying之间的停留时间

-  wait_random_min和wait_random_max：用随机的方式产生两次retrying之间的停留时间

-  wait_exponential_multiplier和wait_exponential_max：以指数的形式产生两次retrying之间的停留时间，产生的值为2^previous_attempt_number
   \*
   wait_exponential_multiplier，previous_attempt_number是前面已经retry的次数，如果产生的这个值超过了wait_exponential_max的大小，那么之后两个retrying之间的停留值都为wait_exponential_max

-  我们可以指定要在出现哪些异常的时候再去retry，这个要用retry_on_exception传入一个函数对象

4.示例
~~~~~~

-  @retry装饰器，如出现异常会一直重试

.. code:: python

   @retry
   def never_give_up_never_surrender():
       print "Retry forever ignoring Exceptions, don't wait between retries"

-  stop_max_attempt_number 设置最大重试次数

.. code:: python

   @retry(stop_max_attempt_number=7)
   def stop_after_7_attempts():
       print "Stopping after 7 attempts"
       raise

-  stop_max_delay 设置失败重试的最大时间, 单位毫秒，超出时间，则停止重试

.. code:: python

   @retry(stop_max_delay=10000)
   def stop_after_10_s():
       print "Stopping after 10 seconds"
       raise

-  wait_fixed 设置失败重试的间隔时间

.. code:: python

   @retry(wait_fixed=2000, stop_max_delay=10000)
   def wait_2_s():
       print "Wait 2 second between retries"
       raise

-  wait_random_min, wait_random_max 设置失败重试随机性间隔时间

.. code:: python

   @retry(wait_random_min=1000, wait_random_max=5000, stop_max_delay=10000)
   def wait_random_1_to_5_s():
       print "Randomly wait 1 to 5 seconds between retries"
       raise

-  wait_exponential_multiplier-间隔时间倍数增加，wait_exponential_max-最大间隔时间

.. code:: python

   import time

   @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
   def wait_exponential_1000():
       print "Wait 2^x * 1000 milliseconds between each retry, up to 10 seconds, then 10 seconds afterwards"
       print int(time.time())
       raise

-  retry_on_exception指定异常类型，指定的异常类型会重试，不指定的类型，会直接异常退出，wrap_exception参数设置为True，则其他类型异常，或包裹在RetryError中，会看到RetryError和程序抛的Exception
   error

.. code:: python

   def retry_if_io_error(exception):
       """Return True if we should retry (in this case when it's an IOError), False otherwise"""
       return isinstance(exception, IOError)

   @retry(retry_on_exception=retry_if_io_error)
   def might_io_error():
       print "Retry forever with no wait if an IOError occurs, raise any other errors"
       raise Exception('a')


   @retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
   def only_raise_retry_error_when_not_io_error():
       print "Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError"
       raise Exception('a')

-  retry_on_result,
   指定要在得到哪些结果的时候去retry，retry_on_result传入一个函数对象,在执行get_result成功后，会将函数的返回值通过形参result的形式传入retry_if_result_none函数中，如果返回值是None那么就进行retry，否则就结束并返回函数值

.. code:: python

   def retry_if_result_none(result):
       return result is None

   @retry(retry_on_result=retry_if_result_none)
   def get_result():
       print 'Retry forever ignoring Exceptions with no wait if return value is None'
       return None
