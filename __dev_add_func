from os import listdir

def writeToFuncList(new_filename, new_funcname, new_keywords):
    new_entry = ",\n    ['" + new_filename + '.' + new_funcname + "',\n    " + ', '.join(new_keywords) + ']'

    fr = open('Function_keywords.py', encoding='utf-8')
    func_file = fr.read()
    fr.close()

    func_file = func_file[:func_file.rfind(']')-1] + new_entry + '\n]\n'

    fw = open('Function_keywords.py', encoding='utf-8', mode='w')
    fw.write(func_file)
    fw.close()

def writeImportToMain(new_filename):
    new_entry = '\nimport ' + new_filename

    fr = open('main.py', encoding='utf-8')
    main_file = fr.read()
    fr.close()

    for i in range(main_file.rfind('import'), len(main_file)):
        if main_file[i] == '\n':
            pos = i
            break

    main_file = main_file[:pos] + new_entry + main_file[pos:]
    fw = open('main.py', encoding='utf-8', mode='w')
    fw.write(main_file)
    fw.close()


lstdir = listdir('.')
if 'main.py' in lstdir:
    if 'Function_keywords.py' in lstdir:
        pass
    else:
        raise FileNotFoundError("This script must be in the same directory as 'Function_keywords.py'.")
else:
    raise FileNotFoundError("This script must be in the same directory as 'main.py'.")


print("This script adds internal Python functions to ReisidAafrikasse. Before adding, remove\n"
      "all tests (print(yourFunction('test_info')) from the function file and make sure the\n"
      "function accepts arguments as list. For example if the function takes 2 arguments, make\n"
      "sure it takes a list as an argument and then isolate the two args from list:\n"
      "arg1, arg2 = lst[0], lst[1].")
func_filename = input('Name of .py file that contains the new function: ')
func_name = input('Name of the new function: ')

if func_filename.endswith('.py'):
    func_filename = func_filename[:-3]
if func_name.endswith('()'):
    func_name = func_name[:-2]

i = 0
keywords = []
while True:
    i += 1
    keyword = input(str(i) + '. keyword (empty string to stop): ')
    if keyword == '':
        break
    else:
        keywords.append("'" + keyword + "'")

writeToFuncList(func_filename, func_name, keywords)
writeImportToMain(func_filename)
