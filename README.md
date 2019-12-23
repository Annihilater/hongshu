# hongshu

对红薯小说网进行 `js` 解密

- 框架：`Scrapy`
- 数据存储：`MongoDB`
- `js` 解密：使用 `PyExecJS` 库执行解密函数，对章节内容进行解密

## 解密过程

![img](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-23-075632.png)

![img](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-23-075641.png)

解密过程涉及到的函数有：

- `utf8to16`
- `hs_decrypt`（`long2str`、`str2long`）
- `base64decode`

简单直接的就是在 Python 内调用 `execjs` 库执行这些解密函数进行解密。

## 效果截图

![image-20191223153102496](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-23-073103.png)

![image-20191223153117665](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-23-073118.png)