- **题目名称：** 简单爱
- **题目类型：** Misc
- **题目难度：** 中等
- **出题人：** gbljdgb
- **考点：** AI入门

# 题目描述
古典加密算个啥?赛博加密才是最抽象的!

* 提供训练代码,遮住对应映射
* 提供`charset`
* 提供训练好的checkpoint
* 提供输出后的字符串

# WP:
把每个字母都放进去前向传播一遍出来,就可以知道对应映射了,逆推就行
```python
import torch
import torch.nn as nn
import torch.optim as optim
from random import shuffle

# 定义神经网络模型
class SimpleStringMappingModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(SimpleStringMappingModel, self).__init__()
        self.fc = nn.Linear(input_size, output_size)
    
    def forward(self, x):
        x = self.fc(x)
        return x
    
charset = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}_"
char_to_index = {char: index for index, char in enumerate(charset)}
index_to_char = {index: char for index, char in enumerate(charset)}

# 创建模型实例
model = SimpleStringMappingModel(len(charset), len(charset))
model.load_state_dict(torch.load('checkpoint.pth'))

# 数据预处理：将字符串映射为 one-hot 编码的张量,类似[0,0,0,1,0,0,0,0,...]
def string_to_one_hot_tensor(input_string, charset, char_to_index):
    tensor = torch.zeros(len(input_string), len(charset))
    for i, char in enumerate(input_string):
        index = char_to_index[char]
        tensor[i][index] = 1
    return tensor

# 数据后处理：将 one-hot 编码的张量(1,len(charset))映射回字符串
def one_hot_tensor_to_string(output_tensor, index_to_char):
    output_string = index_to_char[output_tensor.argmax(1).item()]
    return output_string

model.eval()
for i in charset:
    print(one_hot_tensor_to_string(model(string_to_one_hot_tensor(i,charset,char_to_index)),index_to_char),end="")

print("")

# 假设这是另外一个文件
# 输入qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}_
# 输出VY#057dszPfJKMHXn*rLxc92Z83o!I)S{Ej1ANWm}puU$Be@T4iwyDgt_k%6QhC&b^(aRFqGOlv
a = "VY#057dszPfJKMHXn*rLxc92Z83o!I)S{Ej1ANWm}puU$Be@T4iwyDgt_k%6QhC&b^(aRFqGOlv"
b = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(){}_"
# a->b,反映射
output = "_@k}4OhsrD}#ev8UrD}WfvFa(^R&FbCvWf@7veqGUv)))vesvovwfmKvsvNfZ}vovP3fpvk}4v4U%Wv@w!3BvH39#v8!v8srD5!el"
# 开始逆推
for i in output:
    print(b[a.index(i)],end="")
```