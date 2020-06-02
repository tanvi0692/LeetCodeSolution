class kanika:
    def __init__(self,total_elements):
        self.total_elements = total_elements
        self.res = []
        self.res_count = 0
        
    def verify(self,arr):
        index = 0
        while index < len(arr)-1 and arr[index+1]%arr[index] == 0:

            index+=1
        if index == len(arr)-1:
            return True
        return False
        
    def recursion(self,input_arr,temp_arr=[]):
        
        if len(temp_arr) == self.total_elements:
            if self.verify(temp_arr):
                self.res = self.res + [temp_arr[:]]
                self.res_count = self.res_count +1
            return
        
        for i in range(0,len(input_arr)-self.total_elements+len(temp_arr)+1):
            temp_arr = temp_arr + [input_arr[i]]
            if len(input_arr) ==1:
                self.recursion([],temp_arr)
            else:
                self.recursion(input_arr[i+1:],temp_arr)
            temp_arr.pop()

k = kanika(3)
k.recursion([1,4,4,8,16,13,64])
print(k.res)
print(k.res_count)