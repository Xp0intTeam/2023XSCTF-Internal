import torch
import torch.nn as nn
import torch.optim as optim
from random import shuffle

# 定义字符集和字符到索引的映射
charset = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}_"
char_to_index = {char: index for index, char in enumerate(charset)}
index_to_char = {index: char for index, char in enumerate(charset)}

# 检查字符集是否存在重复字符
assert len(set(charset)) == len(charset)

# 定义神经网络模型
class SimpleStringMappingModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(SimpleStringMappingModel, self).__init__()
        self.fc = nn.Linear(input_size, output_size)
    
    def forward(self, x):
        x = self.fc(x)
        return x

# 创建模型实例
model = SimpleStringMappingModel(len(charset), len(charset))

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 建立训练集,input_string[i] -> 神经网络 -> target_string[i]
input_string = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}_" # 就是charset
""" def shuffle_str(s):
    # 将字符串转换成列表
    str_list = list(s)
    # 调用random模块的shuffle函数打乱列表
    shuffle(str_list)
    # 将列表转字符串
    return ''.join(str_list) """
target_string = ?????? /* 这地方被人删掉了555 */

# 数据预处理：将字符串映射为 one-hot 编码的张量,类似[0,0,0,1,0,0,0,0,...]
def string_to_one_hot_tensor(input_string, charset, char_to_index):
    tensor = torch.zeros(len(input_string), len(charset))
    for i, char in enumerate(input_string):
        index = char_to_index[char]
        tensor[i][index] = 1
    return tensor

# 把列表转one-hot矩阵
input_tensor_list = []
for i in input_string:
    input_tensor_list.append(string_to_one_hot_tensor(i, charset, char_to_index))
output_tensor_list = []
for i in target_string:
    output_tensor_list.append(string_to_one_hot_tensor(i, charset, char_to_index))

model.train()
# 训练模型
n_epochs = 10000
for epoch in range(n_epochs):
    loss_all = 0
    for inputs,targets in zip(input_tensor_list,output_tensor_list):
        # 前向传播
        output_tensor = model(inputs)

        # 计算损失
        loss = criterion(output_tensor, targets)
        loss_all += loss.item()
        
        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{n_epochs}], Loss: {loss_all/len(charset)}')

torch.save(model.state_dict(), 'checkpoint.pth')