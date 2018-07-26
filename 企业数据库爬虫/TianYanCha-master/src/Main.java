import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.regex.Pattern;

public class Main {

    public static void main(String[] args) throws Exception {
        System.out.println("请确保文件全部使用 utf-8 编码格式！");
        if (args.length == 3 && args[0].equals("-t") && (new File(args[1]).canRead()) && (new File(args[2]).canWrite())) {
            transform(args[1], args[2]);
        } else if (args.length == 2 && args[0].equals("-g") && (new File(args[1]).canRead())) {
            gain(args[1], new Tianyancha());
        } else {
            System.out.println("可用的命令：");
            System.out.println("     -t [old_filename] [new_filename] 将公司名转换成一行一个");
            System.out.println("     -g [filename]                    获取公司信息");
        }
    }

    private static void transform(String oldFilename, String newFilename) throws Exception {
        // 文件流
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(oldFilename), "utf-8"));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(newFilename), "utf-8"));
        String temp = bufferedReader.readLine();
        while (temp != null) {
            // 清除前面和后面的空白
            temp = temp.trim();
            // 将多个空白字符转换成一个空格
            temp = temp.replaceAll("\\s+", " ");
            // 用一个空格分割文本
            StringTokenizer stringTokenizer = new StringTokenizer(temp, " ");
            while (stringTokenizer.hasMoreElements()) {
                // 获取一个公司名称
                String token = stringTokenizer.nextToken();
                // 写入文件
                bufferedWriter.write(token);
                bufferedWriter.newLine();
                bufferedWriter.flush();
                // 输出到控制台
                System.out.println(token);
            }
            // 再读入一行
            temp = bufferedReader.readLine();
        }
        // 关闭流
        bufferedWriter.close();
        bufferedReader.close();
    }

    private static void gain(String filename, Tianyancha tianyancha) throws Exception {
        // 文件流
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(filename), "utf-8"));
        BufferedWriter bufferedWriterSuccess = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("success_" + System.currentTimeMillis() + ".txt"), "utf-8"));
        BufferedWriter bufferedWriterError = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("error_" + System.currentTimeMillis() + ".txt"), "utf-8"));
        // 读取公司名称
        String company = bufferedReader.readLine();
        while (company != null) {
            System.out.println(company + " 正在获取...");
            String location = tianyancha.getCompanyLocation(company);
            switch (location) {
                case "-1":
                    bufferedWriterError.write(company);
                    bufferedWriterError.newLine();
                    bufferedWriterError.flush();
                    System.out.println(company + " 没有找到相关结果！");
                    break;
                case "0":
                    System.out.println("当前ip已被限制！");
                    while (true) {
                        Scanner scanner = new Scanner(System.in);
                        System.out.print("请输入主机地址：");
                        String host = scanner.nextLine();
                        System.out.print("请输入端口号：");
                        String port = scanner.nextLine();
                        if (Pattern.matches("([1-9]|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])(\\.(\\d|[1-9]\\d|1\\d{2}|2[0-4]\\d|25[0-5])){3}", host)) {
                            tianyancha.setProxy(host, port);
                            if (tianyancha.checkProxy()) {
                                System.out.println("成功设置代理：" + host + ":" + port);
                                break;
                            } else {
                                System.out.println("当前代理不可用！");
                            }
                        } else {
                            System.out.println("主机地址不合法！");
                        }
                    }
                    break;
                default:
                    bufferedWriterSuccess.write(company + " " + location);
                    bufferedWriterSuccess.newLine();
                    bufferedWriterSuccess.flush();
                    System.out.println(company + " 获取成功！");
                    break;
            }
            // 下一个公司名称
            Thread.sleep(1000);
            company = bufferedReader.readLine();
        }
        // 关闭文件流
        bufferedWriterError.close();
        bufferedWriterSuccess.close();
        bufferedReader.close();
    }
}
