class MyException:
    def __repr__(self):
        raise Exception


a = MyException()
func(a)