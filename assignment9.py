#1
def count_lines(file_name):
    count=0
    with open(file_name, "r", encoding='uft-8') as file:
        for line in file:
            if line.strip != "":
                count+=1
    return count

#2
def find_keyword_in_lines(file_name, keyword):
    result=[]
    with open(file_name,"r", encoding='uft-8') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                result.append[i]
    return result

#3
def read_change_keyword(file_name,):
    with open(file_name, "r", encoding='uft-8') as file:
        content=file.read()
    upper_content= content.upper()
    with open("output.txt", "w", encoding='uft-8') as file:
        file.write=(upper_content)

#4
def calculate_average_score(file_name):
    total=0
    count=0
    with open(file_name, "r", encoding='uft-8') as file:
        for line in file:
            if line.strip!= " " :
                name, score= line.split(',')
                total+= float(score)
                count +=1
    if count==0:
        return 0
    return(total/count)