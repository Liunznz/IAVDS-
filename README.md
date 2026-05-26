# IAVDS：图片内容智能审核与违规检测系统
开发一款面向内容审核团队和企业合规部门的图片智能审核系统，实现自动化违规检测、敏感词管理、申诉处理及统计报表，提高审核效率与准确性。

# 图片内容智能审核与违规检测系统

基于 Python 3 与 PyQt6 的内容安全智能审核与违规检测软件。本系统面向内容审核团队、企业合规部门及互联网平台，
提供从图片上传、AI违规检测、OCR 敏感词识别、批量并发审核、历史检索、申诉复审到统计报表的全流程解决方案。

## 功能模块

| 菜单 | 说明 |
|------|------|
| 单张图片审核 | 支持拖拽/按钮上传图片，AI 内容检测（色情/暴力/政治敏感），OCR 文字识别与敏感词高亮，审核结果保存，PDF 报告导出 |
| 批量图片审核 | 多选文件或添加文件夹，多线程并发审核，任务优先级调整，进度监控，结果汇总入库，CSV 汇总表导出 |
| 审核历史记录 | 多条件组合查询（日期、状态、结论、关键词），详情弹窗（缩略图、OCR 高亮），逻辑删除，申诉发起，单条报告导出 |
| 敏感词库管理 | 树形分类维护（政治敏感/色情/暴力/其他），增删改查，批量导入/导出（TXT/CSV），实时测试高亮，内存缓存同步 |
| 检测模型配置 | 调节三类置信度阈值（色情/暴力/政治敏感），开关 OCR 与哈希检测，配置 JSON 持久化，热加载生效，未保存提示 |
| 误报申诉处理 | 申诉工单列表与状态流转（待处理→复审中→已撤销/已维持），复审界面左右对比原图与检测结果，站内信模拟通知 |
| 统计报表 | 时间范围筛选（最近7天/今日/本周/本月/自定义），审核总量/通过率/驳回率卡片，每日趋势折线图，违规类别饼图，审核员工作量柱状图，Excel 导出 |
| 用户管理 | 三级权限（管理员/审核员/普通用户），递归权限校验，用户增删改查，重置密码，解锁账户，角色筛选与分页 |
| 数据备份 | 手动备份（数据库+图片目录），ZIP 打包，MD5 完整性校验，备份列表管理，还原与校验 |
| 帮助中心 | 树形目录导航，富文本（HTML）手册展示，关键词搜索与高亮跳转，常见问题折叠面板 |
| 关于系统 | 版本信息、技术栈、开源许可展示，模拟检查更新 |

## 部分截图

<img width="777" height="771" alt="image" src="https://github.com/user-attachments/assets/2b2e8f55-aedb-4dff-b4a3-090c4f4268d7" />
<img width="651" height="693" alt="image" src="https://github.com/user-attachments/assets/c9805160-62a7-4261-99d5-7880bb39fe67" />

## 技术栈

- **语言**：Python 3.10+
- **GUI 框架**：PyQt6
- **深度学习 OCR**：EasyOCR（支持中英文）
- **图像处理**：OpenCV、Pillow
- **图表可视化**：Matplotlib
- **数据库**：SQLite
- **热更新**：Watchdog
- **报表生成**：ReportLab（PDF）、OpenPyXL（Excel）
- **打包工具**：PyInstaller、Inno Setup

## 本地运行

```
# 安装依赖
pip install -r requirements.txt

# 启动程序
python main.py
```

**默认账号**：`admin`  
**默认密码**：`admin123`

> 首次启动会自动初始化 SQLite 数据库，创建必要的表（用户表、审核记录表、敏感词表、登录尝试表），并插入默认管理员账号。
> 运行程序会下载EasyOCR，需要科学上网
[系统加载] 正在初始化 OCR 深度学习模型 (中英双语)...
Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
Downloading detection model, please wait. This may take several minutes depending upon your network connection.
Progress: |██████████████████████████████████████████████████| 100.0% CompleteDownloading recognition model, please wait. This may take several minutes depending upon your network connection.
Progress: |██████████████████████████████████████████████████| 100.0% Complete[系统加载] OCR 模型加载完毕！
> 可以测试的审核图片文件夹test_img，目前这个EasyOCR可以识别test_img里面背景为黑色的图片的文字，彩色有噪点的识别不出来

