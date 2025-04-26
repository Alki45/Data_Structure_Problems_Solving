class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.count_intger=0
        

    def consec(self, num: int) -> bool:
        if num==self.value:
            self.count_intger+=1
        else:
            self.count_intger=0
        if self.count_intger>=self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)