import easyocr
reader = easyocr.Reader(['fr', 'ar']) # this needs to run only once to load the model into memory
result = reader.readtext('./../data/bultin.jpg')


#write arabic in a file
with open('result_bultin.txt', 'w', encoding='utf-8') as f:
    for i in range(len(result)):
        f.write(result[i][1] + '\n')