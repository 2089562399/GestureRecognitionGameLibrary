import cv2
import math
from cv2 import flip
import mediapipe as mp
import threading
import time,os
# from cvzone.ClassificationModule import Classifier
import numpy as np

# classifer = Classifier("Model/keras_model.h5", "Model/labels.txt")
# labels = ["1", "2", "OK"]

class hands:
  def __init__(self) -> None:
    self.direction = 0
    self.is_start = False
    self.cx_8 = 0
    self.cy_8 = 0
    self.is_select = False

    self.x_between_finger_tip = 0
    self.y_between_finger_tip = 0

    self.index = 1

    self.str_guester = None   # 算法放回的手势

    self.pattern = 5         # 拼图游戏的手势识别

    # 中指与矩形左上角点的距离
    self.L1 = 0
    self.L2 = 0

  def get_str_guester(self, up_fingers,list_lms):
      
      if len(up_fingers)==1 and up_fingers[0]==8:
          
          v1 = list_lms[6]-list_lms[7]
          v2 = list_lms[8]-list_lms[7]
          
          angle = np.dot(v1,v2)/(np.sqrt(np.sum(v1*v1))*np.sqrt(np.sum(v2*v2)))
          angle = np.arccos(angle)/3.14*180
        
          if angle<160:
              str_guester = "9"
          else:
              str_guester = "1"
      
      elif len(up_fingers)==1 and up_fingers[0]==4:
          str_guester = "Good"
      
      elif len(up_fingers)==1 and up_fingers[0]==20:
          str_guester = "Bad"
          
      elif len(up_fingers)==1 and up_fingers[0]==12:
          str_guester = "FXXX"
    
      elif len(up_fingers)==2 and up_fingers[0]==8 and up_fingers[1]==12:
          str_guester = "2"
          
      elif len(up_fingers)==2 and up_fingers[0]==4 and up_fingers[1]==20:
          str_guester = "6"
          
      elif len(up_fingers)==2 and up_fingers[0]==4 and up_fingers[1]==8:
          str_guester = "8"
      
      elif len(up_fingers)==3 and up_fingers[0]==8 and up_fingers[1]==12 and up_fingers[2]==16:
          str_guester = "3"
          self.pattern = 3
      
      elif len(up_fingers)==3 and up_fingers[0]==4 and up_fingers[1]==8 and up_fingers[2]==12:
    
          dis_8_12 = list_lms[8,:] - list_lms[12,:]
          dis_8_12 = np.sqrt(np.dot(dis_8_12,dis_8_12))
          
          dis_4_12 = list_lms[4,:] - list_lms[12,:]
          dis_4_12 = np.sqrt(np.dot(dis_4_12,dis_4_12))
          
          if dis_4_12/(dis_8_12+1) <3:
              str_guester = "7"
          
          elif dis_4_12/(dis_8_12+1) >5:
              str_guester = "Gun"
          else:
              str_guester = "7"
              
      elif len(up_fingers)==3 and up_fingers[0]==4 and up_fingers[1]==8 and up_fingers[2]==20:
          str_guester = "ROCK"
      
      elif len(up_fingers)==4 and up_fingers[0]==8 and up_fingers[1]==12 and up_fingers[2]==16 and up_fingers[3]==20:
          str_guester = "4"
          self.pattern = 4
      
      elif len(up_fingers)==5:
          str_guester = "5"
          self.pattern = 5
          
      elif len(up_fingers)==0:
          str_guester = "10"
      
      else:
          str_guester = " "
          
      return str_guester


  def handcontroller(self):
    mp_drawing = mp.solutions.drawing_utils   # 获取mediapipe解决方案的绘画工具包
    mp_drawing_styles = mp.solutions.drawing_styles  # 渲染风格
    mp_hands = mp.solutions.hands  # 绘人手
    cap = cv2.VideoCapture(0)  # 打开编号为0的摄像头，这个一般是自带摄像头
    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:  # 最小追踪置信度
      while cap.isOpened():
        success, image = cap.read()  # 从cap中读取图片到img，并将读取是否成功的结果保存在success

        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.如果加载视频，使用“中断”而不是“继续”。
          continue

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        # 若要提高性能，可以选择将图像标记为不可写以通过引用传递。
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 模型训练的时候是使用RGB训练，对于这个类型识别精度和速度比较高
        results = hands.process(image)  # 将RGB图片输入手部模型将结果保存在result

        # Draw the hand annotations on the image.在图像上绘制手部批注。
        image.flags.writeable = True  # 将图像标记为可写
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # 将 BGR 图像转换为 RGB
        if results.multi_hand_landmarks:  # 如果multi_hand_landmarks不为空进入循环
          for hand_landmarks in results.multi_hand_landmarks:  # 遍历multi_hand_landmarks内每一个hand_landmark（手部关键点），相对于遍历图片中每一个手
            
            hand_vector = []
            # 采集所有关键点的坐标
            list_lms = []   
            mp_drawing.draw_landmarks(  # 调用mediapipe内绘画工具包绘画手部关键点
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                # mp_drawing_styles.get_default_hand_landmarks_style(),
                # mp_drawing_styles.get_default_hand_connections_style()
                )
            
            for id, lm in enumerate(hand_landmarks.landmark):  # 返回枚举类型（手势标记点）中每个点对应的索引值和自身值
                # print(id, lm)
                h, w, c = image.shape  # 获取图像的高度、宽度、通道数
                cx, cy = int(lm.x * w), int(lm.y * h)
                list_lms.append([int(cx),int(cy)])

                if id ==5  or id == 8 or id == 4 or id == 12: # 获取索引值为5和8的标记点
                  temporary_list = [cx, cy]
                  hand_vector.append(temporary_list)
                  # print(id, cx, cy)  #打印对应点位的坐标
                  # cv2.circle(image, (cx, cy), 10, (0, 0, 0), cv2.FILLED)
            
            '''外部指头数量'''
            # 构造凸包点
            list_lms = np.array(list_lms,dtype=np.int32)
            hull_index = [0,1,2,3,6,10,14,19,18,17,10]
            hull = cv2.convexHull(list_lms[hull_index,:])
            # 绘制凸包
            cv2.polylines(image,[hull], True, (0, 255, 0), 2)
                        # 查找外部的点数
            n_fig = -1
            ll = [4,8,12,16,20] 
            up_fingers = []
            
          
            for i in ll:
                pt = (int(list_lms[i][0]),int(list_lms[i][1]))
                dist= cv2.pointPolygonTest(hull,pt,True)
                if dist <0:
                    up_fingers.append(i)
            
            self.str_guester = self.get_str_guester(up_fingers,list_lms)
            
            
            cv2.putText(image,' %s'%(self.str_guester),(90,90),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,0),4,cv2.LINE_AA)
            if self.str_guester == "1":
              self.index = 1
            if self.str_guester == "2":
              self.index = 2
            if self.str_guester == "3":
              self.index = 3

            '''方向以及ok'''
            reference_vector = [hand_vector[2][0]-hand_vector[1][0],hand_vector[2][1]-hand_vector[1][1]]
            start_vector = [hand_vector[2][0]-hand_vector[0][0],hand_vector[2][1]-hand_vector[0][1]]

            '''获取点击操作 右上角（0，0） 640*480 -> 640*640'''
            # 获取中间点
            between_finger_tip = ((hand_vector[3][0]+hand_vector[2][0])//2, (hand_vector[3][1]+hand_vector[2][1])//2 * 4 //3)
            self.x_between_finger_tip = between_finger_tip[0]
            self.y_between_finger_tip = between_finger_tip[1]
            # 勾股定理计算长度
            line_len = math.hypot((hand_vector[2][0]-hand_vector[3][0]),(hand_vector[2][1]-hand_vector[3][1]))
            if self.is_select:
              if(line_len > 20):
                print("选择到未选择")
                self.is_select = False
            elif(line_len <20):
              print("从未选择到选择")
              self.is_select = True

            radian = math.acos((reference_vector[1])/pow(pow(reference_vector[0],2)+pow(reference_vector[1],2),0.5))  # b = [0,1] 竖直向下 计算弧度

            '''检测ok手势'''
            ok__bool = start_vector[1] < 25 and start_vector[1] >-25 and start_vector[0] < 25 and start_vector[0] >-25
            if self.is_start==False and ok__bool:
              self.is_start = True
              print("检测到ok手势,此时的index为:",self.index)
            if self.is_start:
              if ok__bool == False:
                self.is_start =False
                print("ok手势失效")

               
            if radian >=(3.14/4)*3:
              #print("上")
              self.direction = 0   
            elif radian <= 3.14/4:
              #print("下")
              self.direction = 1 
            else:
              if reference_vector[0]>0:
                # print("左")
                self.direction = 2 
              else:
                # print("右")
                self.direction = 3 


       
        # flip the image horizontally for a selfie-view display. 水平翻转图像以获得自拍视图显示。
        # cv2.flip(filename, flipcode)  filename：需要操作的图像 flipcode：翻转方式
        # 1：水平翻转  0：垂直翻转  -1：水平垂直翻转
        cv2.imshow('Hands', cv2.flip(image, 1)) 
        if cv2.waitKey(5) & 0xFF == 27:  # 程序等待5毫秒，按下按键是esc的时候返回true  esc键的ASCII值是27
          break
    cap.release()  # 停止捕获视频


def getarge(hand):
  while True:
    print("eee")
    time.sleep(1)

# 上：[-23,-286]  -小 -大
# 下：[110,226] 小 大
# 左：[226,-61] 大 -小
# 右：[-318,-10] -大 -小

if __name__=="__main__":
  
  
  hand = hands()
  # cx_8 = hand.cx_8
  # cy_8 = hand.cy_8
  # print("55555")
  # print(cx_8,cy_8)
  # print("66666")
  
  t1 = threading.Thread(target=hand.handcontroller)     # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
  # t2 = threading.Thread(target=hand.getarge)

  t1.start()
  # t2.start()
