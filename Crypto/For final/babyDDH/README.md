- **题目名称：** babyDDH
- **题目类型：** Crypto
- **题目难度：**中等
- **出题人：** =w=
- **考点：**

1. 能够结合注释读懂题目JAVA代码
2. 能够照葫芦画瓢使用JAVA读取properties文件
3. 能够掌握DDH的概念，理解双线性映射的功能

- **描述：** 
- **flag：** XSCTF{DDH_is_easy_with_bilinear_pairing_d9a01977eaad}
- **Writeup：**

在paring-friendly曲线中，利用双线性映射的性质判断 $e(g^a,g^b) = e(g,g)^{ab} = e(g,g^Z) $ 是否成立即可


```java
public class Solve {
    public static void main(String[] args) {
        // 载入jpbc的jar包，照抄题目附件初始化椭圆曲线，读取生成元 g
        Element g = 
        Properties GameProp = loadPropFromFile("data/Game.properties");
        for (int i = 0; i < 368; i++) {
            String gaString = GameProp.getProperty("ga"+i);
            Element ga = gG1.newElementFromBytes(Base64.getDecoder().decode(gaString)).getImmutable();
            Element gb = 
            Element Z = 
            // 读取 gb, Z 的方式同 ga
            if(curve.pairing(ga,gb).isEqual(curve.pairing(g,Z)))
                System.out.print("1");
            else
                System.out.print("0");
            // 输出的01字符串直接复制到python
            // XSCTF{long_to_bytes(0bxxxxxxxxxxxxxx)}
        }
    }
}
```
