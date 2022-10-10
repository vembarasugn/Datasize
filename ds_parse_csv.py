from collections import Counter, OrderedDict
import re
import operator

countries = []
size_countries = []
err_data = []
summ = {}

with open(r'C:\Users\parad\Downloads\unstructured_sizes.csv') as f:
    data = Counter(f.read().split())
    for key, value in data.most_common():
        cnt = re.findall(r'\(([A-Za-z]+)\)', key)
        if cnt:
            [countries.append(cnt_1) for cnt_1 in cnt if cnt_1 not in countries]
    for cn in countries:
        summ[cn] = []

with open(r'C:\Users\parad\Downloads\unstructured_sizes.csv') as f:
    data = Counter(f.read().split("\n"))
    for datum in data:
        size = re.findall(r'([0-9]+[.]*[0-9]*[A-Za-z]*[\s]*\([A-Za-z]+\))', datum)
        if size:
            [size_countries.append(size_1) for size_1 in size]
            for key in summ:
                [summ[key].append(size_1.split('(')[0].strip()) for size_1 in size if key in size_1]
        else:
            err_data.append(datum)


def list_to_dict(list_val=[]):
    if not list_val:
        return []
    else:
        return dict(Counter(list_val))


for key, val in summ.items():
    x = dict(list_to_dict(val))
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
    summ[key] = sorted_x

fn = open(r'C:\Users\parad\Downloads\data_output.txt', "w")
fn.write('*'*50+"\n")
fn.write("Preferable Sizes from Countries\n")
fn.write('*'*50+"\n")
for val in countries:
    fn.write(val+"\n")
fn.write("\n\n")
fn.write('*'*50+"\n")
fn.write("Sizes Preferred based on Countries and Sizes\n")
fn.write('*'*50+"\n")
for key, val in summ.items():
    fn.write("*"*2+"\n"+key+"\n"+"*"*2+"\n")
    for value_list in val:
        fn.write(str(value_list[0]) + " : " + str(value_list[1])+"\n")
    fn.write("\n")
fn.write("\n\n")
fn.write('*'*50+"\n")
fn.write("Data that are not processed\n")
fn.write('*'*50+"\n")
for err_line in err_data:
    fn.write(err_line+"\n")

