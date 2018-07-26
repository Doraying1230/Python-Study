# Python_TagCloud

### Python练手项目

---
#### 标签云
支持命令行操作，可针对Excel、Word(docx)、txt文本进行提取关键词，统计词频并生成词汇云。

针对Excel：
```
python main.py test.xlsx -k 10
```
针对Word(docx)、txt文本：
```
python normal.py test.docx -k 10
```

---

#### 文本相似度计算

支持命令行操作，可计算docx、txt两种格式任意两文本间的文本相似度（根据情况可能要自行调整停用词）。

使用TF-IDF模型构建。

```
python similarity.py test1.docx test2.txt
```

#### 依赖解决

```
pip install -r requirements.txt
```

生成中文标签云需要添加字体文件，配置文件位置：
```
# 使用whereis查看python安装位置
whereis python
# 得到形如：/usr/local/lib/python3.5
vim /usr/local/lib/python3.5/dist-packages/pytagcloud/fonts/fonts.json
```
写入以下内容（注意json格式）
```
{
        "name": "YaHei",
        "ttf": "MicrosoftYaHeiMono.ttf",
        "web": "None"
        }
```
复制字体文件
```
cp MicrosoftYaHeiMono.ttf /usr/local/lib/python3.5/site-packages/pytagcloud/fonts
```

### 开发环境及测试环境

开发环境：

WSL + Python 3.5

测试环境:

Ubuntu 16.04 + Python 3.5

Mac OS 10.12 + Python 3.6
