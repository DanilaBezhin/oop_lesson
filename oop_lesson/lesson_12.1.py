class StripChar: 
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("The first argument must be a string")
        
        # по умолчанию удаляются пробелы в начале и в конце (можно предать какие еще значения удалять)
        return args[0].strip(self.__chars)
    

s1 = StripChar("?:!.; ")
res1 = s1(" Hello world! ")

s2 = StripChar(" ")
res2 = s2(" Hello world! ")
res3 = s2(" 23123!   ")
print(res1, res2, res3, sep="\n")