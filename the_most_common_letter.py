line='lasfasfssvpavafkaksvmaslflasddfksadfmskbfkgmsakasdvkasdafkafmasdkfsmf'
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number_l=[]
a=0
for letter in letters:
    number_l.append(a)
    
for i in line:
    for letter in letters:
        if i == letter:
            number_l[letters.index(letter)]+=1
     
print(number_l)
print(letters[number_l.index(max(number_l))])    
