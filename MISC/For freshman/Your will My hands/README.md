* **题目名称：** Your will My hands

* **题目类型：** MISC

* **题目难度：** 简单

* **出题人：** hututu

* **考点：**  

1. 盲水印



* **描述：**  我用双手成就你的梦想

* **flag：** XSCTF{I_will_see_this_through}

* **Writeup：**  

  盲僧，盲水印一把缩。因为图片带有百度百科的水印，原图就可以直接拿到。
  
  直接用github项目https://github.com/chishaxie/BlindWaterMark解码拿到flag
  
  ```
  python3 bwmforpy3.py decode mangsheng.png challenge.png flag.png
  ```
  
  
