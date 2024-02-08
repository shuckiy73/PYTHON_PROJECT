def get_medical_service(preparat):
    def do_treat():
        print(f'[{preparat}]Я вылечил тебя')

    return do_treat


treater1 = get_medical_service('Парацетамол')
treater2 = get_medical_service('Укол')

treater1()
treater1()
treater2()
treater2()
treater2()
treater2()


def init_counter(start_from=0):
    def count():
        nonlocal start_from
        start_from += 1
        print(f'Номер: {start_from}')
    return count


counter1 = init_counter(0)
counter2 = init_counter(100)
counter1()
counter1()
counter1()
counter1()
counter1()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
counter2()
