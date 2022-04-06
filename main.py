import json
if __name__ == '__main__':
    exer=input("insert exercise number\n")
    match exer:
        case '1':
            json_obj = '{"Name": "David", "Class": "I", "Age": 6}'
            python_obj=json.loads(json_obj)
            print('JSON Data:\n')
            print(python_obj)
            print('\nName: ',python_obj['Name'])
            print('\nClass: ', python_obj['Class'])
            print('\nAge: ', python_obj['Age'])
        case '2':
            python_obj={
                'Name': 'David',
                'Class': 'I',
                'Age': 6
            }
            json_obj=json.dumps(python_obj)
            print(json_obj)
        case '3':
            python_obj = {
                'Name': 'David',
                'Class': 'I',
                'Age': 6
            }
            json_obj = json.dumps(python_obj)
            print(json_obj)
        case '4':
            python_obj = {'4':5,'6':7,'1':3,'2':8}
            json_obj=json.dumps(python_obj,sort_keys=True,indent=4)
            print(json_obj)
        case '5':
            with open('states.json') as read_file:
                state_data=json.load(read_file)
            for state in state_data["states"]:
                del state["area_codes"]
            with open('new_states.json','w') as write_file:
                json.dump(state_data,write_file,indent=2)


