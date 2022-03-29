import streamlit as st
import pandas as pd
from PIL import Image
import os
import numpy as np
import time

if(os.path.exists("./testcsv.csv")):
    results = pd.read_csv("./testcsv.csv").iloc[:,1:].values.tolist()
else:
    results = [[0,0,0] for i in range(24)]

st.title('书法打标')

file_dir = os.listdir("./image/")
file_dir.sort()
print(file_dir)

csv_file = pd.read_csv("./data.csv")
now_set = st.selectbox('选择实验组', [i for i in range(csv_file.shape[0])])

width = 400

image_1 = Image.open('./image/'+file_dir[csv_file.iloc[now_set,0]-1])
resize_num = image_1.size[0]/width
image_1 = image_1.resize((400,int(image_1.size[1]/resize_num)))
st.image(image_1, caption='实验图像1')

image_2 = Image.open('./image/' + file_dir[csv_file.iloc[now_set, 1]-1])
resize_num = image_2.size[0]/width
image_2 = image_2.resize((400,int(image_2.size[1]/resize_num)))
st.image(image_2, caption='实验图像2')

image_3 = Image.open('./image/' + file_dir[csv_file.iloc[now_set, 2]-1])
resize_num = image_3.size[0]/width
image_3 = image_3.resize((400,int(image_3.size[1]/resize_num)))
st.image(image_3, caption='实验图像3')

image_name = [csv_file.iloc[now_set,0]-1, csv_file.iloc[now_set,1]-1, csv_file.iloc[now_set,2]-1]

list = [1,2,3]
now_score_1 = st.selectbox('Rank 1', list)
now_score_2 = st.selectbox('Rank 2', [i for i in list if i != now_score_1])
now_score_3 = st.selectbox('Rank 3', [i for i in list if (i != now_score_1 and i != now_score_2)])

if(st.button("OK")):
    rank_1 = image_name[now_score_1-1]
    rank_2 = image_name[now_score_2-1]
    rank_3 = image_name[now_score_3-1]
    print(rank_1,rank_2,rank_3)
    results[rank_1][0]+=1
    results[rank_2][1]+=1
    results[rank_3][2]+=1

name = ['rank 1','rank 2','rank 3']

test=pd.DataFrame(columns=name,data=results)
test.to_csv('testcsv.csv',encoding='gbk')
# for i in range(csv_file.shape[0]):
#     print(csv_file.iloc[i,0])
    # select_1 = st.checkbox(str(csv_file.iloc(i)))

    # image_1 = Image.open('./image/'+file_dir[csv_file.iloc[i,0]])
    # image_1 = image_1.resize((int(image_1.size[0]*0.2),int(image_1.size[1]*0.2)))
    # st.image(image_1, caption='Sunrise by the mountains')
    #
    # image_2 = Image.open('./image/' + file_dir[csv_file.iloc[i, 1]])
    # image_2 = image_2.resize((int(image_2.size[0] * 0.2), int(image_2.size[1] * 0.2)))
    # st.image(image_2, caption='Sunrise by the mountains')
    #
    # image_3 = Image.open('./image/' + file_dir[csv_file.iloc[i, 2]])
    # image_3 = image_3.resize((int(image_3.size[0] * 0.2), int(image_3.size[1] * 0.2)))
    # st.image(image_3, caption='Sunrise by the mountains')
    #
    # select_1 = st.checkbox('image 1',key = "label_1"+str(i))
    # select_2 = st.checkbox('image 2',key = "label_2"+str(i))
    # select_3 = st.checkbox('image 3',key = "label_3"+str(i))
    # bt = st.button("OK")
    # print(bt)
