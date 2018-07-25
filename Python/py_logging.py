# coding=utf-8
# date: 2018-3-29, 16:31:51
# name: smz


import logging


def example_one():
    # 配置日志信息
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='myapp.log',
                        filemode='w')
    # 定义一个Handler打印INFO及以上级别的日志到sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 设置日志打印格式
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # 将定义好的console日志handler添加到root logger
    logging.getLogger('').addHandler(console)
    logging.info('Jackdaws love my big sphinx of quartz.')

    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')
    logger1.debug('Quick zephyrs blow, vexing daft Jim.')
    logger1.info('How quickly daft jumping zebras vex.')
    logger2.warning('Jail zesty vixen who grabbed pay from quack.')
    logger2.error('The five boxing wizards jump quickly.')

def example_two():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',   # 大写的Y显示2018,小写的y显示18
                        filename='mylog.log',
                        filemode='a')  # a表示追加,w表示直接写入,如果有重名,会覆盖

    objConsole = logging.StreamHandler()  # 向控制台输出消息的控制器
    objConsole.setLevel(logging.INFO)
    objFormat = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    objConsole.setFormatter(objFormat)
    logging.getLogger().addHandler(objConsole)  # 将所有的Handler合并成一个logger
                                                        # 这样可以一同输出相同的东西
    logging.info('test')

def exercise_one():
    # 基本设置
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s->%(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        filename='mylog.log',
                        filemode='a')
    # 设置控制台的输出管理器
    objconsole = logging.StreamHandler()
    # 设置控制台的管理器的格式
    objformat = logging.Formatter(fmt='%(asctime)s->%(message)s',
                                  datefmt='%Y-%m-%d,%H:%M:%S')
    objconsole.setLevel(level=logging.INFO)
    objconsole.setFormatter(objformat)

    # 获取默认的输出控制器,然后添加上控制台的控制器
    logging.getLogger().addHandler(objconsole)

    # 让所有的控制器输出同样的信息
    logging.info('hello, this is my exercise one')

def exercise_two():
    # 基本设置
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s, %(message)s',
                        datafmt='%Y-%m-%d, %H:%M:%S',
                        filename='mylog.log',
                        filemode='a')

    # 设置控制台输出
    objconsole = logging.StreamHandler()
    # 控制台输出格式
    objformat = logging.Formatter(fmt='%(asctime)s, %(message)s',
                                  datefmt='%Y-%m-%d, %H:%M:%S')
    objconsole.setFormatter(objformat)

    # 将控制器添加到本地的控制器
    logging.getLogger().addHandler(objconsole)
    logging.info('hello, I\'m exercise two')

def exercise_three():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s, %(message)s',
                        datefmt='%Y-%m-%d, %H:%M:%S',
                        filename='mylog.log',
                        filemode='a')

    # 设置控制台的显示
    objconsole = logging.StreamHandler()
    # 控制台的格式
    objformat = logging.Formatter(fmt='%(asctime)s, %(message)s',
                                   datefmt='%Y-%m-%d, %H:%M:%S')
    objconsole.setFormatter(objformat)

    # 将控制台显示与当前的显示器合并
    logging.getLogger().addHandler(objconsole)

    # 同时显示相同的信息
    logging.info('hello, my third exercise')

if __name__ == '__main__':
    # example_two()
    # exercise_one()
    # exercise_two()
    exercise_three()