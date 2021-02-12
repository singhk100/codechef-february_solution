try:
    a=''
    def timeConversion(s):
       if s[-2:] == "AM" :
          if s[:2] == '12':
              a = str('00' + s[3:5])
          else:
              a = s[:2] +s[3:5]
       else:
          if s[:2] == '12':
              a = s[:2] +s[3:5]
          else:
              a = str(int(s[:2]) + 12) + s[3:5]
       return int(a)
    T=int(input())
    for i in range(T):
        s=input()
        s=timeConversion(s)
        T1=int(input())
        result=""
        for j in range(T1):
            s1=input()
            s2=timeConversion(s1[:8])
            s3=timeConversion(s1[9:])
            if (s>=s2 and s<=s3):
                result+="1"
            else:
                result+="0"
        print(result)
except Exception:
    print("problem")
