user_input = input("")  

segments = []  

def balanced_segments(user_input):
    balance = 0
    segment = ""
    
    for char in user_input:
        segment += char
        balance += 1 if char == 'L' else -1
        if balance == 0:  
            segments.append(segment)
            segment = ""  
    
    print(len(segments)) 
    for seg in segments:
        print(seg)

balanced_segments(user_input)
