        for i in range(1,len(nums)-1,1):
            returner.append(prefix[i-1]*postfix[i+1])            
        
        returner.insert(0,postfix[1])
        returner.append(prefix[len(nums)-1])