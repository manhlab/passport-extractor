from deeppavlov import configs, build_model
from pathlib import Path


def findNameByParce(line_mas):
    data = line_mas[0:5]
    name = ""
    surname = ""
    for x in data:
        if len(x) > len(surname):
            name = surname
            surname = x
            continue
        if len(x) > len(name):
            name = x
    return (name, surname)


def findNameWithNer(ner_data):
    if ner_data[1][0].count("B-PER") == 0 or ner_data[1][0].count("I-PER") == 0:
        return findNameByParce(ner_data[0][0])
    name_index = ner_data[1][0].index("B-PER")
    surname_index = ner_data[1][0].index("I-PER")
    if not (
        name_index < 2
        and surname_index > name_index
        and surname_index < 4
        and surname_index - name_index < 2
    ):
        return findNameByParce(ner_data[0][0])
    name = ner_data[0][0][name_index]
    surname = ner_data[0][0][surname_index]
    if len(name) < 4 or len(surname) < 4:
        return findNameByParce(ner_data[0][0])
    return (name, surname)


def findDate(ner_data):
    data = ner_data[0][0][5:]
    data = "".join(data)
    data = data.replace(",", ".")
    if data.count(".") < 2:
        return data[0:11]
    i = 0
    while i < len(data):
        if data[i].isdigit():
            break
        else:
            data = data[1:]
    if data.count(".") < 2:
        return data[0:11]
    return data[data.find(".") - 2 : data.find(".") + 8]


if __name__ == "__main__":
    file = open("results.txt", "w")
    ner_model = build_model(configs.ner.ner_rus_bert_torch, download=True)

    # for name in p.rglob("*"):
    f = open("/content/result.txt", "r")
    Lines = f.readlines()
    for line in Lines:
        print(line)
        ner_data = ner_model([line])
        name, surname = findNameWithNer(ner_data)
        date = findDate(ner_data)
        print(ner_data)
        print(name, surname, date)
        file.write(name + " " + surname + " " + date + "\n")
    file.close()