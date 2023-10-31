import it.unisa.dia.gas.jpbc.Element;
import it.unisa.dia.gas.jpbc.Field;
import it.unisa.dia.gas.jpbc.Pairing;
import it.unisa.dia.gas.plaf.jpbc.pairing.PairingFactory;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Properties;

/**
 * @Author 9695
 * @Date 2023/10/18 23:03
 * @Version 1.0
 */
public class Task {

    public static void main(String[] args) throws FileNotFoundException {
        // 将flag转换成01串，类似 python 的 bytes_to_long
        // 恢复出的 01 串可以直接使用 long_to_bytes(0bxxxxxxx)转换
        String flag = Secret.getflag();
        flag = flag.replace("XSCTF{","").replace("}","");
        String flag_bin = Bytes2Bit(flag.getBytes(StandardCharsets.UTF_8));

        String dir = "data/";
        String pkFileName = dir + "pk.properties";
        String GameName = dir + "Game.properties";
        String outputName = dir + "Game.txt";

        // 从 a.properties 读取椭圆曲线参数并生成曲线
        // q 是素数，并且有 q+1 = rh
        // exp1,exp2,sign1,sign0 是用于生成 r 的参数
        // 这是一条在有限域 Fq 上的椭圆曲线 y^2 = x^3 + x，即 E(Fq)，它包含了 q+1 个点
        // G1 是椭圆曲线上的点群，它的阶为 r
        // Zn 是模 r 的整数环
        Pairing curve = PairingFactory.getPairing("a.properties");
        Field G1 = curve.getG1();
        Field Zn = curve.getZr();

        // 从 pk.properties 中读取群 G 的生成元 g
        // properties 支持键值读取
        // 先加载文件，然后直接按名字 "g" 读取，就会读取 g=xxxxxxxx 的内容 xxxxxxxx
        String g_string = loadPropFromFile(pkFileName).getProperty("g");
        byte[] g_byte = Base64.getDecoder().decode(g_string);
        Element g = G1.newElementFromBytes(g_byte).getImmutable();

        // 给了两种存储结果
        // 一种是 output.txt 直接存的点的表示，结构为（x,y,0），其中(x,y)是椭圆曲线上点的坐标，后面的 0 是个标志位不用管
        // 一种是用 properties 存的字节流，并将字节编码为base64，方便显示
        PrintStream out = new PrintStream(new FileOutputStream(outputName));
        System.setOut(out);
        Properties gameProp = new Properties();
        for (int i = 0; i < flag_bin.length(); i++) {
            Element a = Zn.newRandomElement().getImmutable();
            Element b = Zn.newRandomElement().getImmutable();
            Element c = Zn.newRandomElement().getImmutable();
            assert c!=a.mul(b);
            if('1' == flag_bin.charAt(i)){
                c = a.mul(b);
            }
            Element ga = g.powZn(a);
            Element gb = g.powZn(b);
            Element Z = g.powZn(c);
            //为了避免乱码问题，统一采用Base64编码为可读字符串形式。虽然可不可读都差不多
            gameProp.setProperty("ga"+i,Base64.getEncoder().encodeToString(ga.toBytes()));
            gameProp.setProperty("gb"+i,Base64.getEncoder().encodeToString(gb.toBytes()));
            gameProp.setProperty("Z"+i,Base64.getEncoder().encodeToString(Z.toBytes()));
            System.out.println(ga);
            System.out.println(gb);
            System.out.println(Z);
            System.out.println("---");
        }
        storePropToFile(gameProp, GameName);
        out.close();
    }

    // 将 Properties 对象保存为文件
    public static void storePropToFile(Properties prop, String fileName){
        try(FileOutputStream out = new FileOutputStream(fileName)){
            prop.store(out, null);
        }
        catch (IOException e) {
            e.printStackTrace();
            System.out.println(fileName + " save failed!");
            System.exit(-1);
        }
    }

    // 读取文件为 Properties 对象
    public static Properties loadPropFromFile(String fileName) {
        Properties prop = new Properties();
        try (FileInputStream in = new FileInputStream(fileName)){
            prop.load(in);
        }
        catch (IOException e){
            e.printStackTrace();
            System.out.println(fileName + " load failed!");
            System.exit(-1);
        }
        return prop;
    }

    public static String Byte2Bit(byte b){
        StringBuffer sb = new StringBuffer();
        sb.append((b>>7)&0x1)
                .append((b>>6)&0x1)
                .append((b>>5)&0x1)
                .append((b>>4)&0x1)
                .append((b>>3)&0x1)
                .append((b>>2)&0x1)
                .append((b>>1)&0x1)
                .append((b>>0)&0x1);
        return sb.toString();
    }

    public static String Bytes2Bit(byte[] bs){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bs.length; i++) {
            sb.append(Byte2Bit(bs[i]));
        }
        return sb.toString();
    }
}
