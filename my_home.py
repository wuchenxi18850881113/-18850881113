'''我的主页'''
#python -m streamlit run C:\Users\Administrator\Desktop\我的网络根据地\my_home.py
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页',["我的兴趣推荐","我的图片处理工具","我的智能词典","我的留言区"])
def page_1():
    '''我的兴趣推荐'''
    st.image('slogan.png')
    #st.write('')
    #st.write('')
        
        
def page_2():
    '''我的图片处理工具'''
    st.write(":u7981:图片换色小程序:u7981:")
    uploaded_file = st.file_uploader("上传图片",type=["png","jpeg","jpg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))



def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt','r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt','r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:', times_dict[n])


    
        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world')
                    ''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()

            
def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r', encoding='utf-8') as f:
        messages_list =f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🈲'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🈳'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是.....',['阿短','编程猫'])
    new_message = st.text_input('想要说的话.....')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name, new_message])
        with open('leave_messages.txt', 'w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message_list += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc,gc,bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r, g, b)
    return img
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()