import com.gargoylesoftware.htmlunit.BrowserVersion;
import com.gargoylesoftware.htmlunit.ProxyConfig;
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.*;

import java.net.URLEncoder;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;

class Tianyancha {

    private WebClient webClient;

    Tianyancha() {
        // 关闭 Warning
        Logger.getLogger("com.gargoylesoftware.htmlunit").setLevel(Level.OFF);
        // 初始化 WebClient
        webClient = new WebClient(BrowserVersion.CHROME);   // 浏览器版本为谷歌浏览器
        webClient.getOptions().setTimeout(30000);           // 超时时间 30s
        webClient.getOptions().setCssEnabled(false);        // 禁用 css
        webClient.getOptions().setJavaScriptEnabled(false); // 禁用 js
    }

    void setProxy(String host, String port) throws Exception {
        ProxyConfig proxyConfig = new ProxyConfig(host, Integer.parseInt(port));
        webClient.getOptions().setProxyConfig(proxyConfig);
    }

    boolean checkProxy() throws Exception {
        HtmlPage htmlPage = webClient.getPage("https://www.baidu.com");
        String title = htmlPage.getTitleText();
        return title.contains("百度");
    }

    String getCompanyLocation(String company) throws Exception {
        // 搜索
        HtmlPage searchPage = webClient.getPage("https://www.tianyancha.com/search?key=" + URLEncoder.encode(company, "utf-8"));
        String content = searchPage.asText();
        if (content.contains("获取验证码")) {
            // 需要登录
            return "0";
        } else if (content.contains(company)) {
            // 找到详情页
            HtmlAnchor searchResult = searchPage.getFirstByXPath("//*[@id=\"web-content\"]/div/div/div/div[1]/div[4]/div[1]/div[2]/div[1]/a");
            if (searchResult == null) {
                searchResult = searchPage.getFirstByXPath("//*[@id=\"web-content\"]/div/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/a");
            }
            if (searchResult == null) {
                searchResult = searchPage.getFirstByXPath("//*[@id=\"web-content\"]/div/div/div/div[1]/div[3]/div/div[2]/div[1]/a");
            }
            // 获取到公司的详细信息
            if (searchResult != null) {
                String href = searchResult.getHrefAttribute();
                if (Pattern.matches("^https://www.tianyancha.com/company/\\d+$", href)) {
                    HtmlPage detailPage = webClient.getPage(href);
                    HtmlSpan location = detailPage.getFirstByXPath("//*[@id=\"company_web_top\"]/div[2]/div[2]/div/div[3]/div[2]/span[2]");
                    if (location == null) {
                        location = detailPage.getFirstByXPath("//*[@id=\"company_web_top\"]/div[2]/div[2]/div[1]/div[2]/div[2]/span[2]");
                    }
                    return location.asText();
                }
            }
        }
        return "-1";
    }
}
