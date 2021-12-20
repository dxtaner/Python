m_input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = []
for i in m_input_list:
    if type(i) is list:
        for j in i:
            if type(j) is list:
                for t in j:
                    if type(t) is list:
                        for z in t:
                            output_list.append(z)
                    else:
                        output_list.append(t)
            else:
                output_list.append(j)

    else:
        output_list.append(i)

print("girdi listesi:",m_input_list)
print("flatten listesi:",output_list)