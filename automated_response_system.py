import json
import pprint

pp = pprint.PrettyPrinter(indent=6)

class AutomatedResponseSystem():

    def sample_text_function(self):

        data_dict ={}
        with open('json/assignment_1_input_2.json') as file:
            data = json.load(file)

            #iterating over the questions list
            for dictionary in data['questions']:

                try:
                    if "conditions" in dictionary:
                        expression = dictionary['conditions'][0][0].replace( dictionary['var'], "data_dict['" + dictionary['var'] + "']" )
                        print(expression)
                        if eval(expression):
                            pass
                        else:
                            continue
                except Exception as error:
                    pass

                try:                    
                    if "instruction" in dictionary:
                        if "instruction_var" in dictionary:
                            print(dictionary['instruction']%( data_dict[dictionary['instruction_var'][0]] ) )
                        else:
                            print(dictionary['instruction'])
                except Exception as error:
                    pass

                try:
                    if "text" in dictionary:
                        print(dictionary['text'])

                        if dictionary['var'].find('row')!= -1:
                            data_dict['rows'].append(input())
                            continue 

                        data_dict[ dictionary['var'] ] = input()
                except Exception as error:
                    pass

                try:
                    if "calculated_variable" in dictionary:
                        if dictionary["formula"]=="first_name + ' ' + last_name":
                            data_dict[ dictionary['var'] ] = data_dict['first_name']+' '+data_dict['last_name']
                        
                        if dictionary["formula"]=="[]":
                            data_dict[ dictionary['var'] ] = [] 

                        if dictionary["formula"]=="[map(int, i.split()) for i in row]":
                            data_dict[ dictionary['var'] ] = [list( map(int, i.split()) ) for i in data_dict['rows']]

                        if dictionary["formula"]=="[[matrix[j][i] for j in xrange(3)] for i in xrange(3)]":
                            data_dict['t_matrix'] = [[data_dict['matrix'][j][i] for j in range(3)] for i in range(3)]             

                except Exception as error:
                    pass  

                try:
                    if "list_var" in dictionary:
                        i = 0
                        while( i<=int(dictionary['list_length']) ):
                            print(dictionary['instruction']%( str(i+1), eval(dictionary['instruction_var'][1].replace('t_matrix', "data_dict['t_matrix']")) ) )
                            i =  eval(dictionary['instruction_var'][0])
                except Exception as error:
                    pass        
                

if __name__ == '__main__':
    obj = AutomatedResponseSystem()
    obj.sample_text_function()