## 使用说明

详细操作请参阅系统内「帮助中心」或随项目文档提供的《操作手册》。
<img width="984" height="468" alt="image" src="https://github.com/user-attachments/assets/8cb238fe-2f3a-42ee-af54-328d614b9c41" />
<img width="723" height="762" alt="image" src="https://github.com/user-attachments/assets/5b521324-fac3-409a-9dc7-8ff6ea41b596" />
核心流程：
1. **登录/注册**：使用默认账号登录，或注册新账户（需邮箱验证）。
2. **单张审核**：上传图片 → 自动检测（内容分类+OCR）→ 人工确认 → 保存结果或导出 PDF。
3. **批量审核**：导入多个图片 → 设置并发数 → 开始审核 → 保存入库 → 导出 CSV 汇总。
4. **敏感词库**：按分类添加/导入敏感词 → 在测试区验证高亮效果 → 词库变更实时生效。
5. **模型配置**：调整置信度阈值或功能开关 → 保存并热加载 → 无需重启即可生效。
6. **申诉处理**：用户从历史记录发起申诉 → 审核员在申诉模块复审 → 撤销或维持原判。
7. **统计报表**：选择时间范围 → 生成图表与卡片 → 导出 Excel 报表。
8. **用户管理**（管理员）：创建/编辑/删除用户，分配角色，重置密码，解锁账户。
9. **数据备份**：手动备份数据库与图片 → 支持 MD5 校验还原。



## 下载EasyOCR遇到超时问题解决办法
要解决这个OCR超时崩溃，需要手动下载模型并放进对应的文件夹，告诉 EasyOCR 直接用本地的就行了。请按以下三步操作：
第一步：创建本地模型存放目录
在你的 Windows 电脑上，打开系统文件资源管理器，进入你的用户目录，并新建对应的文件夹。
进入路径：C:\Users\<你的电脑用户名> (例如 C:\Users\Administrator 或你自己起的名字)。
在该目录下，新建一个文件夹命名为 .EasyOCR（注意前面有个小数点）。
进入 .EasyOCR 文件夹，在里面再新建一个文件夹命名为 model。
最终的完整路径应该是这样的：C:\Users\<你的用户名>\.EasyOCR\model\

第二步：手动下载2个核心模型
使用你的浏览器（如果浏览器有代理/科学上网插件最好）或者迅雷，把下面2个模型文件下载到本地：
1. 文本检测基础模型（必须）：
下载链接: https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip
2. 简体中文识别模型：
下载链接: https://github.com/JaidedAI/EasyOCR/releases/download/v1.3/zh_sim_g2.zip
⚠️ 关键操作：解压文件
下载好这三个 .zip 压缩包后，请把它们解压。里面分别会包含一个后缀为 .pth 的文件。把你提取出来的 2个 .pth 文件直接丢进第一步建好的 model 文件夹里。
最终你的 model 文件夹里应该直接平铺这 2个文件：
craft_mlt_25k.pth
zh_sim_g2.pth
第三步：修改代码（断开网络依赖）
现在文件都在本地了，为了防止 EasyOCR 以后启动时再去傻傻地请求网络检查更新，我们需要在代码里加上禁止自动下载的参数 download_enabled=False。
将你的 OCRDetector 的 __init__ 方法略微修改一下：
    def __init__(self):
        print("[系统加载] 正在初始化 OCR 深度学习模型 (中英双语)...")
        try:
            # 加入 download_enabled=False，强迫它只找刚刚放好的本地文件，不走网络！
            self.reader = easyocr.Reader(
                ['ch_sim', 'en'], 
                gpu=False, 
                download_enabled=False 
            )
            print("[系统加载] OCR 模型加载完毕！")
        except Exception as e:
            print(f"[错误] OCR 模型加载失败: {e}")
            self.reader = None
保存代码，重新运行项目。这次就能看到 [系统加载] OCR 模型加载完毕！
