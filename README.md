
# 基于压缩感知技术的目标跟踪实现(Implementation of Object Tracking by Compressive Sensing Technology)

## 01 前情了解
**压缩感知技术**

## 02 实现思路
> 主要设计技术：
> - Python 3.10 `pywifi`
> - WiFi 
> - 小程序 

具体步骤：
1. 收集某场所的WiFi数据。如25幢一楼，电脑端跑python代码，使用`pywifi`库进行收集记录，得到一楼各点的WiFi信号数据，数据的格式为[位置编号，WiFi1的强度，WiFi2的强度，...]。以每块地砖的角为起始点，收集每个地砖交接点的WiFi信号数据，每个角收集10份数据，7/3或8/2划分数据集，用于后续测试。
2. 使用收集的数据集，分析设备当前接收到的数据信息，实现电脑端的位置定位。由于设备硬件问题，定位的准确度可以预见的不会太准。
3. 实现信息交互微信小程序。将移动设备拓展到手机端，发送收集到的当前手机上的WiFi信号数据，主要是SSID和信号强度，至服务器。
4. 实现数据分析压缩感知算法。通过此算法得到定位结果。
5. 搭一个在线服务器（网站），接收小程序所发送的信息，后端接收数据后进行分析，返回一个位置结果。
6. 小程序接收结果，显示当前位置


-------------


缺陷：
- 实时性不足。如果改成一个本地的app或许能好一点，but还是得跑代码，肯定能做到信号的捕获，但分析得到结果这一步实现的可能性不算太高
- 可靠性未知。单纯依靠WiFi的强度，标记点的距离如果只相隔一米的话分析的结果可能不是很准，
- 创新性：好像没什么创新性



# Implementation of Object Tracking by Compressive Sensing Technology
## 01 Former understanding
**Compressive Sensing Technology**

## 02 Implement ideas
Main design techniques:

> Python 3.10 
> - WiFi
> - Mini program 


Specific steps:
1. Collect Wi-Fi data for a location. For example, on the first floor of 25 buildings, the computer runs python code, uses the pywifi library to collect and record, and obtains Wi-Fi signal data of each point on the first floor, and the format of the data is [location number, strength of WiFi1, strength ,... of WiFi2]. Take the corner of each floor tile as the starting point, collect the Wi-Fi signal data of each floor tile junction, collect 10 pieces of data for each corner, and divide the data set 7/3 or 8/2 for subsequent testing.
2. Use the collected data set to analyze the data information currently received by the device to achieve the location of the computer. Due to equipment hardware problems, the accuracy of positioning can be predictably not too accurate.
3. Realize information interaction WeChat mini program. Extend the mobile device to the mobile phone and send the collected Wi-Fi signal data of the current mobile phone, mainly SSID and signal strength, to the server.
4. Implement data analysis compressed sensing algorithms. The positioning result is obtained by this algorithm. 
5. Set up an online server (website), receive the information sent by the mini program, and the backend receives the data and analyzes it and returns a location result. 
6. The applet receives the result and displays the current location



Flaw:
> - Lack of real-time. If you change to a local app, it may be better, but you still have to run the code, and you can definitely capture the signal, but the possibility of analyzing the results is not too high
> - Reliability unknown. Relying solely on the strength of Wi-Fi, the distance between the marked points may not be very accurate if they are only one meter apart. 
> - Innovative: It doesn't seem to be innovative


