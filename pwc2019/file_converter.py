import time
import pandas



def time_converter(seconds):
    # res = str(datetime.timedelta(seconds=seconds))
    res = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return res


with open('output.txt','r') as file_formula:
    raw_formula = file_formula.read()
    raw_formula = raw_formula.replace("    - ",'')
    raw_formula = raw_formula.split('\n')
    # res = res.split('\n')
file_formula.close()

def str_ope(raw_formula):
    result_dict = {
        'timeStamp_list': [],
        'formula_list': []
    }
    # len_time = len(raw_ordinary)
    len_time = 1000
    len_formula = len(raw_formula)
    print(len_formula)
    formula_index = 0
    time_index = 0

    time_span = 0.5
    current_time = 0

    # for time_index in range(len_time):
    while(formula_index < len_formula):

        if(raw_formula[formula_index] == 'No license plates found.'):
            formula_index = formula_index + 1
        else:
            formula_index += 1
            if (formula_index >= len_formula):
                break
            # print(raw_formula[formula_index])
            most_likely = raw_formula[formula_index].split('\t')[0]


            current_formula = most_likely
            current_timeStamp = time.strftime("%H:%M:%S", time.gmtime(current_time))

            result_dict['timeStamp_list'].append(current_timeStamp)
            result_dict['formula_list'].append(current_formula)


            # print("res = ",current_formula)

            while(formula_index < len_formula and 'confidence' in raw_formula[formula_index]):
                formula_index += 1
                # print(formula_index)

            if(formula_index >= len_formula):
                break

        time_index += 1
        current_time += time_span


    df_res = pandas.DataFrame.from_dict(result_dict)
    df_res = df_res[['formula_list','timeStamp_list']]


    df_res.to_csv('formula.csv',index=False)

# print(time_converter(5555))



# print(raw_formula)

str_ope(raw_formula)

# res = time.strftime("%H:%M:%S", time.gmtime(0.5))
# res = time.strftime("%H:%M:%S", time.gmtime(1))
# res = time.strftime("%H:%M:%S", time.gmtime(1.5))
# res = time.strftime("%H:%M:%S", time.gmtime(2))
# print(res)
