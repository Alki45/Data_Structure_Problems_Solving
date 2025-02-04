class Solution:
    def maskPII(self, s: str) -> str:
        new_string=[]
        if('@' in s):
                new_string=[i.lower()  if i.isalpha() else i for i in s]
                new_string=''.join(new_string)
                n=new_string.index('@')
                domain=new_string[n:]
                Repl=new_string[0]+"*****"+new_string[n-1]
                new_string=Repl+domain
                
        else:
                new_string=[i for i in s if i.isdigit()]
                new_string=''.join(new_string)
                if(len(new_string)==10):
                    new_string="***-***-"+new_string[-4:]
                elif(len(new_string)==11):
                    new_string="+*-***-***-"+new_string[-4:]
                elif(len(new_string)==12):
                    new_string="+**-***-***-"+new_string[-4:]
                elif(len(new_string)==13):
                    new_string="+***-***-***-"+new_string[-4:]
        return new_string
            